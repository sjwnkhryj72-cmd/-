import os
from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# استخدام GROQ_API_KEY الذي وضعناه
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": update.message.text}],
            model="llama3-8b-8192",
        )
        reply = chat_completion.choices[0].message.content
        await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="حدث خطأ، تأكد من إعدادات البوت.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ.get("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
