import telebot
from telebot import types
import webbrowser


bot = telebot.TeleBot('6101511461:AAEUW9exztaQUI47pWDrUOstTSc5sdMTInk')
                       
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/AnimatedSticker.tgs', 'rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    
    but0 = types.KeyboardButton('Социальные сети')
    but1 = types.KeyboardButton('Удалить фото')
    but2 = types.KeyboardButton('Изменить фото')
    
    markup.row(but0)
    markup.add(but1, but2)
    
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}', reply_markup = markup)
     
@bot.message_handler(content_types='photo')#обработка медиа файлов фото видео аудио
def getPhoto(message):
    markup = types.InlineKeyboardMarkup()
    
    but0 = types.InlineKeyboardButton('Перейти на сайт', url = "https://vk.com/amazingcode")
    but1 = types.InlineKeyboardButton('Удалить фото', callback_data= "delete")
    but2 = types.InlineKeyboardButton('Изменить', callback_data= "edit")
    
    markup.row(but0)
    markup.add(but1, but2)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup = markup)#ответ на сообщение
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
        
@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text.lower() == 'перейти на сайт':
        webbrowser.open('https://vk.com/amazingcode')
    
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Фотография удаленна')
    
    elif message.text == 'Социальные сети':
        markup = types.InlineKeyboardMarkup()
    
        but = types.InlineKeyboardButton('Перейти на сайт', url = "https://vk.com/amazingcode")
    
        markup.add(but)
        bot.send_message(message.chat.id, 'Посетите нашу группу в вк', reply_markup= markup) 
        
    elif message.text == 'Изменить фото':
        bot.send_message(message.chat.id, 'Вы ещё не выгрузили фото')

bot.polling(none_stop=True)