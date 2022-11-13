from func import *

import telebot

bot = telebot.TeleBot(TOKEN)
for val in values_dict.keys(): #создаем текущий список валют
    val_list += '\n' + val

@bot.message_handler(commands=['start', 'help', 'values'])
def help_machine(message):

    if message.text in ['/start', '/help']:
        bot.reply_to(message, str("Для конвертации валют \n"
                                  "используйте следующий запрос:\n"
                                  "валюта1(пробел)валюта2(пробел)количество\n"
                                  "результатом будет эквивалентная сумма в валюте2\n"
                                  "пример запроса:\n"
                                  "доллар рубль 100500\n"
                                  "список валют /values"))
    else:

        bot.reply_to(message, f'Список валют:\n{val_list}')


@bot.message_handler(content_types=['text'])
def service_machine(message):
    input_string = message.text.lower().split()     # прибиваем текст в нижний регистр, удаляем пробелы

    try:
        if len(input_string) != 3:
            raise APIexception('для конвертации необходимо вводить три параметра через пробелы\n'
                               'валюта1 валюта2 количество')

        elif not set(input_string[0:2]).issubset(set(values_dict.keys())):    # создаем множество из валют с ввода,
                                                                              # которые не входят в наш список
                                                                              # потом их выведем в сообщении
            v = ''
            for _ in set(input_string[0:2]).difference(set(values_dict.keys())):
                v += _ + ' '
            raise APIexception(f'валюта {v} у нас не представлена')

        elif input_string[0] == input_string[1]:
            raise APIexception('вводите различные валюты')
        try:
            input_string[2] = float(input_string[2].replace(',', '.'))       # меняем на всякий случай запятые на точки

        except ValueError:       # обрабатываем ошибку конвертации в float
            raise APIexception(f'количество "{input_string[2]}" не обрабатывается')
        if input_string[2] <= 0:
            raise APIexception(f'указывайте, пожалуйста, количество большее, чем ноль')

    except APIexception as user_ex:
        bot.reply_to(message, user_ex)
    except Exception as general_ex: # обрабатываем другие ошибки, которые могут возникнуть не от пользователя
        bot.reply_to(message, f'увы, но что-то не получается((\n{general_ex}')
    else:
        bot.reply_to(message, f'это {Mfn.get_price(*input_string)} {values_dict[input_string[1]]}')


bot.polling(none_stop=True)
