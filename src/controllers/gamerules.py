from src.controllers.finance import Bank
from src.controllers.tokenplacer import TokenPlacer
from src.models.businesman import Businessman
from src.models.gameboard import Board, Street, Chance, Cell, Jail, Station
from src.models.typescell import CurrentStatusOwner


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

    def move_token(self, points: int, businessman: Businessman) -> None:

        position = businessman.get_position()

        new_position = (position + points) % Board.END

        businessman.set_position(new_position)

        if Board.is_passed_go(position, points):
            self.__give_bonus_go(businessman)

    def processing_move(self, businessman: Businessman,  buying_permission: bool | None):

        new_position = businessman.get_position()

        cell = self.__board.get_cell(new_position)

        self.__processing_cell(cell, businessman, buying_permission)

    def __processing_cell(self, cell: Cell, businessman: Businessman, buying_permission: bool | None) -> None:

        if isinstance(cell, Street):
            self.__token_placer.put_on_ownership(cell, businessman.id, buying_permission)

        elif isinstance(cell, Station):
            self.__token_placer.put_on_ownership(cell, businessman.id, buying_permission)

        elif isinstance(cell, Chance):
            self.__token_placer.put_on_chance(Chance.CASH, cell.try_luck(), businessman.id)

        elif isinstance(cell, Jail):
            self.__token_placer.put_on_jail(businessman.id, cell)

    def __give_bonus_go(self, businessman: Businessman) -> None:
        if not isinstance(businessman, Businessman):  raise TypeError("Тип данных не Businessman")

        self.__bank.charge_account(Bank.BONUS_GO, businessman.id)