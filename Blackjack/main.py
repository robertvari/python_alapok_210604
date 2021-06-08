from game_assets.assets import HumanPlayer, AIPlayer, Deck


class Blackjack:
    def __init__(self):
        self._intro()

        self._deck = Deck()

        self.AI_Player = AIPlayer().create()
        self.Human_Player = HumanPlayer().create()

    @staticmethod
    def _intro():
        print('-'*50, "BLACKJACK", '-'*50)


if __name__ == '__main__':
    Blackjack()