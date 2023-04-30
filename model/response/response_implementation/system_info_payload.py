import datetime
import platform

import psutil

from model.response.base_payload import BasePayload
from util.memory_converter import memory_converter
from util.net_converter import nic_addr


# TODO need to protect, important information in this
class SystemInfoPayload(BasePayload):
    def __init__(self):
        self.boot = {
            "time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        }
        self.cpu = {
            "arch": platform.architecture()[0],
            "cpu": platform.machine(),
            "core": {
                "logical": psutil.cpu_count(),
                "physical": psutil.cpu_count(False)
            },
            "frequency": (psutil.cpu_freq(True)[0]),
            "processor": platform.processor(),
            "stats": {
                "ctx_switches": psutil.cpu_stats().ctx_switches,
                "interrupts": psutil.cpu_stats().interrupts,
                "soft_interrupts": psutil.cpu_stats().soft_interrupts,
                "syscalls": psutil.cpu_stats().syscalls,
            }
        }
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        self.memory = {
            "virtual": {
                "active": memory_converter(mem[4]),
                "available": memory_converter(mem[1]),
                "free": memory_converter(mem[3]),
                "percent": mem[2],
                "total": memory_converter(mem[0]),
            },
            "swap": {
                "free": memory_converter(swap[2]),
                "percent": swap[3],
                "total": memory_converter(swap[0]),
                "used": memory_converter(swap[1]),
            }
        }
        self.process = {
            p.pid : p.info for p in psutil.process_iter(['name', 'username'])
        }
        self.network = {
            "hostname": platform.node(),
            "interface": nic_addr(psutil.net_if_addrs(), psutil.net_io_counters(True))
        }
        self.os = {
            "release": platform.release(),
            "system": platform.system(),
            "version": platform.version(),
        }
        self.python = {
            "branch": platform.python_branch(),
            "build": platform.python_build(),
            "compiler": platform.python_compiler(),
            "implementation": platform.python_implementation(),
            "revision": platform.python_revision(),
            "version": platform.python_version()
        }

    def jsonify(self) -> {}:
        return self.__dict__

    def require_json_array(self) -> bool:
        return False

