import random

class Dice:

    STAND_STILL = (0,0)

    MIN_VALUE = 1
    MAX_VALUE = 6

    @staticmethod
    def throw() -> tuple[int, int]:
        return random.randint(Dice.MIN_VALUE,Dice.MAX_VALUE), random.randint(Dice.MIN_VALUE,Dice.MAX_VALUE)