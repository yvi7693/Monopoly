from src.controllers.finance import Bank
from src.controllers.playermanager import PlayerManager
from src.models.businesman import IdBusinessman
from src.models.gameboard import Ownership

class ManagerOwnership:

    def __init__(self, bank: Bank, player_manager: PlayerManager):
        if not isinstance(bank, Bank):  raise TypeError()

        self.__bank = bank
        self.__player_manager = player_manager

    def try_buy_ownership(self, ownership: Ownership, id: IdBusinessman) -> bool: # попытка купить собственность

        if ownership.has_owner():  return False

        price = ownership.calculate_price()

        if not self.__bank.has_enough_money(price, id): return False

        self.__bank.debit_account(price, id)

        self.__player_manager.add_ownership(ownership, id)

        ownership.set_owner(id)

        return True

    def try_sell_ownership(self, ownership: Ownership, id: IdBusinessman) -> bool:

        if not self.__player_manager.has_tittle_deeds(ownership, id): return False

        price = ownership.calculate_price()

        self.__player_manager.delete_ownership(ownership, id)

        self.__bank.charge_account(price, id)

        ownership.unset_owner()

        return True

    def try_charge_rent(self, ownership: Ownership, tenant: IdBusinessman) -> bool:
        rent = ownership.calculate_rent()

        if not self.__bank.has_enough_money(rent, tenant): return False

        self.__bank.debit_account(rent, tenant)

        owner = ownership.get_owner()

        self.__bank.charge_account(rent, owner)

        return True