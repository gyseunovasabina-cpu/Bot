from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from chat import handle_chat
from recommendations import handle_recommendations
from info import handle_info, handle_info_text

TOKEN = "8478221920:AAGOqSlH7JJZgUx0bIlcJRZMBCEwqt59exI"


async def start(update, context):
    await update.message.reply_text(
        "Привет! \n\n"
        "Команды:\n"
        "/chat — общение\n"
        "/entertainment — фильмы и активности\n"
        "/info — новости и предложения"
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("chat", handle_chat))
    app.add_handler(CommandHandler("entertainment", handle_recommendations))
    app.add_handler(CommandHandler("info", handle_info))

    # Обработка обычного текста
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_chat))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_recommendations))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_info_text))

    app.run_polling()


if __name__ == "__main__":
    main()
