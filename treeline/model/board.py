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
        self._board = self._create_board(self.get_data(file))
        self.width = self._board.shape[1]
        self.height = self._board.shape[0]
        self.fields = self.get_all_fields()

    def _create_board(self, map_in_array: np.ndarray) -> np.ndarray:
        rows = map_in_array.shape[0]
        columns = 2 * map_in_array.shape[1]
        shape = (rows, columns)
        board = np.empty(shape, dtype=object)

        for x in range(0, rows):
            for y in range(0, columns):
                if (x + y) % 2 == 0:
                    if map_in_array[x][y // 2] != 0:  # if field is not "water"
                        board[x][y] = Field(
                            position=(x, y),
                            terrain=Terrain(map_in_array[x][y // 2])
                        )

        return board

    def get_neighbours(self, field: Field) -> List[Field]:
        list_of_neighbours = []
        x = field.position[0]
        y = field.position[1]

        if (y + 2) < self.width:
            list_of_neighbours.append(self._board[x][y + 2])
        if (x + 1) < self.height and (y - 1) >= 0:
            list_of_neighbours.append(self._board[x + 1][y - 1])
        if (x - 1) >= 0 and (y - 1) >= 0:
            list_of_neighbours.append(self._board[x - 1][y - 1])
        if (y - 2) >= 0:
            list_of_neighbours.append(self._board[x][y - 2])
        if (x - 1) >= 0 and (y + 1) < self.width:
            list_of_neighbours.append(self._board[x - 1][y + 1])
        if (x + 1) < self.height and (y + 1) < self.width:
            list_of_neighbours.append(self._board[x + 1][y + 1])

        for n in list_of_neighbours:
            if n is None:
                list_of_neighbours.remove(n)

        LOGGER.info("Found %d neighbours for (%d, %d) field)", len(list_of_neighbours), x, y)
        return list_of_neighbours

    def get_all_fields(self) -> List[Field]:
        for x in range(0, self.height):
            for y in range(0, self.width):
                if (x + y) % 2 == 0:
                    if self._board[x][y] is not None:
                        yield self._board[x][y]

    @staticmethod
    def get_data(file_name: str) -> np.ndarray:
        my_data = genfromtxt(file_name, delimiter=',')
        return my_data

    def get_field(self, x: int, y: int) -> Field:
        return self._board[x][y]

    def get_random_field(self) -> Field:
        x = 0
        y = 1
        while (x + y) % 2 != 0 or self.get_field(x, y) is None:
            x = random.randrange(0, self.height)
            y = random.randrange(0, self.width)
        return self.get_field(x, y)


# b = Board("C:\\Users\\gluch\\Desktop\\python zawada\\treeline\\resources\\maps\\map3.csv")
# # for f in b.get_all_fields():
# #     print(f.__dict__)
# print(b.get_random_field().terrain)
