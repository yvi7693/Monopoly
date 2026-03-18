from multiprocessing.managers import Token

from src.controllers.finance import Bank
from src.controllers.tokenplacer import TokenPlacer
from src.models.businesman import Businessman
from src.models.gameboard import Board, CellTypes


class GameRules:

    __board: Board
    __bank: Bank
    __token_placer: TokenPlacer

    def __init__(self, board: Board, bank: Bank, token_placer: TokenPlacer):
        if not isinstance(board, Board):  raise TypeError("Тип данных не Board")
        if not isinstance(bank, Bank):  raise TypeError("Тип данных не Bank")
        if not isinstance(token_placer, TokenPlacer):  raise TypeError("Тип данных не TokenPlacer")

        self.__board = board
        self.__bank = bank
        self.__token_placer = token_placer

    def make_move(self, businessman: Businessman, points: int):

        self.__move_token(points, businessman)

        new_position = businessman.get_position()

        cell = self.__board.get_cell(new_position)

        cell.land(businessman.id)

    def __move_token(self, points: int, businessman: Businessman) -> None:

        position = businessman.get_position()

        new_position = (position + points) % Board.END

        businessman.set_position(new_position)

        if Board.is_passed_go(position, points):
            self.__give_bonus_go(businessman)

    def __give_bonus_go(self, businessman: Businessman) -> None:
        if not isinstance(businessman, Businessman):  raise TypeError("Тип данных не Businessman")

        self.__bank.charge_account(Bank.BONUS_GO, businessman.id)