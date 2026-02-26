import random
from telegram import Update
from telegram.ext import ContextTypes


class Recommendations:

    happy_movie_list = ["Один дома", "Маска", "День сурка"]
    sad_movie_list = ["Зелёная миля", "Побег из Шоушенка", "Хатико"]
    neutral_movie_list = ["Интерстеллар", "Начало", "Паразиты"]

    eat_activity_list = ["Сходить в пиццерию", "Приготовить пасту", "Сделать смузи"]
    sport_activity_list = ["Пробежка", "Йога", "Велосипед"]
    trip_activity_list = ["Поездка за город", "Пикник у озера", "Поход в горы"]

    def recommend_movie(self, mood):
        if mood == "happy":
            return random.choice(self.happy_movie_list)
        elif mood == "sad":
            return random.choice(self.sad_movie_list)
        elif mood == "neutral":
            return random.choice(self.neutral_movie_list)
        return None

    def recommend_activity(self, interest):
        if interest == "eat":
            return random.choice(self.eat_activity_list)
        elif interest == "sport":
            return random.choice(self.sport_activity_list)
        elif interest == "trip":
            return random.choice(self.trip_activity_list)
        return None


recommendation = Recommendations()


async def handle_entertainment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Фильмы
    if text in ["happy", "sad", "neutral"]:
        movie = recommendation.recommend_movie(text)
        await update.message.reply_text(f"🎬 Рекомендую: {movie}")

    # Активности
    elif text in ["eat", "sport", "trip"]:
        activity = recommendation.recommend_activity(text)
        await update.message.reply_text(f"🎯 Попробуй: {activity}")

    else:
        await update.message.reply_text(
            "Напиши:\n"
            "happy / sad / neutral — фильм\n"
            "eat / sport / trip — активность"
        )


def handle_recommendations():
    return None