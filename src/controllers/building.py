from src.controllers.playermanager import PlayerManager
from src.models.gameboard import Street
from src.models.building import BuildingRatioTypes, BuildingTypes
from src.controllers.finance import Bank
from src.models.idbusinessman import IdBusinessman


class Builder:

    HOME_PRICE = 100
    HOTEL_PRICE = 150

    def __init__(self, bank: Bank, player_manager: PlayerManager):
        self.__bank = bank
        self.__player_manager = player_manager

    def try_build(self, id: IdBusinessman, street: Street, type: BuildingTypes) -> bool:
        if type == BuildingTypes.HOME and self.__try_build_home(id, street):

            return True

        elif type == BuildingTypes.HOTEL and self.__try_build_hotel(id, street):

            return True

        return False

    def __try_build_hotel(self, id: IdBusinessman, street: Street) -> bool:

        if not street.identify_owner(id): return False

        if not street.can_build_hotel(): return False

        if not self.__bank.has_enough_money(street.neighborhood.build_price, id): return False

        self.__bank.try_debit_account(street.neighborhood.build_price, id)

        street.create_build(street.neighborhood.build_price, BuildingTypes.HOTEL, BuildingRatioTypes.HOTEL)

        return True


    def __try_build_home(self, id: IdBusinessman, street: Street) -> bool:

        if not street.identify_owner(id): return False

        if not street.can_build_home(): return False

        if not self.__bank.has_enough_money(street.neighborhood.build_price, id): return False

        self.__bank.try_debit_account(street.neighborhood.build_price, id)

        street.create_build(street.neighborhood.build_price, BuildingTypes.HOME, BuildingRatioTypes.HOME)

        return True
