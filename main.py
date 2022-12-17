import telebot
from telebot import types
from shdow_token import token

bot1 = telebot.TeleBot(token)


@bot1.message_handler(commands=['start'])
def start_message(message):
    bot1.reply_to(message, message.from_user.first_name + ', привет, для начала работы с ботом\
 напиши /commands')


@bot1.message_handler(commands=['commands'])
def commands_message(message):
    bot1.send_message(message.chat.id, "Список команд:\n/start - приветствие + получить список команд\n/buttons - кнопки на панели\n\
/commands - покажет основные команды бота!\nПослушаем музыку?)(в основном для дани)\
 Пиши: 'Предложи музыку'\n")


@bot1.message_handler(commands=['buttons'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)  # row_width=2 - количество столбцов кнопок
    userbtn1 = types.KeyboardButton("Антон")
    userbtn2 = types.KeyboardButton("Даня")
    userbtn3 = types.KeyboardButton("Ярик")
    userbtn4 = types.KeyboardButton("Федя")
    userbtn5 = types.KeyboardButton("Игорь")
    userbtn6 = types.KeyboardButton("Фото Ярика")
    # userbtn7 = types.KeyboardButton("Песня для Феди!")
    userbtn8 = types.KeyboardButton("/commands")

    markup.add(userbtn1, userbtn2, userbtn3, userbtn4, userbtn5, userbtn6, userbtn8)
    bot1.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot1.message_handler(content_types=['text'])
def send_pic(message):
    global file_photo
    global audio
    global audio_dr
    file_photo = open('D:\kosatka.jpg', 'rb')
    audio = open('D:\VG.mp3', 'rb')
    audio_dr = open('D:\s_dr.mp3', 'rb')
    if message.text == "Фото Ярика":
        bot1.send_photo(chat_id=message.from_user.id, photo=file_photo)
        file_photo.close()
    elif message.text == "Антон":
        bot1.send_message(message.chat.id, "Сомнительный тип")
    elif message.text == "Даня":
        bot1.send_message(message.chat.id, "Царь и бог этого мира")
    elif message.text == "Ярик":
        bot1.send_message(message.chat.id, "Косатка")
    elif message.text == "Федя":
        bot1.send_message(message.chat.id, "А все, день рождения кончился, ты лютик семицветик")
    elif message.text == "Игорь":
        bot1.send_message(message.chat.id, "Царь и владыка мира!")
    elif message.text == "Предложи музыку":
        bot1.send_audio(message.chat.id, audio)
        audio.close()
    # elif message.text == "Песня для Феди!":
    #     bot1.send_audio(message.chat.id, audio_dr)
    #     audio.close()


bot1.infinity_polling()
