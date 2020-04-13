from ucam100.command import *
from ucam100.utils import command_from_hex
import serial
import select

import logging

logger = logging.getLogger(__name__)


class Client:
    cam_connected = False

    def __init__(self, port, baudrate=115200, bytesize=8, parity="N"):
        logger.debug("INIT")
        self.baudrate = baudrate
        self.sp = serial.Serial(
            port=port, baudrate=self.baudrate, bytesize=bytesize, parity=parity
        )

    def send_command(self, command: Command):
        command_bytes = bytes.fromhex(str(command))
        logger.debug(f"sending command : {command_bytes}")
        self.sp.write(command_bytes)

    def receive_command(self, wait=0.01):
        readable, _, _ = select.select([self.sp], [], [], wait)
        if len(readable) > 0:
            connection = readable[0]
            received = connection.read(6)
            received_hex = received.hex().upper()
            logger.debug(f"Received: {received_hex}")
            command = command_from_hex(received_hex)
            return command

        return None

    def receive_data(self):
        pass

        # while True:
        # self.sp.

    def connect(self):
        """
        Either the host or the CAM-VGA100 can issue this command to make
        connection. An ACK command must be sent out after receiving this
        command
        """
        command = SyncCommand()
        sync_counter = 0
        while sync_counter < 60:
            logger.debug(f"Sync counter: {sync_counter}")
            self.send_command(command)
            received_command = self.receive_command(wait=0.01)
            if received_command is not None:
                return received_command
            sync_counter += 1

        raise Exception("Sync ACK not received")

    def setup_cam(self, color_type, preview_res, jpeg_res):
        """
        The host issues this command to configure the preview image size and
        color type. After receiving this command, the module will send out an
        ACK command to the host if the configuration success. Otherwise, an
        NACK command will be sent out.
        """
        command = InitialCommand(
            color_type=color_type, preview_res=preview_res, jpeg_res=jpeg_res
        )
