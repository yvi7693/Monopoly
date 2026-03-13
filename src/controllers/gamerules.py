from src.controllers.finance import Bank
from src.models.businesman import Businessman
from src.models.dice import Dice
from src.models.gameboard import Board, Cell

class GameRules:

    board: Board
    dice: Dice

    def __init__(self, board: Board, bank: Bank, dice: Dice):
        if not isinstance(board, Board):  raise TypeError()
        if not isinstance(bank, Bank):  raise TypeError()

        self.__board = board
        self.__dice = dice
        self.bank = bank

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
        if not isinstance(businessman, Businessman):  raise TypeError()

        self.bank.charge_account(Bank.BONUS_GO, businessman.id)