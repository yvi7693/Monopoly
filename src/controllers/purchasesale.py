from src.controllers.finance import Bank
from src.models.gameboard import Ownership
from src.models.businesman import Businessman

class ManagerOwnership:

    def __init__(self, bank: Bank):
        if not isinstance(bank, Bank):  raise TypeError()

        self.__bank = bank

    def try_buy_ownership(self, ownership: Ownership, businessman: Businessman) -> bool: # попытка купить собственность

        if ownership.has_owner():  return False

        price = ownership.get_price()

        if not self.__bank.has_enough_money(price, businessman.id): return False

        self.__bank.debit_account(price, businessman.id)

        businessman.add_ownership(ownership)

        ownership.set_owner(businessman.id)

        return True

    def try_sell_ownership(self, ownership: Ownership, businessman: Businessman):

        if not businessman.has_title_deeds(ownership): return False

        price = ownership.calculate_price()

        businessman.delete_ownership(ownership)

        self.__bank.charge_account(price, businessman.id)

        ownership.unset_owner()

        return True
