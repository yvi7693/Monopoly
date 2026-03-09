from abc import ABC, abstractmethod

class Cell(ABC):

    _x: int
    _current_businessman: Businessman

    def __init__(self, x: int):

        if not isinstance(x, int): raise TypeError()

        self._x = x
        self._current_businessman = None

    @abstractmethod
    def land(self): raise NotImplemented()


class Ownership(Cell, ABC):
    # Модель Собственности

    _owner: Businessman
    _price: float

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

    def set_owner(self, owner: Businessman) -> None:
        pass

    def has_owner(self) -> bool:
        pass

    def identify_owner(self, owner: Businessman) -> bool:
        pass

    def unset_owner(self) -> None:
        pass


class NeighborhoodTypes:
    RED = 0
    BLUE = 1
    GREEN = 2


class Street(Ownership):

    def __init__(self, x: int, price: int, rent: int, neighborhood: NeighborhoodTypes):
        super().__init__(x, price, rent)

        self.__neighborhood =  neighborhood  # район

    def calculate_price(self) -> int:
        pass

    def calculate_rent(self) -> int:
        pass

    def land(self):  # встать
        pass

    def build_home(self) -> None:  # построить дом
        pass

    def build_hotel(self) -> None:  # построить отель
        pass

    def can_build_hotel(self) -> bool: # можно ли построить отель
        pass

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



