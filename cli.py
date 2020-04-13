import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from ucam100 import Client
from ucam100.command import *


def main():
    client = Client(port="/dev/ttyACM0")
    # client.send_command(SyncCommand())

    # logger.debug(f"client.sp : {client.sp}")
    # logger.debug(f"command : {SyncCommand()}")
    client.connect()


if __name__ == "__main__":
    main()
