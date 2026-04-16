from __future__ import annotations
from abc import ABC, abstractmethod

from src.models.building import Building
from src.models.idbusinessman import IdBusinessman
from src.models.typescell import ChanceResultTypes, Neighborhood, NeighborhoodTypes


class Board:

    START = 0
    END = 39

    __cells: list[Cell]
    __neighborhoods: list[Neighborhood]

    def __init__(self, cells: list[Cell] = None, neighborhoods: list[Neighborhood] = None):
        self.__cells = cells or []
        self.__neighborhoods = neighborhoods or []

    def get_cell(self, position) -> Cell: return self.__cells[position]

    def get_name_cells(self) -> list[str]:
        names_cells = []

        for i in range(len(self.__cells)):
            names_cells.append(self.__cells[i].get_name())

        return names_cells

    def get_colors(self) -> list[str]:
        colors = []

        for cell in self.__cells:
            if isinstance(cell, Street):
                colors.append(cell.get_color())

        return colors

    def create_neighborhood(self) -> None:
        self.__cells.clear()

        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.BROWN, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.WHITE_BLUE, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.PURPLE, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.ORANGE, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.RED, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.YELLOW, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.GREEN, 0))
        self.__neighborhoods.append(Neighborhood(NeighborhoodTypes.BLUE, 0))

    def create_cells(self) -> None:
        companies = ['MAX', 'VK', 'RU Tube', 'Amazon', 'Google', 'Meta', 'Tesla', 'Intel', 'AMD', 'Oracle', 'IBM', 'Apple', 'Yandex', 'Nike', 'Sber', 'Tinkoff', 'Ozon', 'Avito', '1C', 'Kaspersky', 'ABBYY', 'Nexign', 'Naumen', 'Drom']
        self.__cells.clear()

        self.__cells.append(FreeParking(0, "Start"))

        j = 0
        k = 0

        for i in range(0, 40, 10):

            self.__cells.append(Street(i + 1, companies[k], 140, 50000, self.__neighborhoods[j]))
            self.__cells.append(Street(i + 3, companies[k+1], 140, 7000, self.__neighborhoods[j]))
            self.__cells.append(Chance(i + 2, "Chance"))
            self.__cells.append(Street(i + 4, companies[k+2], 160, 4000, self.__neighborhoods[j]))
            self.__cells.append(Station(i + 5, "Station", 200, 3000))
            self.__cells.append(Street(i + 6, companies[k+3], 160, 6000, self.__neighborhoods[j + 1]))
            self.__cells.append(Street(i + 8, companies[k+4], 140, 50000, self.__neighborhoods[j + 1]))
            self.__cells.append(Chance(i + 7, "Chance"))
            self.__cells.append(Street(i + 9, companies[k+5], 200, 7000, self.__neighborhoods[j + 1]))
            self.__cells.append(FreeParking(i + 10, ""))

            j += 2
            k += 6

        self.__cells[10] = FreeParking(10, "Cursion")
        self.__cells[20] = FreeParking(20, "Free Park")
        self.__cells[30] = Jail(30, "Jail")

    @staticmethod
    def is_free_parking(cell: Cell) -> bool:
        if isinstance(cell, FreeParking):
            return True

        return False

    @staticmethod
    def is_ownerless(cell: Cell) -> bool:
        if isinstance(cell, Ownership) and not cell.has_owner():
            return True

        return False

    @staticmethod
    def is_passed_go(position: int, points: int) -> bool:
        if (position + points) > Board.END: return True

        return False


class Cell(ABC):

    _x: int
    _name: str

    def __init__(self, x: int, name: str):

        if not isinstance(x, int):  raise TypeError("Тип данных не int")

        self._x = x
        self._name = name

    def get_name(self) -> str:
        return self._name

class FreeParking(Cell):

    def __init__(self, x: int, name: str):
        super().__init__(x, name)


class Chance(Cell):

    CASH = 200

    def __init__(self, x: int, name: str):
        super().__init__(x, name)
        self.__result = None

    def __str__(self):
        if self.__result == ChanceResultTypes.POSITIVE:
            return f"Вы попали на клетку шанс\n и получаете {Chance.CASH}💰"

        return f"Вы попали на клетку шанс\n вы вынуждены заплатить {Chance.CASH}💰"

    def try_luck(self) -> ChanceResultTypes:  # испытать удачу

        self.__solve_chance()

        if self.__result == ChanceResultTypes.POSITIVE:
            return ChanceResultTypes.POSITIVE

        else:
            return ChanceResultTypes.NEGATIVE


    def __solve_chance(self) -> None:  # вычислить шанс
        import random

        if random.randint(0, 10) > 5:
            self.__result = ChanceResultTypes.POSITIVE
        else:
            self.__result = ChanceResultTypes.NEGATIVE


class Ownership(Cell, ABC):
    # Модель Собственности

    _owner: IdBusinessman | None
    _price: int
    _rent: int

    def __init__(self, x: int, name: str, price: int, rent: int):
        super().__init__(x, name)

        if not isinstance(price, int):  raise  TypeError("Тип данных не int")
        if not isinstance(rent, int):  raise TypeError("Тип данных не int")

        self._owner = None
        self._price = price
        self._rent = rent

    def __str__(self):
        if self.has_owner():
            return f"Вы заплатили ренту {self.calculate_rent()}💰"

        return f"{self._name}: {self._price}💰"

    def __eq__(self, other: Ownership):
        return self._owner == other._owner and self._price == other._price and self._rent == other._rent

    @abstractmethod
    def calculate_price(self) -> int: raise NotImplemented()

    @abstractmethod
    def calculate_rent(self) -> int:  raise NotImplemented()

    def get_owner(self) -> IdBusinessman:
        if self._owner is None:  raise AssertionError("У собственности нет владельца")
        return self._owner

    def get_price(self) -> int:
        return self._price

    def set_owner(self, owner: IdBusinessman) -> None:

        if not isinstance(owner, IdBusinessman): raise TypeError("Тип данных не IdBusinessman")

        self._owner = owner

    def has_owner(self) -> bool:
        return not self._owner is None

    def identify_owner(self, owner: IdBusinessman) -> bool:
        return self._owner == owner or self._owner is None

    def unset_owner(self) -> None:
        self._owner = None


class Street(Ownership):

    HOME_MAX_COUNT = 4
    HOTEL_MAX_COUNT = 1

    __neighborhood: Neighborhood
    __builds: list[Building]

    def __init__(self, x: int, name: str, price: int, rent: int, neighborhood: Neighborhood):
        super().__init__(x, name, price, rent)

        self.__neighborhood =  neighborhood  # район
        self.__builds = []

    def __eq__(self, other: Street):
        return super().__eq__(other) and self.__neighborhood == other.__neighborhood


    def get_color(self) -> str:
        return self.__neighborhood.get_color()

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

    def create_build(self, price: int, type: int, ratio: int) -> None:  # построить дом
        self.__builds.append(Building(price, type, ratio))

    def can_build_home(self) -> bool: # можно ли построить дом
        if len(self.__builds) < Street.HOME_MAX_COUNT: return True

        return False

    def can_build_hotel(self) -> bool: # можно ли построить отель
        if len(self.__builds) == Street.HOME_MAX_COUNT : return True

        return False

    def __get_neighborhood(self) -> Neighborhood:
        return self.__neighborhood

    neighborhood = property(__get_neighborhood)


class Station(Ownership):

    def __init__(self, x: int, name: str, price: int, rent: int):
        super().__init__(x, name, price, rent)

    def calculate_price(self) -> int:
        return self._price

    def calculate_rent(self) -> int:
        return self._rent


class Jail(Cell):

    __prisoners: list[IdBusinessman]

    def __init__(self, x: int, name: str):
        super().__init__(x, name)

        self.__prisoners = []

    def __str__(self):
        return f"Вы попадаете в тюрьму и пропускаете ход 🙈"

    def conclude(self, id: IdBusinessman) -> None:
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        if self.__is_concluded(id):  raise AssertionError("Данный предприниматель уже заключён")

        self.__prisoners.append(id)

    def give_freedom(self, id: IdBusinessman) -> None:
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        if not id in self.__prisoners:  raise AssertionError("Данного предпринимателя нет в тюрьме")

        delete_index = 0

        for i in range(len(self.__prisoners)):
            if self.__prisoners[i] == id:
                delete_index = i
                break

        self.__prisoners.pop(delete_index)

    def __is_concluded(self, id: IdBusinessman) -> bool:

        if id in self.__prisoners: return True

        return False