from src.models.gameboard import Jail
from src.models.idbusinessman import IdBusinessman


class Warden:

    @staticmethod
    def arrest(id: IdBusinessman, jail: Jail) -> None:
        jail.conclude(id)

    @staticmethod
    def release(id: IdBusinessman, jail: Jail) -> None:
        jail.give_freedom(id)
