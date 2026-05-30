import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# تحميل المتغيرات (سيعمل على جهازك وعلى Railway)
# نقوم بجلبها مباشرة من نظام التشغيل
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        # إذا لم يكن المفتاح موجوداً، سيظهر خطأ هنا
        response = model.generate_content(user_text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    except Exception as e:
        # لنعرف ما هو الخطأ الحقيقي، سأجعله يطبع الخطأ في الـ Logs في Railway
        print(f"Error details: {e}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="عذراً، تعذر الاتصال بـ Gemini.")
