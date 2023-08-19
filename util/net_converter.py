from getmac import get_mac_address
from psutil._common import snetio, snicaddr

from util.memory_converter import memory_converter


def nic_addr(dictionary: {str, list[snicaddr]}, also_snetio: {str, snetio}) -> {}:
    t = {}
    for key in dictionary:
        t[key] = []
        if also_snetio[key] is not None:
            t[key].append(snetio(also_snetio[key]))

        for v in dictionary[key]:
            temp = {
                "address": v[1],
                "broadcast": v[3],
                "family": v[0],
                "netmask": v[2],
                "ptp": v[4]
            }
            t[key].append(temp)
    return t


def snetio(value: snetio) -> {}:
    return {
        "bytes": {
            "received": memory_converter(value[1]),
            "sent": memory_converter(value[0])
        },
        "package": {
            "received": memory_converter(value[3]),
            "sent": memory_converter(value[2])
        },
        "errin": value[4],
        "errout": value[5],
        "dropin": value[6],
        "dropout": value[7]
    }


def snetio_converter(dictionary: {str, snetio}) -> {}:
    t = {}
    for key in dictionary:
        value = dictionary[key]
        t[key] = {
            "bytes": {
                "received": memory_converter(value[1]),
                "sent": memory_converter(value[0])
            },
            "package": {
                "received": memory_converter(value[3]),
                "sent": memory_converter(value[2])
            },
            "errin": value[4],
            "errout": value[5],
            "dropin": value[6],
            "dropout": value[7]
        }
    return t


def mac_from_ip(ip_address: str) -> str | None:
    return get_mac_address(ip=ip_address, network_request=True)
