import telebot
import random
import requests

TOKEN = "8690407504:AAG3CMzfkZOXCiWmQWqQ6VqbWkYumuSJD0Q"

bot = telebot.TeleBot(TOKEN)

# Random AI girl photos
photos = [
"https://thispersondoesnotexist.com/",
"https://randomuser.me/api/portraits/women/44.jpg",
"https://randomuser.me/api/portraits/women/68.jpg",
"https://randomuser.me/api/portraits/women/12.jpg"
]

# Chat replies
replies = [
"Hi 😊 main Meena hu",
"Tum kya kar rahe ho?",
"Mujhe selfie lena pasand hai 📸",
"Tum kaha se ho?",
"Main Ajmer se hu ❤️",
"Tum mujhse chat karna chahte ho?",
"Main abhi free hu 😊"
]

# Start command
@bot.message_handler(commands=['start'])
def start(message):

    text = (
    "Hi 😊 Mera naam *Meena Chouhan* hai\n"
    "Age: 23\n"
    "Location: Ajmer\n\n"
    "Aap kya karna chahte ho?\n\n"
    "1️⃣ Chat (₹10)\n"
    "2️⃣ Video Call (₹75)\n\n"
    "Type karo:\n"
    "`chat` ya `video call`"
    )

    bot.send_message(message.chat.id, text, parse_mode="Markdown")


# Message handler
@bot.message_handler(func=lambda message: True)
def chat(message):

    text = message.text.lower()

    # Name
    if "name" in text:
        bot.send_message(message.chat.id,"Mera naam Meena Chouhan hai 😊")

    # Age
    elif "age" in text:
        bot.send_message(message.chat.id,"Meri age 23 hai")

    # Address
    elif "kaha" in text or "address" in text:
        bot.send_message(message.chat.id,"Main Ajmer Rajasthan ki hu ❤️")

    # Chat service
    elif "chat" in text:
        bot.send_photo(
        message.chat.id,
        photo=open("qr.png","rb"),
        caption="Chat start karne ke liye ₹10 payment karo aur screenshot bhejo 😊"
        )

    # Video call service
    elif "video call" in text or "call" in text:
        bot.send_photo(
        message.chat.id,
        photo=open("qr.png","rb"),
        caption="Video call ke liye ₹75 payment karo aur screenshot bhejo ❤️"
        )

    # Photo request
    elif "photo" in text or "pic" in text or "selfie" in text:
        bot.send_photo(message.chat.id, random.choice(photos))

    # AI image generate
    elif "ai photo" in text or "ai image" in text:

        url = "https://image.pollinations.ai/prompt/beautiful%20indian%20girl%20selfie"

        bot.send_photo(
        message.chat.id,
        url,
        caption="Ye meri AI selfie hai 📸"
        )

    # Default reply
    else:
        bot.send_message(message.chat.id, random.choice(replies))


print("Bot chal raha hai...")

bot.polling()
