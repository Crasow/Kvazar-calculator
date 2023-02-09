def get_hp(message):
    general_hp = int(message)
    azu_hp = int(general_hp / 2)
    ari_hp = int(general_hp * 2 / 10)
    kvin_hp = int(general_hp - ari_hp - azu_hp)

    print(f'{azu_hp} {ari_hp} {kvin_hp}')


get_hp('17')
