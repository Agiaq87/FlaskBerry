memory_unit = ["B", "KB", "MB", "GB", "TB", "PB"]


def memory_converter(byte: int) -> str:
    memory_index = 0

    while byte >= 1024:
        byte /= 1024
        memory_index += 1

    return f"{int(byte)}{memory_unit[memory_index]}"
