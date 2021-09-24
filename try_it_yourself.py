from random import randint


class Die:
    """Roll Die class. This is a basic learning project."""
    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self):
        """This method is intended to roll the dice."""
        die = randint(1, self.sides)
        print(die)
        return die


if __name__ == "__main__":
    dado = Die()
    dado.roll_die()
