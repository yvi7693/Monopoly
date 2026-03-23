from src.controllers.bankruptmanager import BankruptManager
from src.controllers.gamerules import GameRules
from src.controllers.playermanager import PlayerManager
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.building import Builder
from src.controllers.finance import Bank
from src.controllers.tokenplacer import TokenPlacer
from src.controllers.warden import Warden

from src.models.dice import Dice
from src.models.gameboard import Board, Jail


class Game:

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

    def set_up(self, count_businessmen: int):
        self.__player_manager.add_businessmen(count_businessmen)

        self.__game_board.create_neighborhood()
        self.__game_board.create_cells()

    def mainloop(self):

        is_play = True

        while is_play:

            businessmen = self.__player_manager.get_businessmen()

            for i in range(0, len(businessmen)):

                points = self.__dice.throw()

                self.__game_rules.make_move(businessmen[i], points)

                self.__bankrupt_manager.identify_bankrupt(businessmen[i])

            if len(businessmen) == 1:

                is_play = False