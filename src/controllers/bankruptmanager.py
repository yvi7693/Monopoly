from src.controllers.playermanager import PlayerManager
from src.models.businesman import Businessman
from src.models.idbusinessman import IdBusinessman


class BankruptManager:

    __player_manager: PlayerManager
    __bankrupts: list[IdBusinessman]

    def __init__(self, player_manager: PlayerManager):
        self.__player_manager = player_manager
        self.__bankrupts = []

    def bankrupting(self, id: IdBusinessman) -> None:
        if id in self.__bankrupts: return None

        self.__bankrupts.append(id)
        self.__player_manager.exclude_businessman(id)

        return None

    def is_bankrupt(self, id: IdBusinessman) -> bool:
        return id in self.__bankrupts