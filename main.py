from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from random import randint

Window.clearcolor = (41 / 255, 43 / 255, 44 / 255, 1)

kvazar_names = ["Квин", "Азу", "Ари"]


class MyApp(App):
    def __init__(self):
        super().__init__()
        # -----------------------------------------------------------------------
        self.general_max_hp = 0
        self.azu_max_hp = 0
        self.ari_max_hp = 0
        self.kvin_max_hp = 0
        # -----------------------------------------------------------------------
        self.azu_hp = self.azu_max_hp
        self.ari_hp = self.ari_max_hp
        self.kvin_hp = self.kvin_max_hp
        # -----------------------------------------------------------------------

        self.max_hp_label = Label(text="Макс ХП Квазара:")
        self.input_max_hp = TextInput(hint_text="Макс HP персонажа",
                                      background_color="#3C3F41",
                                      foreground_color="#FFFFFF")
        self.input_max_hp.bind(text=self.input_max_hp_changed)
        self.input_damage = TextInput(hint_text="Урон",
                                      background_color="#3C3F41",
                                      foreground_color="#FFFFFF")
        self.log_hp_label = Label()
        self.damage_submit_btn = Button(text="Готово", on_press=self.damage_submit)
        self.real_hp_label = Label(text="Текущие ХП Квазара:")

        self.heal_submit_btn = Button(text="Похилить", on_press=self.heal_submit)
        self.heal_log_label = Label()
        self.input_heal_kvin = TextInput(hint_text="Хил Квин",
                                         background_color="#3C3F41",
                                         foreground_color="#FFFFFF")
        self.input_heal_azu = TextInput(hint_text="Хил Азу",
                                        background_color="#3C3F41",
                                        foreground_color="#FFFFFF")
        self.input_heal_ari = TextInput(hint_text="Хил Ари",
                                        background_color="#3C3F41",
                                        foreground_color="#FFFFFF")
        self.rest_btn = Button(text="Отдых", on_press=self.rest_btn_pressed)
        self.set_hp_btn = Button(text="Установить", on_press=self.set_hp)

    def refresh_real_hp(self):
        self.real_hp_label.text = f'Текущие ХП Квазара:\n\nКвин - {self.kvin_hp}\n' \
                                  f'Азу - {self.azu_hp}\nАри - {self.ari_hp}'

    def set_hp(self, *args):
        if self.input_heal_kvin.text:
            self.kvin_hp = int(self.input_heal_kvin.text)
        if self.input_heal_azu.text:
            self.azu_hp = int(self.input_heal_azu.text)
        if self.input_heal_ari.text:
            self.ari_hp = int(self.input_heal_ari.text)

        self.refresh_real_hp()

    def rest_btn_pressed(self, *args):
        self.azu_hp = self.azu_max_hp
        self.ari_hp = self.ari_max_hp
        self.kvin_hp = self.kvin_max_hp

        self.refresh_real_hp()

    def heal_submit(self, *args):
        heal_log_text = ''
        if self.input_heal_kvin.text:
            heal_log_text += f'Квин был похилен на {self.input_heal_kvin.text} хп\n'
            self.kvin_hp += int(self.input_heal_kvin.text)
        if self.input_heal_azu.text:
            heal_log_text += f'Азу был похилен на {self.input_heal_azu.text} хп\n'
            self.azu_hp += int(self.input_heal_azu.text)
        if self.input_heal_ari.text:
            heal_log_text += f'Ари была похилен на {self.input_heal_ari.text} хп\n'
            self.ari_hp += int(self.input_heal_ari.text)

        self.heal_log_label.text = heal_log_text
        self.refresh_real_hp()

    def damage_submit(self, *args):
        damage = int(self.input_damage.text)
        d10roll = randint(1, 10)
        if 6 <= d10roll <= 9:
            self.kvin_hp -= damage
            target = kvazar_names[0]
        elif 1 <= d10roll <= 5:
            self.azu_hp -= damage
            target = kvazar_names[1]
        else:
            self.ari_hp -= damage
            target = kvazar_names[2]

        if self.kvin_hp < 0:
            self.azu_hp += self.kvin_hp
            self.kvin_hp = 0
            if self.azu_hp < 0:
                self.ari_hp += self.azu_hp
                self.azu_hp = 0
        elif self.azu_hp < 0:
            self.kvin_hp += self.azu_hp
            self.azu_hp = 0
            if self.kvin_hp < 0:
                self.ari_hp += self.kvin_hp
                self.kvin_hp = 0
        elif self.ari_hp < 0:
            self.azu_hp += self.ari_hp
            self.ari_hp = 0
            if self.ari_hp < 0:
                self.kvin_hp += self.azu_hp
                self.azu_hp = 0

        self.log_hp_label.text = f'По {target} нанесли {damage} урона'

        self.refresh_real_hp()

        if self.ari_hp == 0 and self.azu_hp == 0 and self.kvin_hp == 0:
            self.real_hp_label.text = "YOU PIDOR"
            self.max_hp_label.text = "YOU PIDOR"

    def input_max_hp_changed(self, *args):
        try:
            self.general_max_hp = int(args[1])
            self.azu_max_hp = int(self.general_max_hp / 2)
            self.ari_max_hp = int(self.general_max_hp * 2 / 10)
            self.kvin_max_hp = int(self.general_max_hp - self.ari_max_hp - self.azu_max_hp)

            self.azu_hp = self.azu_max_hp
            self.ari_hp = self.ari_max_hp
            self.kvin_hp = self.kvin_max_hp

        except Exception:
            pass

        self.max_hp_label.text = f'Макс ХП Квазара:\n\nКвин - {self.kvin_max_hp}\n' \
                                 f'Азу - {self.azu_max_hp}\nАри - {self.ari_max_hp}'
        self.refresh_real_hp()

    def build(self):
        layout = BoxLayout(orientation='vertical')
        grid = GridLayout(cols=2)
        heal_grid = GridLayout(cols=3)
        heal_set_btns = BoxLayout(orientation='horizontal')

        grid.add_widget(self.input_max_hp)
        grid.add_widget(self.max_hp_label)

        grid.add_widget(self.input_damage)
        grid.add_widget(self.log_hp_label)
        grid.add_widget(self.damage_submit_btn)
        grid.add_widget(self.real_hp_label)

        heal_grid.add_widget(self.input_heal_kvin)
        heal_grid.add_widget(self.input_heal_azu)
        heal_grid.add_widget(self.input_heal_ari)

        grid.add_widget(heal_grid)

        heal_set_btns.add_widget(self.heal_submit_btn)
        heal_set_btns.add_widget(self.set_hp_btn)

        grid.add_widget(self.heal_log_label)
        grid.add_widget(heal_set_btns)

        grid.add_widget(self.rest_btn)

        layout.add_widget(grid)
        return layout


if __name__ == '__main__':
    MyApp().run()
