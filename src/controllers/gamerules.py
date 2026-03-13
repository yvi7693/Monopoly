from src.models.businesman import Businessman
from src.models.dice import Dice
from src.models.gameboard import Board, Cell

class GameRules:

    board: Board
    dice: Dice
    cells: list[Cell]

    def __init__(self, board: Board, cells: list[Cell] = None):
        if not isinstance(board, Board):  raise TypeError()
        if not isinstance(cells, list): raise TypeError()

        self.__board = board
        self.__dice = Dice()
        self.__cells = cells or []

    def make_move(self, businessman: Businessman):
        points = self.__dice.throw()

        self.__move_token(points, businessman)

        new_position = businessman.get_position()

        cell = self.board.get_cell(new_position)

        cell.land(businessman)

    def __move_token(self, points: int, businessman: Businessman) -> None:
        businessman.make_move(points)

        new_position = businessman.get_position()

        if self.board.is_passed_go(new_position):
            self.__passed_go(businessman)

    def __passed_go(self, businessman: Businessman) -> None:
        pass






