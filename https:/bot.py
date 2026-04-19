import telebot
from telebot import types
import database
import worker
import os

# بياناتك السرية مباشرة هنا
BOT_TOKEN = "8418697197:AAFBoWrnxpyeaJ5d6NI754uglyb-33_WOEM"
ADMIN_ID = 524843160 # الآيدي الخاص بك

bot = telebot.TeleBot(BOT_TOKEN)
database.init_db()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("📸 Instagram", callback_data="plat_insta")
    btn2 = types.InlineKeyboardButton("🎬 TikTok", callback_data="plat_tiktok")
    btn3 = types.InlineKeyboardButton("💎 Telegram", callback_data="plat_tg")
    btn4 = types.InlineKeyboardButton("🔵 Facebook", callback_data="plat_fb")
    btn5 = types.InlineKeyboardButton("💰 محفظتي", callback_data="wallet")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    balance = database.get_balance(message.from_user.id)
    bot.reply_to(message, f"🛡️ أهلاً بك في بوت البلاغات.\n💰 رصيدك الحالي: {balance}$", reply_markup=markup)

# أمر إضافة الرصيد للأدمن
@bot.message_handler(commands=['add'])
def add_balance(message):
    if message.from_user.id == ADMIN_ID:
        try:
            parts = message.text.split()
            target_id = int(parts[1])
            amount = float(parts[2])
            database.update_balance(target_id, amount)
            bot.reply_to(message, f"✅ تم إضافة {amount}$ للمستخدم {target_id}")
        except:
            bot.reply_to(message, "⚠️ الصيغة: /add user_id 50")

bot.polling()
