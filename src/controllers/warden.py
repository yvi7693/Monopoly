from src.models.gameboard import Jail
from src.models.idbusinessman import IdBusinessman


class Warden:

    def __init__(self, jail: Jail = None):
        self.__jail = jail

    def set_jail(self, jail: Jail) -> None:
        self.__jail = jail

    def arrest(self, id: IdBusinessman) -> None:
        if self.__jail.is_concluded(id):
            return None

        self.__jail.conclude(id)

        return None

    def release(self, id: IdBusinessman) -> None:
        self.__jail.give_freedom(id)

    def is_conclude(self, id: IdBusinessman) -> bool:
        return self.__jail.is_concluded(id)

