from src.controllers.finance import Bank
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.warden import Warden
from src.models.businesman import IdBusinessman
from src.models.gameboard import Ownership
from src.models.typescell import ChanceResultTypes, CurrentStatusOwner, StatusOwner, MessageManager, TypeMessage


class TokenPlacer:

    __manager_ownership: ManagerOwnership
    __bank: Bank
    __warden = Warden

    def __init__(self, manager_ownership: ManagerOwnership, bank: Bank, warden: Warden):

        if not isinstance(manager_ownership, ManagerOwnership):  raise TypeError("Тип данных не ManagerOwnership")

        self.__manager_ownership = manager_ownership
        self.__bank = bank
        self.__warden = warden
        self.__message_manager = MessageManager()

    def put_on_ownership(self, ownership: Ownership, id: IdBusinessman, buying_permission: bool, purchased: CurrentStatusOwner) -> None:

        self.__message_manager.set_type_message(TypeMessage.ASK)

        if not ownership.has_owner():
            if buying_permission:

                if self.__manager_ownership.try_buy_ownership(ownership,id):
                    purchased.set_status(StatusOwner.BOUGHT)

                else:
                    purchased.set_status(StatusOwner.NOT_MONEY)
            else:
                purchased.set_status(StatusOwner.NOT_WISH)

        elif not ownership.identify_owner(id):
            if self.__manager_ownership.try_charge_rent(ownership,id):
                purchased.set_status(StatusOwner.PAID_RENT)

            else:
                purchased.set_status(StatusOwner.NOT_MONEY)

        return None

    def put_on_chance(self, money: int, result: ChanceResultTypes, id: IdBusinessman,) -> None:

        if not isinstance(money, int):  raise TypeError("Тип данных не int")
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__message_manager.set_type_message(TypeMessage.INFO)

        if result == ChanceResultTypes.POSITIVE:
            self.__bank.charge_account(money, id)

        elif result == ChanceResultTypes.NEGATIVE:
            self.__bank.debit_account(money, id)

    def put_on_jail(self, id: IdBusinessman) -> None:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__message_manager.set_type_message(TypeMessage.INFO)

        self.__warden.arrest(id)








