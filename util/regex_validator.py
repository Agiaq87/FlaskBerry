import re


def check_mac_address(mac_address: str) -> bool:
    return len(re.findall(re.compile(r'(?:[0-9a-fA-F]:?){12}'), mac_address)) != 0
