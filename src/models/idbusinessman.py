from dataclasses import dataclass


@dataclass
class IdBusinessman:

    id: int

    def __str__(self):
        return str(self.id)

    def get_value(self) -> int:
        return self.id