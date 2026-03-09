class Businessman:

    def __init__(self, balance):

        self.__balance = balance
        self.__ownerships = []

    def get_balance(self) -> int:
        pass

    def add_ownership(self, ownership):
        pass

    def delete_ownership(self, ownership):
        pass

    def increase_balance(self, money): # увеличить баланс
        pass

    def decrease_balance(self, money):  # уменьшить баланс
        pass

    def make_move(self) -> int:  # сделать ход
        pass

    def check_balance(self, price) -> bool:
        pass