from src.models.businesman import Businessman, IdBusinessman


class PlayerManager:

    MAX_COUNT = 6

    __businessmen: list[Businessman]

    def __init__(self):
        self.__businessmen = []

    def get_businessmen(self) -> list[Businessman]:
        return self.__businessmen

    def try_add_businessmen(self, businessmen_count: int) -> bool:
        current_count = len(self.__businessmen)

        if current_count + businessmen_count > PlayerManager.MAX_COUNT: return False

        for i in range(businessmen_count+1):
            current_count = len(self.__businessmen)

            id = IdBusinessman(current_count)

            self.__businessmen.append(Businessman(id))

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