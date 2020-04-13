from abc import ABC


class Command(ABC):
    id_number = None
    param_1 = None
    param_2 = None
    param_3 = None
    param_4 = None

    def __str__(self):
        return (
            self.id_number + self.param_1 + self.param_2 + self.param_3 + self.param_4
        )

    def __eq__(self, value):
        return str(self) == str(value)


class InitialCommand(Command):
    COLOR_TYPE_2BIT_GRAY_SCALE = "01"
    COLOR_TYPE_4BIT_GRAY_SCALE = "02"
    COLOR_TYPE_8BIT_GRAY_SCALE = "03"
    COLOR_TYPE_12BIT_COLOR = "05"
    COLOR_TYPE_16BIT_COLOR = "06"
    COLOR_TYPE_JPEG = "07"

    PREVIEW_RES_80X60 = "01"
    PREVIEW_RES_160X120 = "03"

    JPEG_RES_80X64 = "01"
    JPEG_RES_160X128 = "03"
    JPEG_RES_320X240 = "5"
    JPEG_RES_640X480 = "07"

    def __init__(self, color_type, preview_res, jpeg_res):
        self.id_number = "AA01"
        self.param_1 = "00"
        self.param_2 = color_type
        self.param_3 = preview_res
        self.param_4 = jpeg_res


class GetPictureCommand(Command):
    PICTURE_TYPE_SNAPSHOT = "01"
    PICTURE_TYPE_PREVIEW = "02"
    PICTURE_TYPE_JPEG_PREVIEW = "05"

    def __init__(self, picture_type):
        self.id_number = "AA04"
        self.param_1 = picture_type


class SnapshotCommand(Command):
    SNAPSHOT_TYPE_COMPRESSED = "00"
    SNAPSHOT_TYPE_UNCOMPRESSED = "01"

    def __init__(self, snapshot_type, skip_frame_low_byte, skip_frame_high_byte):
        self.id_number = "AA05"
        self.param_1 = snapshot_type
        self.param_2 = skip_frame_low_byte
        self.param_3 = skip_frame_high_byte
        self.param_4 = "00"


class SetPackageSizeCommand(Command):
    def __init__(self, package_size_low_byte, package_size_high_byte):
        self.id_number = "AA06"
        self.param_1 = "08"
        self.param_2 = package_size_low_byte
        self.param_3 = package_size_high_byte
        self.param_4 = "00"


class SetBoadrateCommand(Command):
    BOADRATE_7200 = ("FF", "01")
    BOADRATE_9600 = ("BF", "01")
    BOADRATE_14400 = ("7F", "01")
    BOADRATE_19200 = ("5F", "01")
    BOADRATE_28800 = ("3F", "01")
    BOADRATE_38400 = ("2F", "01")
    BOADRATE_57600 = ("1F", "01")
    BOADRATE_115200 = ("0F", "01")

    def __init__(self, board_rate):
        self.id_number = "AA07"
        self.param_1 = board_rate[0]
        self.param_2 = board_rate[1]
        self.param_3 = "00"
        self.param_4 = "00"


class ResetCommand(Command):
    RESET_TYPE_WHOLE_SYSTEM = "00"
    RESET_TYPE_STATE_MACHINES = "01"

    def __init__(self, reset_type):
        self.id_number = "AA08"
        self.param_1 = reset_type
        self.param_2 = "00"
        self.param_3 = "00"
        self.param_4 = "00"


class PowerOffCommand(Command):
    def __init__(self):
        self.id = "AA09"
        self.param_1 = "00"
        self.param_2 = "00"
        self.param_3 = "00"
        self.param_4 = "00"


class DataCommand(Command):
    DATA_TYPE_SNAPSHOT_PICTURE = "01"
    DATA_TYPE_PREVIEW_PICTURE = "02"
    DATA_TYPE_JPEG_PREVIEW_PICTURE = "05"

    def __init__(self, data_type, length_byte_0, length_byte_1, length_byte_2):
        self.id_number = "AA0A"
        self.param_1 = data_type
        self.param_2 = length_byte_0
        self.param_3 = length_byte_1
        self.param_4 = length_byte_2


class SyncCommand(Command):
    def __init__(self):
        self.id_number = "AA0D"
        self.param_1 = "00"
        self.param_2 = "00"
        self.param_3 = "00"
        self.param_4 = "00"


class AckCommand(Command):
    def __init__(self, command_id, package_id_byte_0, package_id_byte_1):
        self.id_number = "AA0E"
        self.param_1 = command_id
        self.param_2 = "00"
        self.param_3 = package_id_byte_0
        self.param_4 = package_id_byte_1


class NackCommand(Command):
    def __init__(self, error_number):
        self.id_number = "AA0F"
        self.param_1 = "00"
        self.param_2 = "00"
        self.param_3 = error_number
        self.param_4 = "00"
