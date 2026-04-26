from dataclasses import dataclass


@dataclass
class IdBusinessman:

    __id: int

    def __str__(self):
        return str(self.__id)

    def get_value(self) -> int:
        return self.__id