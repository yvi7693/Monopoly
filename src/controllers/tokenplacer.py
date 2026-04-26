from __future__ import annotations

import dataclasses
from enum import Enum

from src.controllers.playermanager import BankruptManager, PlayerManager
from src.controllers.finance import Bank
from src.controllers.purchasesale import ManagerOwnership
from src.controllers.warden import Warden
from src.models.businesman import IdBusinessman
from src.models.gameboard import Ownership, Chance
from src.models.typescell import ChanceResultTypes


class TokenPlacer:

    __manager_ownership: ManagerOwnership
    __bank: Bank
    __warden = Warden
    __bankrupt_manager: BankruptManager
    __player_manager: PlayerManager
    __status: TokenPlacerStatus | None

    def __init__(self, manager_ownership: ManagerOwnership, bank: Bank, warden: Warden, bankrupt_manager: BankruptManager, player_manager: PlayerManager):

        if not isinstance(manager_ownership, ManagerOwnership):  raise TypeError("Тип данных не ManagerOwnership")
        if not isinstance(bank, Bank):  raise TypeError("Тип данных не Bank")
        if not isinstance(bankrupt_manager, BankruptManager):  raise TypeError("Тип данных не BankruptManager")

        self.__manager_ownership = manager_ownership
        self.__bank = bank
        self.__warden = warden
        self.__bankrupt_manager = bankrupt_manager
        self.__player_manager = player_manager

        self.__status = None

    def get_status(self) -> TokenPlacerStatus:
        return self.__status

    def put_on_ownership(self, ownership: Ownership, id: IdBusinessman, buying_permission: bool) -> None:

        if not ownership.has_owner():
            if buying_permission and self.__manager_ownership.try_buy_ownership(ownership,id):
                self.__status = TokenPlacerStatus.BUY
                return None

            else:
                self.__status = TokenPlacerStatus.NO_MONEY
                return None

        elif not ownership.identify_owner(id):

            if self.__manager_ownership.try_charge_rent(ownership,id):
                self.__status = TokenPlacerStatus.RENT

            elif self.__player_manager.has_ownerships(id):
                self.__status = TokenPlacerStatus.NEED_SELL

            else:
                self.__status = TokenPlacerStatus.NEED_SELL
                self.__bankrupt_manager.bankrupting(id)

        return None

    def put_on_chance(self, money: int, chance: Chance, id: IdBusinessman) -> None:

        if not isinstance(money, int):  raise TypeError("Тип данных не int")
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        chance.try_luck()

        result = chance.get_result()

        self.__status = TokenPlacerStatus.CHANCE

        if result == ChanceResultTypes.POSITIVE:
            self.__bank.charge_account(money, id)

        elif result == ChanceResultTypes.NEGATIVE:

            if not self.__bank.try_debit_account(money, id):
                self.__bankrupt_manager.bankrupting(id)

    def put_on_jail(self, id: IdBusinessman) -> None:

        self.__status = TokenPlacerStatus.JAIL

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        self.__warden.arrest(id)


    def put_on_free_parking(self) -> None:

        self.__status = TokenPlacerStatus.PARKING

        return None


@dataclasses.dataclass
class TokenPlacerStatus(Enum):

    BUY = 0
    NO_MONEY = 1
    RENT = 2
    NEED_SELL = 3
    BANKRUPT = 4
    CHANCE = 5
    JAIL = 6
    PARKING = 7







