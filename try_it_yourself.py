from random import randint
from random import sample


class Die:
    """Roll Die class. This is a basic learning project."""
    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self):
        """This method is intended to roll the dice."""
        die = randint(1, self.sides)
        return die


class Lottery:
    """Winner of lottery. This is a basic learning project."""

    def __init__(self):
        self.lottery_database = (14, 5, 'R', 36, 56, 'D', 63, 96, 'A', 68, 85, 'J', 14, 45, 'V')

    def lottery_winner(self):
        winner = sample(self.lottery_database, 4)
        # print(f"Congratulations, any ticket matching these four numbers or letters wint a prize: \n\t{winner}")
        return winner


if __name__ == "__main__":
    dado = Die()
    print(f"Die: {dado.roll_die()}")
    concurso = Lottery()
    concurso.lottery_winner()
    counter: int = 0
    winner_tickets = [14, 'R', 45, 85]
    winner_numbers = Lottery()
    while True:
        counter += 1
        if winner_numbers.lottery_winner() == winner_tickets:
            print(f"Congratulations, you win the prize!!!\n\tNote: you needed -{counter:,}- trials to win.")
            break
        else:
            continue
