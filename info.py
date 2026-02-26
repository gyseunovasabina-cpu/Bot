import random
from telegram import Update
from telegram.ext import ContextTypes

news_list = [
    "Какой сегодня прздник?",
    "Развлечения зимой",
    "Последний новости "
]

offers_list = [
    "Заряжу мотивацией за подписку",
    "Топ 5 семейных фильмов",
    "Поболтаем?"
]


async def handle_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши:\n"
        "news — новости\n"
        "offer — предложения"
    )


async def handle_info_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "news":
        await update.message.reply_text(random.choice(news_list))
    elif text == "offer":
        await update.message.reply_text(random.choice(offers_list))
