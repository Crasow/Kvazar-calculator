from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (41 / 255, 43 / 255, 44 / 255, 1)


def get_hp(message):
    general_max_hp = int(message.text)
    azu_hp = int(general_max_hp / 2)
    ari_hp = int(general_max_hp * 2 / 10)
    kvin_hp = int(general_max_hp - ari_hp - azu_hp)

    bot.send_message(user_id, f'Квин - {kvin_hp}\nАзу - {azu_hp}\nАри - {ari_hp}')


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.max_hp_label = Label()
        self.input_max_hp = TextInput(hint_text="Max HP персонажа",
                                      background_color="#3C3F41",
                                      foreground_color="#FFFFFF")
        self.input_max_hp.bind(text=self.input_max_hp_changed)

    def input_max_hp_changed(self, *args):
        kvin_hp = 0
        azu_hp = 0
        ari_hp = 0
        try:
            general_max_hp = int(args[1])
            azu_hp = int(general_max_hp / 2)
            ari_hp = int(general_max_hp * 2 / 10)
            kvin_hp = int(general_max_hp - ari_hp - azu_hp)
        except Exception:
            pass

        self.max_hp_label.text = f'Квин - {kvin_hp}\nАзу - {azu_hp}\nАри - {ari_hp}'

    def build(self):
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(self.input_max_hp)
        layout.add_widget(self.max_hp_label)

        return layout


if __name__ == '__main__':
    MyApp().run()
