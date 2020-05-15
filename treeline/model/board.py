import numpy as np
import logging
import random
from typing import (
    List,
)
from numpy import genfromtxt
from treeline.model.terrain import Terrain
from treeline.model.field import Field

LOGGER = logging.getLogger(__name__)


class Board:
    """
    height = number of fields vertically
    width = number of fields horizontally
    because we use array of hexes:
        number of columns in array = 2 * width (!)
        number of rows in array = height
    """

    def __init__(self, file: str):
        self.board = self._create_board(self.get_data(file))
        self.width = self.board.shape[1]
        self.height = self.board.shape[0]

    def _create_board(self, map_in_array: np.ndarray) -> np.ndarray:
        rows = map_in_array.shape[0]
        columns = 2 * map_in_array.shape[1]
        shape = (rows, columns)
        board = np.empty(shape, dtype=object)

        for x in range(0, rows):
            for y in range(0, columns):
                if (x + y) % 2 == 0:
                    board[x][y] = Field(
                        position=(x, y),
                        terrain=Terrain(map_in_array[x][y // 2])
                    )

        return board

    def get_neighbours(self, field: Field) -> List[Field]:
        list_of_neighbours = []
        x = field.position[0]
        y = field.position[1]
        board_width = self.board.shape[1]
        board_height = self.board.shape[0]

        if (y + 2) < board_width:
            list_of_neighbours.append(self.board[x][y + 2])
        if (x + 1) < board_width and (y - 1) >= 0:
            list_of_neighbours.append(self.board[x + 1][y - 1])
        if (x - 1) >= 0 and (y - 1) >= 0:
            list_of_neighbours.append(self.board[x - 1][y - 1])
        if (y - 2) >= 0:
            list_of_neighbours.append(self.board[x][y - 2])
        if (x - 1) >= 0 and (y + 1) < board_height:
            list_of_neighbours.append(self.board[x - 1][y + 1])
        if (x + 1) < board_width and (y + 1) < board_height:
            list_of_neighbours.append(self.board[x + 1][y + 1])

        LOGGER.info("Found %d neighbours for (%d, %d) field)", len(list_of_neighbours), x, y)
        return list_of_neighbours

    def get_all_fields(self) -> List[Field]:
        for x in range(0, self.height):
            for y in range(0, self.width):
                if (x + y) % 2 == 0:
                    yield self.board[x][y]

    @staticmethod
    def get_data(file_name: str) -> np.ndarray:
        my_data = genfromtxt(file_name, delimiter=',')
        return my_data

    def get_field(self, x: int, y: int) -> Field:
        if 0 < x < self.height and 0 < y < self.width:
            return self.board[x][y]
        else:
            raise IndexError

    def get_random_field(self) -> Field:
        x = 0
        y = 1
        while (x + y) % 2 != 0:
            x = random.randrange(0, self.height)
            y = random.randrange(0, self.width)
        return self.get_field(x, y)

# b = Board("C:\\Users\\gluch\\Desktop\\python zawada\\treeline\\resources\\maps\\map1.csv")
# for f in b.get_all_fields():
#     print(f.__dict__)
# b.get_random_field()
