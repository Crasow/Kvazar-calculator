from kivy.app import App  # Kivy imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.config import Config

# Functional imports
from random import randint

# My custom imports
from CoboldCls import Cobold
from KvazarCls import Kvazar

Window.clearcolor = (41 / 255, 43 / 255, 44 / 255, 1)

# Window.size = (324, 648)


kvin = Cobold("Квин", range(6, 10))
azu = Cobold("Азу", range(1, 6))
ari = Cobold("Ари", range(10, 11))
Kvazar = Kvazar(kvin, azu, ari)

if __name__ == '__main__':
    class KvazarApp(App):
        def __init__(self):
            # TODO: Сделать настройки с : установкой хп по значению
            # TODO: Сделать настройки с : сменой веоятности попадания
            # TODO: Сделать таблицу навыков и таллантов
            super().__init__()
            # -----------------------------------------------------------------------

            self.max_hp_label = Label(text="Макс ХП Квазара:")
            self.input_max_hp = TextInput(hint_text="Макс HP персонажа",
                                          background_color="#3C3F41",
                                          foreground_color="#FFFFFF")
            self.input_max_hp.bind(text=self.input_max_hp_changed)

            self.input_damage = TextInput(hint_text="Урон",
                                          background_color="#3C3F41",
                                          foreground_color="#FFFFFF")
            self.get_damage_label = Label()
            self.damage_submit_btn = Button(on_press=self.damage_submit, background_normal="imgs/damage.png")
            self.current_hp_label = Label(text="Текущие ХП Квазара:")

            self.heal_submit_btn = Button(on_press=self.heal_submit, background_normal="imgs/heal.png")
            self.heal_log_label = Label()
            self.input_heal_kvin = TextInput(hint_text=f"Хил {kvin.name}",
                                             background_color="#3C3F41",
                                             foreground_color="#FFFFFF")
            self.input_heal_azu = TextInput(hint_text=f"Хил {azu.name}",
                                            background_color="#3C3F41",
                                            foreground_color="#FFFFFF")
            self.input_heal_ari = TextInput(hint_text=f"Хил {ari.name}",
                                            background_color="#3C3F41",
                                            foreground_color="#FFFFFF")
            self.rest_btn = Button(on_press=self.rest_btn_pressed, background_normal="imgs/rest.png")
            self.set_hp_btn = Button(text="Установить", on_press=self.set_hp)

        def refresh_current_hp(self):
            self.current_hp_label.text = f'Текущие ХП Квазара:\n\nКвин - {kvin.hp}\n' \
                                         f'Азу - {azu.hp}\nАри - {ari.hp}'

        def set_hp(self, *args):
            if self.input_heal_kvin.text:
                Kvazar.set_hp(kvin, int(self.input_heal_kvin.text))
            if self.input_heal_azu.text:
                Kvazar.set_hp(azu, int(self.input_heal_azu.text))
            if self.input_heal_ari.text:
                Kvazar.set_hp(ari, int(self.input_heal_ari.text))

            self.refresh_current_hp()

        def rest_btn_pressed(self, *args):
            Kvazar.rest()

            self.refresh_current_hp()

        def heal_submit(self, *args):
            heal_log_text = ''
            if self.input_heal_kvin.text:
                heal_log_text += Kvazar.get_heal(kvin, int(self.input_heal_kvin.text))
            if self.input_heal_azu.text:
                heal_log_text += Kvazar.get_heal(kvin, int(self.input_heal_kvin.text))
            if self.input_heal_ari.text:
                heal_log_text += Kvazar.get_heal(kvin, int(self.input_heal_kvin.text))

            self.heal_log_label.text = heal_log_text
            self.refresh_current_hp()

        def damage_submit(self, *args):
            damage = int(self.input_damage.text)
            targets = Kvazar.get_damage(damage)
            damage_text = ''
            for target in targets:
                damage_text += f'По {target.name} нанесли {target.damage_taken} урона\n'

            self.get_damage_label.text = damage_text
            
            self.refresh_current_hp()

            if ari.hp <= 0 and kvin.hp <= 0 and azu.hp <= 0:
                # TODO: сделать мемный экран смерти
                self.current_hp_label.text = "YOU PIDOR"
                self.max_hp_label.text = "YOU PIDOR"

        def input_max_hp_changed(self, *args):
            try:
                Kvazar.set_max_hp(self.input_max_hp.text)
            except Exception:
                pass

            self.max_hp_label.text = f'Макс ХП Квазара:\n\n' \
                                     f'Квин - {kvin.max_hp}\n' \
                                     f'Азу - {azu.max_hp}\n' \
                                     f'Ари - {ari.max_hp}'
            self.refresh_current_hp()

        def build(self):
            layout = BoxLayout(orientation='vertical')
            grid = GridLayout(cols=2)
            heal_grid = GridLayout(cols=3)
            heal_set_btns = BoxLayout(orientation='horizontal')

            grid.add_widget(self.input_max_hp)
            grid.add_widget(self.max_hp_label)

            grid.add_widget(self.input_damage)
            grid.add_widget(self.get_damage_label)
            grid.add_widget(self.damage_submit_btn)
            grid.add_widget(self.current_hp_label)

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


    KvazarApp().run()
