
import telebot
import json

TOKEN = "5788725455:AAEN2jvuPTV8dds7KcJx17qWhfDZ4TdDDSs"

bot = telebot.TeleBot(TOKEN)



# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, "Здравствуйте!")




# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
   bot.reply_to(message, 'good muse!')


@bot.message_handler(content_types=['photo'])
def handle_pics(message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['text', 'audio'])
def fgfgfgf(message):
    print(message.text)
    bot.send_message(message.chat.id, "Привет, дорогой и любимый "+message.from_user.first_name)


bot.polling(none_stop=True)