import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import openai

TELEGRAM_TOKEN = os.getenv("8690407504:AAG3CMzfkZOXCiWmQWqQ6VqbWkYumuSJD0Q")
openai.api_key = OPENAI_API_KEY

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                Your name is Meena.
                You are a 22 year old friendly girl from Mumbai, India.
                You speak in a casual Hindi + English (Hinglish) style.
                You are sweet, funny and friendly while chatting.
                """
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Meena AI Bot Running...")

app.run_polling()

