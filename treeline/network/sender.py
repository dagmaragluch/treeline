import logging
import socket

from treeline.model.field import Field

LOGGER = logging.getLogger(__name__)


class Sender:
    def __init__(self, receiver_address, receiver_socket):
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.connect((receiver_address, receiver_socket))

    def send_take(self, field: Field):
        x, y = field.position
        msg = "TAKE {} {}".format(x, y)
        self.send(msg)

    def send_build(self, building_type: str, field: Field):
        x, y = field.position
        msg = "BUILD {} {} {}".format(x, y, building_type)
        self.send(msg)

    def send_add_worker(self, field: Field):
        x, y = field.position
        msg = "ADD {} {}".format(x, y)
        self.send(msg)

    def send_remove_worker(self, field: Field):
        x, y = field.position
        msg = "REMOVE {} {}".format(x, y)
        self.send(msg)

    def send_start(self, field: Field, player_number: int):
        x, y = field.position
        msg = "START {} {} {}".format(x, y, player_number)
        self.send(msg)

    def send_end_turn(self):
        msg = "END"
        self.send(msg)

    def send_game_over(self):
        msg = "OVER"
        self.send(msg)

    def send_ready(self):
        msg = "READY"
        self.send(msg)

    def send_syncworkers(self, total_workers: int, available_workers: int):
        msg = "SYNCWORKERS {} {}".format(total_workers, available_workers)
        self.send(msg)

    def send(self, msg: str):
        LOGGER.debug("Sent %s", msg)
        msg = msg+";"
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def close(self):
        self.sender.close()
