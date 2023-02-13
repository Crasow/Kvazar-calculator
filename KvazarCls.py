from random import randint


class Kvazar:
    def __init__(self, kvin: object, azu: object, ari: object):
        self.hp = 0
        self.kvin = kvin
        self.azu = azu
        self.ari = ari
        self.all = [self.kvin, self.azu, self.ari]

    # Genereate cobold`s max hp
    def set_max_hp(self, max_hp: str):
        kvazar_max_hp = int(max_hp)
        self.azu.max_hp = int(kvazar_max_hp / 2)
        self.ari.max_hp = int(kvazar_max_hp * 2 / 10)
        self.kvin.max_hp = int(kvazar_max_hp - self.ari.max_hp - self.azu.max_hp)

        self.rest()  # refresh current hp

    # write damage to one of cobolds and return target
    def get_damage(self, damage):
        # Shortening the code
        kvin = self.kvin
        azu = self.azu
        ari = self.ari

        # Clear logs about last damage
        for cob in self.all:
            cob.damage_taken = 0

        d10roll = randint(1, 10)  # Roll who will get damage
        if d10roll in kvin.get_hit_chance:
            target = kvin
        elif d10roll in azu.get_hit_chance:
            target = azu
        else:
            target = ari

        target.damage_taken = damage
        target.get_damage(damage)
        targets = [target]

        # Cobolds have prioritet of getting damage: first of all Azu, then Kvin and last - Ari
        if target.hp < 0:  # if anyone`s hp become below 0 next in priority must get residual dmg
            cobolds_prior_list = [azu, kvin, ari]
            cobolds_prior_list.remove(target)  # get list of candidates except died cobold
            target.damage_taken = damage + target.hp  # recalculate what damage he got before hp become 0
            residual_dmg = target.hp  # what damage goes to next cob
            while residual_dmg <= 0 and cobolds_prior_list:  # cycle for every remaining dmg or cob
                target.hp = 0  # make zero hp of died cob
                target = cobolds_prior_list.pop(0)  # new target in priority
                targets.append(target)
                target_hp_be4_hit = target.hp
                target.hp += residual_dmg  # first in prior (Azu or Kvin) get dmg
                if target.hp > 0:
                    target.damage_taken = residual_dmg
                else:
                    target.damage_taken = target_hp_be4_hit
                residual_dmg = target.hp

        return targets

    def get_heal(self, target, heal):
        target.heal(heal)

        return f'{target.name} был похилен на {heal} хп\n'

    def rest(self):
        for cobold in self.all:
            cobold.rest()

    # ------ Config part ------
    def set_hp(self, target, hp):
        target.hp = hp

    def set_hit_chance(self, target, chance):
        target.get_hit_chance = chance
