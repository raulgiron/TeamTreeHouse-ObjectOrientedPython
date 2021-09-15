class Card:
    """Card class that will handle the init, eq and str methods."""

    def __init__(self, word: str, location: str):
        """Initialize ours class methods.
            :param word
            :param location
        """
        self.card = word
        self.location = location
        self.matched = False

    def __eq__(self, other):
        """Verifies the cards equality.
            :param other
        """
        return self.card == other.card

    def __str__(self):
        """Return card as string."""
        return self.card


if __name__ == "__main__":
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')

    print(card1 == card2)
    print(card1 == card3)
