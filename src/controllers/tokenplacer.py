from src.controllers.finance import Bank
from src.controllers.purchasesale import ManagerOwnership
from src.models.businesman import IdBusinessman
from src.models.gameboard import Ownership


class TokenPlacer:

    __manager_ownership: ManagerOwnership
    __bank: Bank

    def __init__(self, manager_ownership: ManagerOwnership, bank: Bank):

        if not isinstance(manager_ownership, ManagerOwnership):  raise TypeError("Тип данных не ManagerOwnership")

        self.__manager_ownership = manager_ownership
        self.__bank = bank

    def put_on_ownership(self, ownership: Ownership, id: IdBusinessman) -> None:
        if self.__manager_ownership.try_buy_ownership(ownership, id):
            return None

        else:

            if not ownership.identify_owner(id):
                if self.__manager_ownership.try_charge_rent(ownership, id):
                    return None

                else:
                    return None

            else:
                return None

    def put_on_positive_chance(self, money: int, id: IdBusinessman) -> None:

        if not isinstance(money, int):  raise TypeError("Тип данных не int")
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__bank.charge_account(money, id)

    def put_on_negative_chance(self, money: int, id: IdBusinessman) -> None:

        if not isinstance(money, int):  raise TypeError("Тип данных не int")
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__bank.debit_account(money, id)






