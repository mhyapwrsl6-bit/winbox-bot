from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8855067562:AAHHwewh76uRKKGOzfTimLnjsHeAqnTgd8I"

CHANNEL_LINK = "https://t.me/chaosdiary_0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 عضویت در کانال", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🎮 به زودی: بازی‌ها", callback_data="games")]
    ]

    await update.message.reply_text(
        "👋 سلام، به WinBox خوش اومدی!\n\n"
        "برای دیدن پست‌های جدید و حمایت از ما، اول عضو کانال Chaos Diary شو. 💙",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
