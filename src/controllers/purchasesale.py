from src.models.gameboard import Ownership
from src.models.businesman import Businessman

class ManagerOwnership:

    def try_buy_ownership(self, ownership: Ownership, businessman: Businessman) -> bool: # попытка купить собственность

        if ownership.has_owner():  return False

        price = ownership.get_price()

        if not businessman.check_balance(price): return False

        businessman.decrease_balance(price)

        businessman.add_ownership(ownership)

        ownership.set_owner(businessman)

        return True

    def try_sell_ownership(self, ownership: Ownership, businessman: Businessman):

        if not businessman.has_tittle_deeds(ownership): return False

        price = ownership.calculate_price()

        businessman.delete_ownership(ownership)

        businessman.increase_balance(price)

        ownership.unset_owner()

        return True
