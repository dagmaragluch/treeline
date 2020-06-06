import logging
import socket
import time

from treeline.engine.engine import Engine
from treeline.engine.camera import Camera
from treeline.model.board import Board
from treeline.model.player import Player
from treeline.model.resource import Resources
from treeline.model.game import Game
from treeline.interface.interface import Interface
from treeline.network.receiver import Receiver
from treeline.network.sender import Sender

LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':

    addr = None
    your_port = None
    p2_port = None

    online = False
    receiver = None
    sender = None
    attempt = 0

    if online:
        addr = "127.0.0.1"
        your_port = int(input("Your port"))  # TODO: Fix popup window
        p2_port = int(input("Type second player's port"))
        receiver = Receiver(addr, your_port)
        receiver.start()

    while online:
        attempt += 1

        try:
            sender = Sender(addr, p2_port)
            break
        except ConnectionRefusedError:
            LOGGER.debug("Connection refused, trying again, wait {} seconds".format(attempt * 5))

        time.sleep(attempt * 5)

    engine = Engine()
    board = Board("./resources/maps/map2.csv")
    players = [Player(), Player()]
    game = Game(board, players, 0, sender, engine)

    if receiver is not None:
        game.add_receiver_callbacks(receiver)
        LOGGER.debug(receiver.callbacks)

    interface = Interface(game)

    for widget in interface.widgets:
        engine.add_widget(widget)
    for actor in game.get_all_actors():
        engine.add_actor(actor)

    engine.start()
