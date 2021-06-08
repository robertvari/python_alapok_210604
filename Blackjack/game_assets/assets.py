import random
from faker import Faker

fake = Faker()


class PlayerBase:
    def __init__(self):
        self._name = None
        self._credits = random.randint(100, 1000)
        self._hand = []
        self.in_game = True

    def create(self):
        self._name = fake.name()
        return self

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}"

    def __repr__(self):
        return str(self._name)


class HumanPlayer(PlayerBase):
    def create(self):
        self._name = input("What is your name?")
        return self


class AIPlayer(PlayerBase):
    pass


class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        self.cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                card_name = f"{name} {card[0]}"
                value = card[1]

                new_card = Card(name, value)
                self.cards.append(new_card)

        random.shuffle(self.cards)


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, in_value):
        assert isinstance(in_value, int), "Value must be of type integer."
        self._value = in_value

    def __repr__(self):
        return f"{self._name}: {self.value}"


if __name__ == '__main__':
    ai_player1 = AIPlayer().create()
    ai_player2 = AIPlayer().create()

    human_player = HumanPlayer().create()

    print(ai_player1)
    print(ai_player2)
    print(human_player)