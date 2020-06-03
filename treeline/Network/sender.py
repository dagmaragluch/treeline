import socket

from treeline.model.field import Field


class Sender:
    def __init__(self, receiver_address, receiver_socket):
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.connect((receiver_address, receiver_socket))

    def send_take(self, field: Field):
        x, y = field.position
        msg = "TAKE_{}_{}".format(x, y)
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def send_build(self, building_type: str, field: Field):
        x, y = field.position
        msg = "BUILD_{}_{}_{}".format(x, y, building_type)
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def send_add_worker(self, field: Field):
        x, y = field.position
        msg = "ADD_{}_{}".format(x, y)
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def send_remove_worker(self, field: Field):
        x, y = field.position
        msg = "REMOVE_{}_{}".format(x, y)
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def send_end_turn(self):
        msg = "END"
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def send_game_over(self):
        msg = "OVER"
        self.sender.sendall(bytes(msg, 'UTF-8'))

    def close(self):
        self.sender.close()
