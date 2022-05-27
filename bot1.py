import requests
from datetime import datetime
import telebot
# from Token import TOKEN 

def telegram_bot(token): # Бот
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"]) # Приветсвие пользователя
    def start_message(message):
        bot.send_message(message.chat.id, "Привет! Для того, чтобы узнать цену битка напиши 'цена битка'")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "цена битка": # Вывод цены битка
            try:   # Пробуем вывести цену
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd") # Обычный парсинг
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n Цена битка: {sell_price}"
                )
            except Exception as ex: # Вывод ошибки
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то пошло нет так, попробуй заново написать 'цена'"
                )
        else:
            bot.send_message(message.chat.id, "Хммм, чет ты не то написал)) Проверь")

    bot.polling()


if __name__ == '__main__': # Вызов функции
    telegram_bot(TOKEN)