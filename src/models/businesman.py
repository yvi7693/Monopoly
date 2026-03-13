from src.models.gameboard import Ownership


class Businessman:

    def __init__(self):

        self.__balance = 1500
        self.__ownerships = []
        self.__position = 0

    def get_balance(self) -> int: return self.__balance

    def get_position(self) -> int: return self.__position

    def add_ownership(self, ownership: Ownership) -> None:
        if not isinstance(ownership, Ownership): raise TypeError()

        self.__ownerships.append(ownership)

    def delete_ownership(self, delete_ownership: Ownership):
        delete_index = 0

        for i in range(len(self.__ownerships)):
            if self.__ownerships[i] == delete_ownership:
                delete_index = i

        self.__ownerships.pop(delete_index)

    def make_move(self, points: int) -> None:
        if not isinstance(points, int): raise TypeError()
        self.__position += points

    def increase_balance(self, money: int) -> None: self.__balance += money

    def decrease_balance(self, money: int) -> None: self.__balance -= money

    def check_balance(self, price: int) -> bool: return self.__balance >= price