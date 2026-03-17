from src.models.businesman import Businessman
from src.models.gameboard import Street, BuildingRatioTypes, BuildingTypes
from src.controllers.finance import Bank


class Builder:

    HOME_PRICE = 100
    HOTEL_PRICE = 150

    def __init__(self, bank: Bank):
        self.__bank = bank

    def try_build(self,  businessman: Businessman, street: Street, type: BuildingTypes) -> bool:
        if type == BuildingTypes.HOME:
            self.__try_build_home(businessman, street)

            return True

        elif type == BuildingTypes.HOTEL:
            self.__try_build_hotel(businessman, street)

            return True

        return False


    def __try_build_hotel(self, businessman: Businessman, street: Street):

        if not street.identify_owner(businessman.id): return False

        if not businessman.has_neighborhood_by_street(street.neighborhood): return False

        if not street.can_build_hotel(): return False

        if not self.__bank.has_enough_money(street.neighborhood.build_price, businessman.id): return False

        self.__bank.debit_account(street.neighborhood.build_price, businessman.id)

        street.create_build(street.neighborhood.build_price, BuildingTypes.HOTEL, BuildingRatioTypes.HOTEL)

        return True


    def __try_build_home(self, businessman: Businessman, street: Street):

        if not street.identify_owner(businessman.id): return False

        if not businessman.has_neighborhood_by_street(street.neighborhood): return False

        if not street.can_build_home(): return False

        if not self.__bank.has_enough_money(street.neighborhood.build_price, businessman.id): return False

        self.__bank.debit_account(street.neighborhood.build_price, businessman.id)

        street.create_build(street.neighborhood.build_price, BuildingTypes.HOME, BuildingRatioTypes.HOME)

        return True
