import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import openai

TELEGRAM_TOKEN = os.getenv("8690407504:AAG3CMzfkZOXCiWmQWqQ6VqbWkYumuSJD0Q")
OPENAI_API_KEY = os.getenv("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")

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

