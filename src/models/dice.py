class Dice:

    @staticmethod
    def throw() -> int:
        import random

        return random.randint(2,12)