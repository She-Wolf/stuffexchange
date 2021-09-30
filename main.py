import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Добавить вещь', 'Найти вещь')
    bot.send_message(message.chat.id, '''Привет! 
    Я помогу тебе обменять что-то ненужное на очень нужное.
    Чтобы разместить вещь к обмену нажми - “Добавить вещь”. После этого тебе станут доступны вещи других пользователей.
    Нажми “Найти вещь” и я пришлю тебе фотографии вещей для обмена. Понравилась вещь - пиши “Обменяться”, нет - снова нажимай “Найти вещь”.
    Нажал “Обменяться”? - если владельцу вещи понравится что-то из твоих вещей, то я пришлю контакты вам обоим.''', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def reply_all_message(message):
    if message.text == 'Добавить вещь':
        bot.send_message(message.chat.id, 'Введи название вещи')
    elif message.text == 'Найти вещь':
        exchange_item()
#         img = open('sn.jpg', 'rb')
#         bot.send_photo(message.chat.id, img, 'Кроссовки', reply_markup=keyboard)
    else:
        print(f'Упаковываем вещь {message.text} в список юзера {message.chat.username}')

       

def exchange_item(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('Хочу эту вещь!', callback_data='exchange-item'),
        telebot.types.InlineKeyboardButton('Пропустить', callback_data='next')
    )  
  
    bot.send_message(  
        message.chat.id,   
        'Вы хотите обменяться на этот предмет или смотрим дальше?',  
        reply_markup=keyboard  
    )

if __name__ == '__main__':
     bot.infinity_polling()
