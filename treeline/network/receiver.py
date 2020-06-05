import logging
import socket
import threading
from typing import List

LOGGER = logging.getLogger(__name__)


class Receiver(threading.Thread):
    def __init__(self, sender_address, sender_socket):
        threading.Thread.__init__(self)
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.receiver.bind((sender_address, sender_socket))
        self.receiver.listen(1)
        self.s_socket = None
        self.s_address = None
        self.callbacks = {}

    def run(self):
        sender_sock, sender_addr = self.receiver.accept()
        self.s_socket = sender_sock
        self.s_address = sender_addr
        while True:
            data = self.s_socket.recv(2048)
            msg = data.decode()
            if msg == 'OVER':
                break
            if msg == '':
                LOGGER.debug("Empty msg received")

            self.handle_message(msg)

    def handle_message(self, msg: str):
        words = msg.split("_")
        command = words[0]
        params = words[1:]
        params = self._parse_params(params)
        self.callbacks[command](*params)

    @staticmethod
    def _parse_params(params: List[str]):
        new_params = []
        for param in params:
            try:
                new_param = int(param)
                new_params.append(new_param)
            except ValueError:
                new_params.append(param)

        return new_params
