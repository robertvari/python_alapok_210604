import random


class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100},
        "ork": {"strength": 130, "max_HP": 200},
        "elf": {"strength": 60, "max_HP": 100},
        "dwarf": {"strength": 100, "max_HP": 220},
    }

    def __init__(self):
        # base attributes
        self._name = None
        self._race = None
        self._inventory = []
        self._golds = random.randint(0, 100)

        #combat attributes
        self._left_hand = None
        self._right_hand = None

        self._strength = 100
        self._max_HP = 100
        self._current_HP = self._max_HP

    def create(self):
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        self._name = f"{random.choice(FIRST)}{random.choice(SECOND)}"

        self._race = random.choice(list(self.races))

        self._max_HP = self.races[self._race]["max_HP"]
        self._current_HP = self._max_HP

        self._strength = self.races[self._race]["strength"]

        return self

    def report(self):
        print(f"Name: {self._name}\nRace: {self._race}\nStrength: {self._strength}\nGolds: {self._golds}")

    @property
    def race(self):
        return self._race

    def attack(self, other):
        attack_strength = random.randint(0, self._strength)

        if attack_strength == 0:
            print(f"{self._name} misses {other}")
        else:
            other.set_current_HP(attack_strength)

    def set_current_HP(self, value):
        self._current_HP -= value

    @property
    def is_alive(self):
        return self._current_HP > 0

    def __repr__(self):
        return self._name


class Player(CharacterBase):
    def create(self):
        self._name = "Robert"
        self._race = "human"

        # todo check player race

        self._max_HP = self.races[self._race]["max_HP"]
        self._current_HP = self._max_HP
        self._strength = self.races[self._race]["strength"]

        return self


class Enemy(CharacterBase):
    pass


if __name__ == '__main__':
    enemy1 = Enemy().create()
    enemy2 = Enemy().create()
    enemy3 = Enemy().create()

    player = Player().create()

    player.report()