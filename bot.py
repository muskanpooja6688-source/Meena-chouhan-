import telebot

TOKEN = "8690407504:AAG3CMzfkZOXCiWmQWqQ6VqbWkYumuSJD0Q"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Welcome ❤️\nGirls Chat / Video Call available")

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if "name" in text:
        bot.send_message(message.chat.id,"Mera name Meena Chouhan hai 😊")

    elif "age" in text:
        bot.send_message(message.chat.id,"Meri age 23 hai ❤️")

    elif "address" in text or "kaha se" in text:
        bot.send_message(message.chat.id,"Main Ajmer se hu 😊")

    elif "video call" in text:
        bot.send_photo(message.chat.id, open("qr.png","rb"), "Payment karo fir video call milega 💰")

    elif "chat" in text:
        bot.send_message(message.chat.id,"Girls chat ke liye payment karo ❤️")

bot.polling()
