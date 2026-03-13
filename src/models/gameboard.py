from __future__ import annotations
from abc import ABC, abstractmethod
from operator import truediv

from businesman import IdBusinessman
from src.controllers.finance import Bank


class Board:

    START = 0
    END = 39

    __cells: list[Cell]

    def __init__(self, cells: list[Cell] = None):
        self.__cells = cells or []

    def get_cell(self, position) -> Cell: return self.__cells[position]

    @staticmethod
    def is_passed_go(position: int, points: int) -> bool:
        if (position + points) > 39: return True

        return False

class Cell(ABC):

    _x: int

    def __init__(self, x: int):

        if not isinstance(x, int): raise TypeError()

        self._x = x

    @abstractmethod
    def land(self, id: IdBusinessman): raise NotImplemented()

class ChanceResultTypes:

    POSITIVE = 1
    NEGATIVE = -1


class Chance(Cell):

    CASH = 30

    def __init__(self, x: int, bank: Bank):
        super().__init__(x)

        if not isinstance(bank, Bank):  raise TypeError()

        self.__bank = bank

    def land(self, id: IdBusinessman):
        self.__try_luck(id)

    def __try_luck(self, id: IdBusinessman):  # испытать удачу

        result = Chance.__solve_chance()

        if result == ChanceResultTypes.POSITIVE:
            self.__execute_positive_chance(id)
        else:
            self.__execute_negative_chance(id)

    def __execute_positive_chance(self, id: IdBusinessman):  # выполнить позитивный исход
        self.__bank.charge_account(Chance.CASH, id)

    def __execute_negative_chance(self, id: IdBusinessman):  # выполнить негативный исход
        self.__bank.charge_account(Chance.CASH, id)

    @staticmethod
    def __solve_chance() -> int:  # вычислить шанс
        import random

        if random.randint(0, 10) > 5:
            return ChanceResultTypes.POSITIVE
        else:
            return ChanceResultTypes.NEGATIVE


class Ownership(Cell, ABC):
    # Модель Собственности

    _name: str
    _owner: IdBusinessman
    _price: int
    _rent: int

    def __init__(self, name: str, x: int, price: int, rent: int):
        super().__init__(x)

        if not isinstance(price, int):  raise  TypeError("Тип данных не int")
        if not isinstance(rent, int):  raise TypeError("Тип данных не int")

        self._name = name
        self._owner = None
        self._price = price
        self._rent = rent

    @abstractmethod
    def calculate_price(self) -> int:  raise NotImplemented()

    @abstractmethod
    def calculate_rent(self) -> int:  raise NotImplemented()

    def get_price(self) -> int:  return self._price

    def set_owner(self, owner: IdBusinessman) -> None:

        if not isinstance(owner, IdBusinessman): raise TypeError("Тип данных не IdBusinessman")

        self._owner = owner

    def has_owner(self) -> bool:
        return not self._owner is None

    def identify_owner(self, owner: IdBusinessman) -> bool:
        return self._owner == owner

    def unset_owner(self) -> None:
        self._owner = None


class NeighborhoodTypes:
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    BROWN = 4

class Street(Ownership):

    HOME_MAX_COUNT = 4

    __neighborhood: NeighborhoodTypes
    __builds: list[Building]

    def __init__(self, x: int, price: int, rent: int, neighborhood: NeighborhoodTypes):
        super().__init__(x, price, rent)

        self.__neighborhood =  neighborhood  # район
        self.__builds = []

    def __eq__(self, other: Street):
        return self._name == other._name

    def get_neighborhood(self) -> NeighborhoodTypes:
        return self.__neighborhood

    def land(self, id: IdBusinessman):  # встать
        pass

    def calculate_price(self) -> int:
        price_buildings = 0

        for build in self.__builds:
            price_buildings += build.get_price()

        return self._price + price_buildings

    def calculate_rent(self) -> int:
        build_ratio = 1

        for build in self.__builds:
            build_ratio += build.get_ratio()

        return  self._rent * build_ratio

    def create_build(self, price: int, type: int) -> None:  # построить дом
        self.__builds.append(Building(price, type))

    def can_build_home(self) -> bool: # можно ли построить дом
        if len(self.__builds) < Street.HOME_MAX_COUNT: return True

        return False

    def can_build_hotel(self) -> bool: # можно ли построить отель
        if len(self.__builds) == Street.HOME_MAX_COUNT : return True

        return False


class BuildingRatioTypes:
    HOME = 2
    HOTEL = 9

class Building:  # строение

    def __init__(self, price: int, ratio: int):
        if not isinstance(price, int):  raise TypeError()
        if not isinstance(ratio, int):  raise TypeError()

        self.__price = price
        self.__ratio = ratio

    def get_price(self) -> int:
        return self.__price

    def get_ratio(self) -> int:
        return self.__ratio

    def get_full_price(self) -> int:
        return self.__price * self.__ratio