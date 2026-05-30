import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# --- إعدادات المفاتيح (تم دمجها للتجربة السريعة) ---
TELEGRAM_BOT_TOKEN = "8699507145:AAFmNuzqUIIzZc3SnsZcXGTjTV8JbzwYOeI"
GEMINI_API_KEY = "ضع_مفتاح_جيمناي_هنا"
# -----------------------------------------------

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = model.generate_content(user_text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="عذراً، حدث خطأ في النظام.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Dragon Engine is running...")
    application.run_polling()

