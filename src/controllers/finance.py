from src.models.idbusinessman import IdBusinessman

class BankAccount:

    __id: IdBusinessman
    __balance: int

    def __init__(self, id: IdBusinessman):
        if not isinstance(id, IdBusinessman):  raise TypeError()

        self.__id = id
        self.__balance = Bank.START_CAPITAL

    def __get_id(self) -> IdBusinessman: return self.__id

    def charge(self, money: int) -> None:
        if not isinstance(money, int):  raise TypeError()

        self.__balance += money

    def debit(self, money: int) -> None:
        if not isinstance(money, int):  raise TypeError()

        if self.__balance - money < 0: raise AssertionError()

        self.__balance -= money

    def has_enough_money(self, money: int) -> bool:
        if not isinstance(money, int):  raise TypeError()

        return self.__balance >= money

    id = property(__get_id)


class Bank:

    START_CAPITAL = 1500
    BONUS_GO = 200

    __accounts: list[BankAccount]

    def __init__(self, accounts: list[BankAccount] = None):
        if not accounts is None and not isinstance(accounts, list):  raise TypeError()

        self.__accounts = accounts or []

    def register_account(self, id: IdBusinessman) -> None:
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        if id in self.__accounts:  raise AssertionError("Аккаунт уже добавлен")

        self.__accounts.append(BankAccount(id))

    def deregister_account(self, id: IdBusinessman) -> None:
        if not isinstance(id, IdBusinessman):  raise TypeError("Тип данных не IdBusinessman")

        if not id in self.__accounts:  raise AssertionError("Аккаунта нет в списке")

        delete_index = 0

        for i in range(len(self.__accounts)):
            if self.__accounts[i].id == id:
                delete_index = i

        self.__accounts.pop(delete_index)

    def charge_account(self, money: int, id: IdBusinessman) -> None:
        if not isinstance(money, int):  raise TypeError()
        if not isinstance(id, IdBusinessman):  raise TypeError()

        account = self.__search_account(id)

        if account is None:  raise AssertionError("")

        account.charge(money)

    def debit_account(self, money: int, id: IdBusinessman) -> None:
        if not isinstance(money, int):  raise TypeError()
        if not isinstance(id, IdBusinessman):  raise TypeError()

        account = self.__search_account(id)

        if account is None:  raise ValueError()

        account.debit(money)

    def has_enough_money(self, money: int, id: IdBusinessman) -> bool:
        if not isinstance(money, int):  raise TypeError()
        if not isinstance(id, IdBusinessman):  raise TypeError()

        account = self.__search_account(id)

        if account is None:  raise ValueError()

        return account.has_enough_money(money)


    def __search_account(self, id: IdBusinessman) -> BankAccount | None:
        if not isinstance(id, IdBusinessman):  raise TypeError()

        for account in self.__accounts:
            if account.id == id:
                return account

        return None