class Cobold:
    hp: int
    name: str

    def __init__(self, name, get_hit_chance: str):
        self.name = name
        self.max_hp = 0
        self.hp = self.max_hp
        self.get_hit_chance = get_hit_chance  # some range of dice values to hit cobold
        self.damage_taken = 0

    def get_damage(self, damage):
        self.hp -= damage

    def heal(self, heal):
        self.hp += heal

    def rest(self):
        self.hp = self.max_hp
