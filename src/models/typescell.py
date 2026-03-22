from dataclasses import dataclass
from enum import Enum


@dataclass
class ChanceResultTypes(Enum):

    POSITIVE = 1
    NEGATIVE = -1


@dataclass
class NeighborhoodTypes(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    BROWN = 4
    PURPLE = 5
    ORANGE = 7
    BLACK = 8


@dataclass
class Neighborhood:

    MAX_COUNT_STREET = 3

    __type: NeighborhoodTypes
    __build_price: int

    def __eq__(self, other):
        return self.type == other.type

    def __get_build_price(self) -> int: return self.__build_price

    def __get_type(self) -> NeighborhoodTypes: return self.__type

    build_price = property(__get_build_price)
    type = property(__get_type)
