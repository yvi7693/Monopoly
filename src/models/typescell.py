from dataclasses import dataclass
from enum import Enum

from typing_extensions import Literal




class NeighborhoodTypes(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    BROWN = "brown"
    PURPLE = "purple"
    ORANGE = "orange"
    WHITE_BLUE = "#87CEEB"


@dataclass
class Neighborhood:

    MAX_COUNT_STREET = 3

    __type: NeighborhoodTypes
    __build_price: int

    def __init__(self, type: NeighborhoodTypes, build_price: int):
        self.__type = type
        self.__build_price = build_price

    def __eq__(self, other):
        return self.type == other.type

    def get_color(self) -> str:
        color = self.__type

        if color == NeighborhoodTypes.BLUE: return "#4169E1"
        if color == NeighborhoodTypes.RED: return "#FF0000"
        if color == NeighborhoodTypes.YELLOW: return "#FFFF00"
        if color == NeighborhoodTypes.BROWN: return "#8B4513"
        if color == NeighborhoodTypes.PURPLE: return "#FF00FF"
        if color == NeighborhoodTypes.GREEN: return "#00FF00"
        if color == NeighborhoodTypes.ORANGE: return "#F4A460"
        return "#87CEEB"

    def __get_build_price(self) -> int: return self.__build_price

    def __get_type(self) -> NeighborhoodTypes: return self.__type

    build_price = property(__get_build_price)
    type = property(__get_type)


@dataclass
class ChanceResultTypes(Enum):

    POSITIVE = 1
    NEGATIVE = -1


class StatusOwner(Enum):
    BOUGHT = 0
    NOT_MONEY = 1
    NOT_WISH = 2
    PAID_RENT = 3


class CurrentStatusOwner:

    __status: Literal[StatusOwner.BOUGHT, StatusOwner.NOT_MONEY, StatusOwner.NOT_WISH, StatusOwner.PAID_RENT] | None

    def __init__(self):
        self.__status = None

    def set_status(self, new_status: Literal[StatusOwner.BOUGHT, StatusOwner.NOT_MONEY, StatusOwner.NOT_WISH, StatusOwner.PAID_RENT]) -> None:

        if new_status not in [StatusOwner.BOUGHT, StatusOwner.NOT_MONEY, StatusOwner.NOT_WISH, StatusOwner.PAID_RENT]:
            raise ValueError("Не соответствует ожидаемому значению")

        self.__status = new_status

    def get_status(self) -> Literal[StatusOwner.BOUGHT, StatusOwner.NOT_MONEY, StatusOwner.NOT_WISH, StatusOwner.PAID_RENT] | None:
        return self.__status

class TypeMessage(Enum):
    INFO = 0
    ASK = 1
    ERROR = 2



