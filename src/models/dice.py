import random

class Dice:

    @staticmethod
    def throw() -> tuple[int, int]:
        return random.randint(1,6), random.randint(1,6)