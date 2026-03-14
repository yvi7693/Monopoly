from src.controllers.finance import Bank
from src.controllers.gamerules import GameRules
from src.controllers.playermanager import PlayerManager
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.building import Builder

from src.models.dice import Dice
from src.models.gameboard import Board



class Game:

    def __init__(self):
        self.__bank = Bank()
        self.__game_board = Board()

        self.__game_rules = GameRules(self.__game_board, self.__bank)
        self.player_manager = PlayerManager()
        self.__builder = Builder(self.__bank)
        self.__manager_ownership = ManagerOwnership(self.__bank)
        self.__dice = Dice()

    def set_up(self, count_businessmen: int):
        pass

    def mainloop(self):
        pass