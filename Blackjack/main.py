from game_assets.assets import HumanPlayer, AIPlayer


class Blackjack:
    def __init__(self):
        self._intro()

        self.human_player = HumanPlayer()


    @staticmethod
    def _intro():
        print('-'*50, "BLACKJACK", '-'*50)


if __name__ == '__main__':
    Blackjack()