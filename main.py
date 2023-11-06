import telebot
import random
import config
import time


#создание бота
token  = config.bot_token
bot=telebot.TeleBot(token)

greetings = ["Привет!", "Здравствуй!", "Вуссап!", "Ку!", "Хеллоу!"]

blocked_users = {}

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет я ВЧН-бот, здесь ты найдешь всё что тебе нужно")



@bot.message_handler(commands=['hello'])
def handle_hello(message):
    chat_id = message.chat.id
    random_greeting = random.choice(greetings)
    bot.send_message(chat_id, random_greeting)


@bot.message_handler(commands=['info'])
def inf(message):
    bot.send_message(message.chat.id, 'Привет, во мне есть такие-то функции и еще я дополниетльно умею это')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    emoj = random.choice(['выглядит хорошо', 'ну такое'])
    bot.send_message(message.chat.id, f"Спасибо за фото! Я получил вашу фотографию, {emoj}")


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(func=lambda message: message.text is not None)
def handle_message(message):
    user_id = message.from_user.id
    text = message.text.lower()
    
    if "админ дурак" in text or "админ козёл" in text:
        if user_id not in blocked_users or (time.time() - blocked_users[user_id]) >= 10:
            bot.send_message(user_id, "Вы были заблокированы на 10 секунд за оскорбление. Пожалуйста, уважайте других.")
            blocked_users[user_id] = time.time()
            bot.leave_chat(user_id)  # Бот покидает чат с пользователем
            time.sleep(10)  # Подождать 10 секунд
            bot.join_chat(user_id)  # Бот возвращается в чат
            bot.send_message(user_id, "Вы были разблокированы и можете продолжить общение.")
            
            

bot.infinity_polling()




