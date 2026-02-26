import random 

class Recommendations:

    happy_movie_list = ["Один дома", "Маска", "Трудный ребёнок", "День сурка", "Мальчишник в Вегасе"]
    sad_movie_list = ["Зелёная миля", "Побег из Шоушенка", "Список Шиндлера", "Хатико", "До встречи с тобой"]
    neutral_movie_list = ["Интерстеллар", "Начало", "Остров проклятых", "Паразиты", "Довод"]
    eat_activity_list = ["Сходить в пиццерию", "Приготовить пасту", "Устроить бранч", "Сходить на фуд-корт", "Сделать смузи и перекус"]
    sport_activity_list = ["Пробежка в парке", "Йога", "Плавание", "Велосипед", "Теннис"]
    trip_activity_list = ["Поездка за город", "Пешая прогулка по центру", "Пикник у озера", "Однодневный тур в соседний город", "Поход в горы"]

    def recommend_movie(self, mood):
        if mood == "happy":
            movie = random.choice(self.happy_movie_list)
        elif mood == "sad":
            movie = random.choice(self.sad_movie_list)
        elif mood == "neutral":
            movie = random.choice(self.neutral_movie_list)
        else:
            movie = None 
        return movie 

    def recommend_activity(self, interest):
        if interest == "eat":
            activity = random.choice(self.eat_activity_list)
        elif interest == "sport":
            activity = random.choice(self.sport_activity_list)
        elif interest == "trip":
            activity = random.choice(self.trip_activity_list)
        else:
            activity = None 
        return activity