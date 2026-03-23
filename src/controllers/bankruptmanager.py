from src.controllers.playermanager import PlayerManager
from src.models.businesman import Businessman


class BankruptManager:

    __player_manager: PlayerManager

    def __init__(self, player_manager: PlayerManager):
        self.__player_manager = player_manager

    def identify_bankrupt(self, businessman: Businessman) -> None:

        count_ownerships = len(businessman.ownerships)

        if count_ownerships == 0:

            self.__player_manager.exclude_businessman(businessman)