from enum import Enum


class BuildingRatioTypes:
    HOME = 2
    HOTEL = 9


class BuildingTypes(Enum):
    HOME = 0
    HOTEL = 1


class Building:

    # строение

    __price: int
    __type: BuildingTypes
    __ratio: int

    def __init__(self, price: int, type: BuildingTypes, ratio: int):
        if not isinstance(price, int):  raise TypeError("Тип данных не int")
        if not isinstance(type, BuildingTypes):  raise TypeError("Тип данных не int")
        if not isinstance(ratio, int):  raise TypeError("Тип данных не int")

        self.__price = price
        self.__type = type
        self.__ratio = ratio

    def get_price(self) -> int:
        return self.__price

    def get_type(self) -> BuildingTypes:
        return self.__type

    def get_ratio(self) -> int:
        return self.__ratio

    def get_full_price(self) -> int:
        return self.__price * self.__ratio