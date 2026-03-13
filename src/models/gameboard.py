from __future__ import annotations
from abc import ABC, abstractmethod
from businesman import Businessman

class Cell(ABC):

    _x: int

    def __init__(self, x: int):

        if not isinstance(x, int): raise TypeError()

        self._x = x

    @abstractmethod
    def land(self, businessman: Businessman): raise NotImplemented()

class ChanceResultTypes:

    POSITIVE = 1
    NEGATIVE = -1


class Chance(Cell):

    CASH = 30

    def __init__(self, x: int):

        super().__init__(x)

    def land(self, businessman: Businessman):
        self.__try_luck(businessman)

    def __try_luck(self, businessman: Businessman):  # испытать удачу

        result = self.__solve_chance()

        if result == ChanceResultTypes.POSITIVE:
            self.__execute_positive_chance(businessman)
        else:
            self.__execute_negative_chance(businessman)

    def __execute_positive_chance(self, businessman):  # выполнить позитивный исход
        businessman.increase_balance(Chance.CASH)

    def __execute_negative_chance(self, businessman):  # выполнить негативный исход
        businessman.decrease_balance(Chance.CASH)

    def __solve_chance(self) -> int:  # вычислить шанс
        import random

        if random.randint(0, 10) > 5:
            return ChanceResultTypes.POSITIVE
        else:
            return ChanceResultTypes.NEGATIVE


class Ownership(Cell, ABC):
    # Модель Собственности

    _name: str
    _owner: Businessman
    _price: int

    def __init__(self, x: int, price: int, rent: int):
        super().__init__(x)

        if not isinstance(price, int):  raise  TypeError()
        if not isinstance(rent, int):  raise TypeError()

        self._owner = None
        self._price = price
        self._rent = rent

    @abstractmethod
    def calculate_price(self) -> int:  raise NotImplemented()

    @abstractmethod
    def calculate_rent(self) -> int:  raise NotImplemented()

    def get_price(self) -> int:  return self._price

    def set_owner(self, owner: Businessman) -> None:

        if not isinstance(owner, Businessman): raise TypeError()

        self._owner = owner

    def has_owner(self) -> bool:
        return not self._owner is None

    def identify_owner(self, owner: Businessman) -> bool:
        return self._owner == owner

    def unset_owner(self) -> None:
        self._owner = None


class NeighborhoodTypes:
    RED = 0
    BLUE = 1
    GREEN = 2


class Street(Ownership):

    def __init__(self, x: int, price: int, rent: int, neighborhood: NeighborhoodTypes):
        super().__init__(x, price, rent)

        self.__neighborhood =  neighborhood  # район
        self.__builds = []

    def __eq__(self, other: Street):
        return self._name == other._name

    def get_neighborhood(self) -> NeighborhoodTypes: return self.__neighborhood

    def land(self, businessman: Businessman):  # встать
        pass

    def calculate_price(self) -> int:
        price_buildings = 0

        for build in self.__builds:
            price_buildings += build.get_price()

        return self._price + price_buildings

    def calculate_rent(self) -> int:
        build_ratio = 0

        for build in self.__builds:
            build_ratio += build.get_ratio()

        return  self._rent * build_ratio

    def build_home(self, home: Building) -> None:  # построить дом
        if not isinstance(home, Building):  raise TypeError()
        if home.get_ratio() != BuildingRatioTypes.HOME:  raise ValueError()

        self.__builds.append(home)

    def build_hotel(self, hotel: Building) -> None:  # построить отель
        if not isinstance(hotel, Building):  raise TypeError()
        if hotel.get_ratio() != BuildingRatioTypes.HOTEL:  raise ValueError()

        self.__builds.append(hotel)

    def can_build_home(self) -> bool: # можно ли построить дом
        if len(self.__builds) < 4: return True

        return False

    def can_build_hotel(self) -> bool: # можно ли построить отель
        if len(self.__builds) == 4 : return True

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

    def get_price(self):
        return self.__price

    def get_ratio(self):
        return self.__ratio

    def get_full_price(self):
        return self.__price * self.__ratio



