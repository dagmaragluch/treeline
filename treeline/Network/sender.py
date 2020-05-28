import socket


class Sender:
    def __init__(self, receiver_address, receiver_socket):
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender.connect((receiver_address, receiver_socket))

    def send_code(self, code):
        self.sender.sendall(bytes(code, 'UTF-8'))

    def close(self):
        self.sender.close()
