import telebot

bot = telebot.TeleBot('6049769264:AAFZgB6XuTYXX-1in6O4RtZ6WVN3qStpPpk')

print('Bot started')

user_id = ''


@bot.message_handler(commands=['start', 'help'])
def start(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, 'Бот  запущен. Укажи скок хп у персонажа.')
    bot.register_next_step_handler(message, get_hp)  # следующий шаг – функция get_name


def get_hp(message):
    general_hp = int(message.text)
    azu_hp = int(general_hp / 2)
    ari_hp = int(general_hp * 2 / 10)
    kvin_hp = int(general_hp - ari_hp - azu_hp)

    bot.send_message(user_id, f'Квин - {kvin_hp}\nАзу - {azu_hp}\nАри - {ari_hp}')


bot.polling(none_stop=True, interval=0)
