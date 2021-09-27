import json
import unittest
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
        print(f"Congratulations, any ticket matching these four numbers or letters wint a prize: \n\t{winner}")
        return winner


filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/favorite_number.json'


def already_stored():
    try:
        with open(filename, 'r') as file_object:
            favorite_number = json.load(file_object)
            # print(f"I know your favorite number! It's {favorite_number}.")
            return favorite_number
    except FileNotFoundError:
        favorite_number = input("Please type your favorite number: ")
        with open(filename, 'w') as file_object:
            json.dump(int(favorite_number), file_object)
            print(f"Your favorite number {favorite_number}, was saved. I'll remember it nex time.")
            return favorite_number


class TestFavoriteNumber(unittest.TestCase):
    """This class test the already_stored function."""

    def test_already_stored(self):
        """Do numbers like '8.' work?"""
        stored_number = already_stored()
        self.assertEqual(stored_number, 55)


def world(city: str, country: str, population: int = None):
    if population:
        place = f"{city}, {country} - Population {population:,}."
        return place
    else:
        place = f"{city}, {country}."
        return place


class TestWorld(unittest.TestCase):
    """This class test the world function."""

    def test_city_country(self):
        """Do args like 'Santo Domingo, Dominican Republic.' work?"""
        formatted_place = world('Santo Domingo', 'Dominican Republic')
        self.assertEqual(formatted_place, 'Santo Domingo, Dominican Republic.')

    def test_city_country_population(self):
        """Do args like 'Santo Domingo, Dominican Republic - Population 2,201,941.' work?"""
        formatted_place = world('Santo Domingo', 'Dominican Republic', 2201941)
        self.assertEqual(formatted_place, 'Santo Domingo, Dominican Republic - Population 2,201,941.')


class Employee:
    """This class takes a name, a last name, and an annual salary."""

    def __init__(self, name: str, last_name: str, annual_salary):
        self.name = name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        raised_salary = salary_raise + self.annual_salary
        # print(f"\nCongrats!, {self.name.title()} {self.last_name.title()}."
        #       f"Your annual salary was raise by {salary_raise:,.2f}"
        #       f"\n\tYour new annual salary will be US${raised_salary:,.2f}\n")
        return raised_salary


class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """Created two instance of Employee"""
        self.default = Employee('raul', 'giron', 150000)
        self.custom = Employee('vicente', 'giron', 100000)

    def test_give_default_rise(self):
        total = self.default.give_raise()
        self.assertEqual(total, 155000)

    def test_give_custom_rise(self):
        total = self.custom.give_raise(200000)
        self.assertEqual(total, 300000)


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
    already_stored()
    raul = world('D.N.', 'Dominican Republic')
    print(raul)
    prueba = Employee('raul', 'giron', 120000)
    prueba.give_raise()
    unittest.main()
