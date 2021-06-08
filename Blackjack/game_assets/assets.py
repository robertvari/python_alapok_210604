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

    def draw_cards(self, deck):
        while self.in_game:
            # check hand value
            hand_value = self._count_hand()

            if hand_value > 16:
                self.in_game = False
                print(f"{self._name} passes...")
            else:
                new_card = deck.give_card()
                self._hand.append(new_card)

    def _count_hand(self):
        return sum([card.value for card in self._hand])

    def show_hand(self):
        print(f"Hand value: {self._count_hand()}. Cards: {self._hand}")

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}"

    def __repr__(self):
        return str(self._name)


class HumanPlayer(PlayerBase):
    def create(self):
        self._name = input("What is your name?")
        return self

    def draw_cards(self, deck):
        print(f"This is your turn {self._name}")

        while self.in_game:
            self.show_hand()

            hand_value = self._count_hand()
            if hand_value > 21:
                self.in_game = False
                print(f"Your hand value is to much: {hand_value}. You lost this round.")
                break

            player_input = input("Do you want to draw a card?(y/n)")
            if player_input == "y":
                new_card = deck.give_card()
                print(f"The new card is: {new_card}")

                self._hand.append(new_card)
            else:
                print("You passed")
                self.in_game = False


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

    def give_card(self):
        current_card = self.cards[-1]
        self.cards.remove(current_card)
        return current_card


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
    ai_player = AIPlayer().create()
    human_player = HumanPlayer().create()

    deck = Deck()

    ai_player.draw_cards(deck)
    human_player.draw_cards(deck)

    ai_player.show_hand()
    human_player.show_hand()