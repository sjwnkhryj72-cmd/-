import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# ضع المفاتيح هنا مباشرة وبدون أي تردد (هذا للتجربة فقط)
TELEGRAM_BOT_TOKEN = "8699507145:AAFmNuzqUllzZc3SnsZcXGTjTV8JbzwYOel"
GEMINI_API_KEY = "AQ.Ab8RN6IgyecQXGyioTukzh7doiC5cKKdI6WHae_K0FHN9C1atA" 

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = model.generate_content(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="خطأ في الاتصال.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.run_polling()
