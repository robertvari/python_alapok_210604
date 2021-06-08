from .characters import Enemy


class PlaceBase:
    def __init__(self, main_game):
        self._name = None
        self._main_game = main_game

    def menu(self):
        pass


class Village(PlaceBase):
    def __init__(self, main_game):
        super(Village, self).__init__(main_game)
        self._name = "Village"

    def menu(self):
        print("You are standing in a small village.\nYou can see a Tavern and an Arena.")
        choice = input("What is your choice? (1. Tavern, 2. Arena)")

        if choice == "1":
            self._main_game.tavern.menu()

        if choice == "2":
            self._main_game.arena.menu()


class Tavern(PlaceBase):
    def __init__(self, main_game):
        super(Tavern, self).__init__(main_game)
        self._name = "Tavern"


class Arena(PlaceBase):
    def __init__(self, main_game):
        super(Arena, self).__init__(main_game)
        self._name = "Arena"
        self._enemy = Enemy().create()

    def menu(self):
        print(f"You stepped into the Arena and an {self._enemy.race} runs toward you.")
        player = self._main_game.player

        while True:
            player.attack(self._enemy)

            if not self._enemy.is_alive:
                print(f"The {self._enemy.race} is dead")
                break

            self._enemy.attack(player)

            if not player.is_alive:
                print("You are dead :(")
                break