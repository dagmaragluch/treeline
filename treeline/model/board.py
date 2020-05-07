import numpy as np

from treeline.model.field import Field


class Hex:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x = x_coordinate
        self.y = y_coordinate


'''
height = number of fields vertically
width = number of fields horizontally
because we use array of hexes:
    number of columns in array = 2 * width (!)
    number of rows in array = height
'''


class Board:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = self.create_board(width, height)

    def create_board(self, width: int, height: int):
        rows = width
        columns = 2 * height
        shape = (rows, columns)
        board = np.empty(shape, dtype=object)

        for x in range(0, rows):
            for y in range(0, columns):
                if (x + y) % 2 == 0:
                    board[x][y] = Hex(x, y)

        return board

    def get_neighbours(self, hex: Hex):
        list_of_neighbours = []
        x = hex.x
        y = hex.y
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

        print(len(list_of_neighbours))
        return list_of_neighbours


# b = Board(6, 3)
# n1 = b.get_neighbours(b.board[4][2])
# print(n1)
