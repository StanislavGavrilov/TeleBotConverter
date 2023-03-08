import telebot
from config import TOKEN,keys
from extensions import CryptoConverter, ConvertionExeption



bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Чтобы начать пользоваться, введите команду в следующем формате:\n" \
           "<из валюты><в валюту><количество>\n" \
           "Пример:\n" \
           "долар рубль 7\n" \
           "долар рубль 7.5\n" \
           "Увидеть список всех валют: /values"

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Неверное количество параметров.')
        qoute, base, amount = values
        total_base=float(CryptoConverter.convert(qoute,base,amount))
        end_amount=float(amount)
        end_base = total_base * end_amount
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:


        text=f'Цена {amount} {qoute} в {base} = {end_base} '
        bot.send_message(message.chat.id,text)


bot.polling()
