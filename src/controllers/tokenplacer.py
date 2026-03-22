from src.controllers.finance import Bank
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.warden import Warden
from src.models.businesman import IdBusinessman
from src.models.gameboard import Ownership
from src.models.typescell import ChanceResultTypes


class TokenPlacer:

    __manager_ownership: ManagerOwnership
    __bank: Bank
    __warden = Warden

    def __init__(self, manager_ownership: ManagerOwnership, bank: Bank, warden: Warden):

        if not isinstance(manager_ownership, ManagerOwnership):  raise TypeError("Тип данных не ManagerOwnership")

        self.__manager_ownership = manager_ownership
        self.__bank = bank
        self.__warden = Warden

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

    def put_on_chance(self, money: int, result: ChanceResultTypes, id: IdBusinessman,) -> None:

        if not isinstance(money, int):  raise TypeError("Тип данных не int")
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        if result == ChanceResultTypes.POSITIVE:
            self.__bank.charge_account(money, id)

        elif result == ChanceResultTypes.NEGATIVE:
            self.__bank.debit_account(money, id)

    def put_on_jail(self, id: IdBusinessman) -> None:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__warden.arrest(id)








