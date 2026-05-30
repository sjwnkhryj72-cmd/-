import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# 1. تحميل المفاتيح من ملف .env (الخزنة السرية)
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. دالة الرد الذكي
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        # طلب الرد من Gemini
        response = model.generate_content(user_text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="عذراً، حدث خطأ في معالجة الطلب.")

if __name__ == '__main__':
    # 4. تشغيل البوت باستخدام التوكن المستخرج من .env
    if not TELEGRAM_BOT_TOKEN:
        print("خطأ: لم يتم العثور على TELEGRAM_BOT_TOKEN في ملف .env")
    else:
        application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        print("Dragon Engine is running...")
        application.run_polling()
