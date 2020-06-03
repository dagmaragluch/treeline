from treeline.glengine.engine import Engine
from treeline.engine.camera import Camera
from treeline.model.board import Board
from treeline.model.player import Player
from treeline.model.resource import Resources
from treeline.model.game import Game
from treeline.interface.interface import Interface
import cProfile

if __name__ == '__main__':
    engine = Engine()
    camera = Camera((0, 0), fov=16)
    engine.set_camera(camera)
    engine.register_for_keys(camera)

    board = Board("./resources/maps/map1.csv")
    players = [Player(), Player()]
    game = Game(board, players)
    interface = Interface(game)

    for widget in interface.widgets:
        engine.add_widget(widget)
    for actor in game.get_all_actors():
        engine.add_actor(actor)

    # engine.start()
    cProfile.run("engine.start()", sort="cumtime")