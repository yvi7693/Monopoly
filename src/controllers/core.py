from src.controllers.bankruptmanager import BankruptManager
from src.controllers.gamerules import GameRules
from src.controllers.playermanager import PlayerManager
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.building import Builder
from src.controllers.finance import Bank
from src.controllers.tokenplacer import TokenPlacer
from src.controllers.warden import Warden
from src.models.businesman import Businessman

from src.models.dice import Dice
from src.models.gameboard import Board, Ownership, Cell
from src.models.typescell import CurrentStatusOwner, MessageManager


class Game:

    __current_player: Businessman | None
    __current_balance: int | None
    __current_points: tuple[int, int] | None

    def __init__(self):
        self.__bank = Bank()
        self.__game_board = Board()

        self.__warden = Warden()
        self.__player_manager = PlayerManager(self.__bank)
        self.__manager_ownership = ManagerOwnership(self.__bank, self.__player_manager)
        self.__token_placer = TokenPlacer(self.__manager_ownership, self.__bank, self.__warden)
        self.__game_rules = GameRules(self.__game_board, self.__bank, self.__token_placer)
        self.__builder = Builder(self.__bank)
        self.__bankrupt_manager = BankruptManager(self.__player_manager)
        self.__dice = Dice()
        self.__current_status_owner = CurrentStatusOwner()

        self.__current_player = None
        self.__current_balance = None
        self.__current_points = None
        self.__current_cell_name = None
        self.__current_cell = None

    def set_up(self, count_businessmen: int):
        self.__player_manager.add_businessmen(count_businessmen)

        self.__game_board.create_neighborhood()
        self.__game_board.create_cells()

    def make_move(self) -> None:
        self.__current_player = self.__player_manager.get_current_businessman()
        self.__current_points = self.__dice.throw()

        self.__game_rules.move_token(sum(self.__current_points), self.__current_player)

        self.__current_balance = self.__bank.get_balance(self.__current_player.id)
        self.__current_cell_name = self.__game_board.get_cell(self.__current_player.get_position()).get_name()
        self.__current_cell = self.__game_board.get_cell(self.__current_player.get_position())

    def processing_move(self, buying_permission: bool | None) -> None:
        self.__game_rules.processing_move(self.__current_player, buying_permission, self.__current_status_owner)

    def get_current_status_owner(self) -> CurrentStatusOwner:
        return self.__current_status_owner


    def get_current_player(self) -> Businessman:
        return self.__current_player

    def get_current_balance(self) -> int:
        return self.__current_balance

    def get_current_points(self) -> tuple[int, int]:
        return self.__current_points

    def get_current_cell(self) -> Cell:
        return self.__current_cell

    def __get_board(self) -> Board:
        return self.__game_board

    def __get_token_placer(self):
        return self.__token_placer

    board = property(__get_board)
    token_placer = property(__get_token_placer)