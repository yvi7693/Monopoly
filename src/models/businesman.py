from __future__ import annotations

from copy import deepcopy

from src.models.gameboard import Ownership, Board, Neighborhood, Street
from src.models.idbusinessman import IdBusinessman


class Businessman:

    def __init__(self, id: IdBusinessman, position: int = Board.START, ownerships: list[Ownership] = None):

        self.__id = id
        self.__ownerships = ownerships or []
        self.__position = position

    def get_ownerships_names(self) -> str:
        names_ownership = ""

        for ownership in self.__ownerships:
            if not isinstance(ownership, Street):
                names_ownership += f"{ownership.get_name()}\n"

            else:
                count_building = len(ownership.get_builds())

                if count_building > 4:
                    emoji = "🏨"
                else:
                    emoji = "🏠" * count_building

                names_ownership += f"{ownership.get_name()}{emoji}\n"


        return names_ownership

    def get_ownerships_names_list(self) -> list[str]:
        names_ownership = []

        for ownership in self.__ownerships:
            names_ownership.append(ownership.get_name())

        return names_ownership

    def get_street_names(self) -> list[str]:
        names_street = []

        for ownership in self.__ownerships:
            if isinstance(ownership, Street):

                names_street.append(ownership.get_name())

        return names_street

    def get_street(self) -> list[Street]:
        streets = []

        for ownership in self.__ownerships:
            if isinstance(ownership, Street):
                streets.append(ownership)

        return streets

    def get_position(self) -> int: return self.__position

    def set_position(self, points: int) -> None:
        if not isinstance(points, int): raise TypeError("Тип данных не int")
        self.__position = points

    def add_ownership(self, ownership: Ownership) -> None:
        if not isinstance(ownership, Ownership): raise TypeError("Тип данных не Ownership")

        if ownership in self.__ownerships: raise TypeError("Данная собственность уже находится во владении")

        self.__ownerships.append(ownership)

    def delete_ownership(self, delete_ownership: Ownership):
        if not isinstance(delete_ownership, Ownership):  raise TypeError("Тип данных не Ownership")

        if not delete_ownership in self.__ownerships: raise TypeError("Данной собственности нет в списке собственностей")

        delete_index = 0

        for i in range(len(self.__ownerships)):
            if self.__ownerships[i] == delete_ownership:
                delete_index = i

        self.__ownerships.pop(delete_index)

    def has_title_deeds(self, search_ownership: Ownership) -> bool:
        if not isinstance(search_ownership, Ownership):  raise TypeError("Тип данных не Ownership")

        for ownership in self.__ownerships:
            if ownership == search_ownership:
                return True

        return False

    def has_neighborhood_by_street(self, neighborhood: Neighborhood) -> bool:
        count = 0

        for ownership in self.__ownerships:
            if ownership.neighborhood == neighborhood:
                count += 1

        if count == Neighborhood.MAX_COUNT_STREET: return True

        return False

    def __get_id(self) -> IdBusinessman:
        return self.__id

    def __get_ownerships(self) -> list[Ownership]:
        copy_ownerships = []

        for i in range(len(self.__ownerships)):
            copy_ownerships.append(deepcopy(self.__ownerships[i]))

        return copy_ownerships

    @staticmethod
    def copy(businessman: Businessman) -> Businessman:
        return Businessman(businessman.id, businessman.get_position() ,businessman.__ownerships)

    id = property(__get_id)
    ownerships = property(__get_ownerships)
