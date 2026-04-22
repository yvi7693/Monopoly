from src.controllers.finance import Bank
from src.models.businesman import Businessman, IdBusinessman
from src.models.gameboard import Ownership, Street


class PlayerManager:

    MAX_COUNT = 6

    __businessmen: list[Businessman]

    def __init__(self, bank: Bank):
        self.__businessmen = []
        self.__bank = bank

        self.__queue = 0

    def get_current_businessman(self) -> Businessman:

        max_count_businessman = len(self.__businessmen)

        current_businessman = self.__businessmen[self.__queue]

        self.__queue += 1

        if self.__queue >= max_count_businessman:
            self.__queue = 0

        return current_businessman

    def add_businessmen(self, businessmen_count: int) -> None:

        for i in range(businessmen_count):
            current_count = len(self.__businessmen)

            id = IdBusinessman(current_count)

            self.__businessmen.append(Businessman(id))

            self.__bank.register_account(id)

    def exclude_businessman(self, id : IdBusinessman) -> None:
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        businessman = self.__search_businessman(id)

        delete_index = 0

        for i in range(len(self.__businessmen)):
            if self.__businessmen[i] == businessman:
                delete_index = i
                break

        self.__businessmen.pop(delete_index)

        self.__bank.deregister_account(businessman.id)

        if len(self.__businessmen) == 0:
            self.__queue = 0

        elif delete_index < self.__queue:
            self.__queue -= 1

        elif self.__queue >= len(self.__businessmen):
            self.__queue = 0

    def add_ownership(self, ownership: Ownership, id: IdBusinessman) -> None:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")
        if not isinstance(ownership, Ownership):  raise TypeError("Тип данных не Ownership")

        businessman = self.__search_businessman(id)

        if businessman is None:  raise AssertionError("Текущий предприниматель не найден")

        businessman.add_ownership(ownership)

    def delete_ownership(self, ownership: Ownership, id: IdBusinessman) -> None:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")
        if not isinstance(ownership, Ownership):  raise TypeError("Тип данных не Ownership")

        businessman = self.__search_businessman(id)

        if businessman is None:  raise AssertionError("Текущий предприниматель не найден")

        businessman.delete_ownership(ownership)

    def has_tittle_deeds(self, ownership: Ownership, id: IdBusinessman) -> bool:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")
        if not isinstance(ownership, Ownership):  raise TypeError("Тип данных не Ownership")

        businessman = self.__search_businessman(id)

        if businessman is None:  raise AssertionError("Текущий предприниматель не найден")

        return businessman.has_title_deeds(ownership)

    def has_neighborhood(self, id: IdBusinessman, street: Street) -> bool:
        businessman = self.__search_businessman(id)

        if businessman.has_neighborhood_by_street(street.neighborhood):
            return True

        return False

    def get_businessmen(self) -> list[Businessman]:
        businessmen_copy = []

        for i in range(len(self.__businessmen)):
            businessmen_copy.append(Businessman.copy(self.__businessmen[i]))

        return businessmen_copy

    def __search_businessman(self, id: IdBusinessman) -> Businessman | None:

        for i in range(len(self.__businessmen)):

            if self.__businessmen[i].id == id:

                businessman = self.__businessmen[i]

                return businessman

        return None


class BankruptManager:

    __player_manager: PlayerManager
    __bankrupts: list[IdBusinessman]

    def __init__(self, player_manager: PlayerManager):
        self.__player_manager = player_manager
        self.__bankrupts = []

    def bankrupting(self, id: IdBusinessman) -> None:
        if id in self.__bankrupts: return None

        self.__bankrupts.append(id)
        self.__player_manager.exclude_businessman(id)

        return None

    def is_bankrupt(self, id: IdBusinessman) -> bool:
        return id in self.__bankrupts


class WinnerManager:

    ONE_PLAYER = 1

    __player_manager: PlayerManager
    __winner: Businessman | None

    def __init__(self, player_manager: PlayerManager):

        self.__player_manager = player_manager
        self.__winner = None

    def get_winner(self) -> Businessman:
        return self.__winner

    def chek_winner(self) -> bool:
        return len(self.__player_manager.get_businessmen()) == WinnerManager.ONE_PLAYER

    def declare_winner(self, businessman: Businessman) -> None:
        self.__winner = businessman

    def is_winner(self) -> bool:
        return not self.__winner is None






