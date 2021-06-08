from game_assets.assets import HumanPlayer, AIPlayer, Deck


class Blackjack:
    def __init__(self):
        self._intro()

        self._deck = Deck()

        self._min_bet = 10
        self._bet = 0

        self._players = [AIPlayer().create() for i in range(3)]

        self.Human_Player = HumanPlayer().create()
        self._players.append(self.Human_Player)

        self._game()

    def _game(self):
        print(f"You have {self.Human_Player.credits}")
        print(f"You are playing with {self._players[:-1]}")

        for player in self._players:
            self._bet += player.give_bet(self._min_bet)
            player.draw_cards(self._deck)

        self._get_winner()

    def _get_winner(self):
        player_list = [p for p in self._players if p.count_hand() <= 21]

        if player_list:
            winner_list = sorted(player_list, key=lambda p: p.count_hand())
            winner = winner_list[-1]
            print(f"The winner is {winner} who wins {self._bet} credits")
            winner.set_credits(self._bet)
        else:
            print("Nobody wins this time :(")

    @staticmethod
    def _intro():
        print('-'*50, "BLACKJACK", '-'*50)


if __name__ == '__main__':
    Blackjack()