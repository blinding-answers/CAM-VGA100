from ucam100.command import *


def command_from_hex(hex_command: str):
    # 6 Bytes = 12 hex chars
    if len(hex_command) < 12:
        raise Exception("6Byte hex expected")

    hex_command = hex_command.upper()
    hex_byte_array = [hex_command[i : i + 2] for i in range(0, len(hex_command), 2)]
    command = Command()
    command.id_number = hex_byte_array[0] + hex_byte_array[1]
    command.param_1 = hex_byte_array[2]
    command.param_2 = hex_byte_array[3]
    command.param_3 = hex_byte_array[4]
    command.param_4 = hex_byte_array[5]
    return command
