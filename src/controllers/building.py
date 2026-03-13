from src.models.businesman import Businessman
from src.models.gameboard import Street, BuildingRatioTypes
from src.controllers.finance import Bank


class Builder:

    HOME_PRICE = 100
    HOTEL_PRICE = 150

    def __init__(self, bank: Bank):
        self.__bank = bank

    def try_build_hotel(self, businessman: Businessman, street: Street):

        if not street.identify_owner(businessman.id): return False

        if not businessman.has_neighborhood_by_street(street.get_neighborhood()): return False

        if not street.can_build_hotel(): return False

        if not self.__bank.has_enough_money(Builder.HOTEL_PRICE, businessman.id): return False

        self.__bank.debit_account(Builder.HOTEL_PRICE, businessman.id)

        street.create_build(Builder.HOTEL_PRICE, BuildingRatioTypes.HOTEL)

        return True


    def try_build_home(self, businessman: Businessman, street: Street):

        if not street.identify_owner(businessman.id): return False

        if not businessman.has_neighborhood_by_street(street.get_neighborhood()): return False

        if not street.can_build_home(): return False

        if not self.__bank.has_enough_money(Builder.HOME_PRICE): return False

        self.__bank.debit_account(Builder.HOME_PRICE)

        street.create_build(Builder.HOME_PRICE, BuildingRatioTypes.HOME)

        return True
