import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# تحميل المتغيرات من "Variables" في Railway
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
# استخدام نموذج Flash للسرعة والأداء العالي
model = genai.GenerativeModel('gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        # إرسال الرسالة إلى Gemini وانتظار الرد
        response = model.generate_content(user_text)
        # إرسال الرد للمستخدم
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    except Exception as e:
        # في حال حدوث خطأ، نرسل رسالة واضحة
        await context.bot.send_message(chat_id=update.effective_chat.id, text="حدث خطأ في معالجة طلبك، الرجاء المحاولة لاحقاً.")

if __name__ == '__main__':
    print("Starting Dragon Engine...")
    
    # التحقق من وجود التوكن
    if not TELEGRAM_BOT_TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN is missing!")
    else:
        application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        
        # إضافة المعالج
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        
        print("Dragon Engine is running...")
        application.run_polling()
