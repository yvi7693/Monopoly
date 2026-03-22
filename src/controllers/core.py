from src.controllers.gamerules import GameRules
from src.controllers.playermanager import PlayerManager
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.building import Builder
from src.controllers.finance import Bank
from src.controllers.tokenplacer import TokenPlacer

from src.models.dice import Dice
from src.models.gameboard import Board



class Game:

    def __init__(self):
        self.__bank = Bank()
        self.__game_board = Board()

        self.__player_manager = PlayerManager(self.__bank)
        self.__manager_ownership = ManagerOwnership(self.__bank, self.__player_manager)
        self.__token_placer = TokenPlacer(self.__manager_ownership, self.__bank)
        self.__game_rules = GameRules(self.__game_board, self.__bank, self.__token_placer)
        self.__builder = Builder(self.__bank)
        self.__dice = Dice()

    def set_up(self, count_businessmen: int):
        self.__player_manager.try_add_businessmen(count_businessmen)

        # создание клеток
        ...


    def mainloop(self):
        pass