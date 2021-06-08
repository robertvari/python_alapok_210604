from game_assets.characters import Player
from game_assets.places import Village, Tavern, Arena


class BattleOfClasses:
    def __init__(self):
        self._intro()
        self.player = Player().create()

        # create places
        self.village = Village(self)
        self.tavern = Tavern(self)
        self.arena = Arena(self)

        self.village.menu()

    @staticmethod
    def _intro():
        print("-"*50, "Battle of Classes", "-"*50)


if __name__ == '__main__':
    BattleOfClasses()

    # is A / has A
    # village is PlaceBase? True
    # village has BattleOfClasses? True