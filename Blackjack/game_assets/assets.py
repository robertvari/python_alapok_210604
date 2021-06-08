class PlayerBase:
    pass


class HumanPlayer(PlayerBase):
    pass


class AIPlayer(PlayerBase):
    pass


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
    card1 = Card("Spade", 2)
    card1.value = 11

    print(card1)