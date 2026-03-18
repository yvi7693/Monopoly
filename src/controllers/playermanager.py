from src.controllers.finance import Bank
from src.models.businesman import Businessman, IdBusinessman
from src.models.gameboard import Ownership


class PlayerManager:

    MAX_COUNT = 6

    __businessmen: list[Businessman]

    def __init__(self, bank: Bank):
        self.__businessmen = []
        self.__bank = bank

    def get_businessmen(self) -> list[Businessman]:

        businessmen = []

        for businessman in self.__businessmen:
            businessmen.append(businessman.copy(businessman))


        return businessmen

    def try_add_businessmen(self, businessmen_count: int) -> bool:
        current_count = len(self.__businessmen)

        if current_count + businessmen_count > PlayerManager.MAX_COUNT: return False

        for i in range(businessmen_count+1):
            current_count = len(self.__businessmen)

            id = IdBusinessman(current_count)

            self.__businessmen.append(Businessman(id))

            self.__bank.register_account(id)

        return True

    def exclude_businessman(self, businessman: Businessman) -> None:
        if not isinstance(businessman, Businessman):  raise TypeError("Тип данных не Businessman")

        if not businessman in self.__businessmen: raise AssertionError("Данного предпринимателя нет в списке")

        delete_index = 0

        for i in range(len(self.__businessmen)):
            if self.__businessmen == businessman:
                delete_index = i
                break

        self.__businessmen.pop(delete_index)

        self.__bank.deregister_account(businessman.id)

    def add_ownership(self, ownership: Ownership, id: IdBusinessman) -> None:

        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")
        if not isinstance(ownership, Ownership):  raise TypeError("Тип данных не Ownership")

        businessman = self.__search_businessman(id)

        if businessman is None:  raise AssertionError("Текущий предприниматель не найден")

        businessman.delete_ownership(ownership)

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

    def __search_businessman(self, id: IdBusinessman) -> Businessman | None:

        for i in range(len(self.__businessmen)):

            if self.__businessmen[i].id == id:

                businessman = self.__businessmen[i]

                return businessman

        return None




