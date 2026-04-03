from dataclasses import dataclass


@dataclass
class IdBusinessman:

    id: int

    def get_value(self) -> int:
        return self.id