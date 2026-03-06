import telebot

TOKEN = "8690407504:AAG3CMzfkZOXCiWmQWqQ6VqbWkYumuSJD0Q"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    "Hi 😊 Mera naam Meena Chouhan hai.\n"
    "Age: 23\n"
    "Address: Ajmer\n\n"
    "Aap kya karna chahte ho?\n"
    "1️⃣ Chat (₹10)\n"
    "2️⃣ Video Call (₹75)\n\n"
    "Type karo: chat ya video call")

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if "name" in text:
        bot.send_message(message.chat.id, "Mera naam Meena Chouhan hai 😊")

    elif "age" in text:
        bot.send_message(message.chat.id, "Meri age 23 hai")

    elif "address" in text or "kaha" in text:
        bot.send_message(message.chat.id, "Main Ajmer ki hu")

    elif "chat" in text:
        bot.send_photo(
            message.chat.id,
            photo=open('qr.png','rb'),
            caption="Chat start karne ke liye ₹10 payment karo aur screenshot bhejo 😊"
        )

    elif "video call" in text or "call" in text:
        bot.send_photo(
            message.chat.id,
            photo=open('qr.png','rb'),
            caption="Video call ke liye ₹75 payment karo aur screenshot bhejo 💕"
        )

    else:
        bot.send_message(message.chat.id,
        "Aap kya karna chahte ho?\n"
        "Chat ₹10\n"
        "Video Call ₹75")

bot.polling()
