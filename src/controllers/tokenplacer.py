from src.controllers.playermanager import BankruptManager
from src.controllers.finance import Bank
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.warden import Warden
from src.models.businesman import IdBusinessman
from src.models.gameboard import Ownership, Jail
from src.models.typescell import ChanceResultTypes


class TokenPlacer:

    __manager_ownership: ManagerOwnership
    __bank: Bank
    __warden = Warden
    __bankrupt_manager: BankruptManager

    def __init__(self, manager_ownership: ManagerOwnership, bank: Bank, warden: Warden, bankrupt_manager: BankruptManager):

        if not isinstance(manager_ownership, ManagerOwnership):  raise TypeError("Тип данных не ManagerOwnership")
        if not isinstance(bank, Bank):  raise TypeError("Тип данных не Bank")
        if not isinstance(bankrupt_manager, BankruptManager):  raise TypeError("Тип данных не BankruptManager")

        self.__manager_ownership = manager_ownership
        self.__bank = bank
        self.__warden = warden
        self.__bankrupt_manager = bankrupt_manager

    def put_on_ownership(self, ownership: Ownership, id: IdBusinessman, buying_permission: bool) -> None:

        if not ownership.has_owner():
            if buying_permission:

                if self.__manager_ownership.try_buy_ownership(ownership,id):
                    return None

                else:
                    self.__bankrupt_manager.bankrupting(id)
            else:
                return None

        elif not ownership.identify_owner(id):

            if self.__manager_ownership.try_charge_rent(ownership,id):
                return None

            else:
                self.__bankrupt_manager.bankrupting(id)

        return None

    def put_on_chance(self, money: int, result: ChanceResultTypes, id: IdBusinessman) -> None:

        if not isinstance(money, int):  raise TypeError("Тип данных не int")
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        if result == ChanceResultTypes.POSITIVE:
            self.__bank.charge_account(money, id)

        elif result == ChanceResultTypes.NEGATIVE:
            if not self.__bank.try_debit_account(money, id):

                self.__bankrupt_manager.bankrupting(id)

    def put_on_jail(self, id: IdBusinessman, jail: Jail) -> None:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__warden.arrest(id, jail)








