import telebot
bot = telebot.TeleBot('5437901418:AAHp-kRBsrOnHPwqP6wmYRnrZ46OPCK8tUc')
@bot.message_handler(commands=["start","старт"])
def start(message):
    bot.send_message(message.chat.id,'Привет!')
bot.polling(none_stop=True)
