from src.models.gameboard import Ownership, Board
from dataclasses import dataclass

@dataclass
class IdBusinessman:

    id: int


class Businessman:

    def __init__(self, id: IdBusinessman):

        self.__id = id
        self.__ownerships = []
        self.__position = Board.START

    def get_position(self) -> int: return self.__position

    def __get_id(self) -> IdBusinessman: return self.__id

    def add_ownership(self, ownership: Ownership) -> None:
        if not isinstance(ownership, Ownership): raise TypeError()

        self.__ownerships.append(ownership)

    def delete_ownership(self, delete_ownership: Ownership):
        if not isinstance(delete_ownership, Ownership):  raise TypeError()

        delete_index = 0

        for i in range(len(self.__ownerships)):
            if self.__ownerships[i] == delete_ownership:
                delete_index = i

        self.__ownerships.pop(delete_index)

    def make_move(self, points: int) -> None:
        if not isinstance(points, int): raise TypeError()
        self.__position += points

    def has_tittle_deeds(self, search_ownership: Ownership) -> bool:
        if not isinstance(search_ownership, Ownership):  raise TypeError()

        for ownership in self.__ownerships:
            if ownership == search_ownership:
                return True

        return False

    id = property(__get_id)