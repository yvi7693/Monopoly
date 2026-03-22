from src.models.gameboard import Jail
from src.models.idbusinessman import IdBusinessman


class Warden:

    __jail: Jail

    def __init__(self, jail: Jail):

        self.__jail = jail

    def arrest(self, id: IdBusinessman) -> None:
        self.__jail.conclude(id)

    def release(self, id: IdBusinessman) -> None:
        self.__jail.give_freedom(id)
