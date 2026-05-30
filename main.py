import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# جلب المفاتيح مباشرة من النظام
TELEGRAM_BOT_TOKEN = os.environ.get("8699507145:AAFmNuzqUIIzZc3SnsZcXGTjTV8JbzwYOeI")
GEMINI_API_KEY = os.environ.get("AQ.Ab8RN6KgTes_qHnG2NqPdPwn-G6nIgXxx8coADJINJddv-lXcg")

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ... بقية كود معالجة الرسائل
