from entertainment import recommend_movie, recommend_activity
from chat import small_talk, tell_joke
from info import show_news, offer_purchase


def main():
    print("Привет! Я бот 🤖")

    while True:
        print("\nВыбери действие:")
        print("1 — Развлечения")
        print("2 — Поболтать")
        print("3 — Новости и предложения")
        print("0 — Выход")

        choice = input("Твой выбор: ")

        if choice == "1":
            mood = input("Какое у тебя настроение? ")
            recommend_movie(mood)

            interest = input("Какой у тебя интерес? ")
            recommend_activity(interest)

        elif choice == "2":
            user_input = input("Напиши сообщение: ")
            if user_input.lower() == "шутка":
                tell_joke()
            else:
                small_talk(user_input)

        elif choice == "3":
            print("1 — Новости")
            print("2 — Предложение покупки")
            sub_choice = input("Выбор: ")

            if sub_choice == "1":
                show_news()
            elif sub_choice == "2":
                offer_purchase()

        elif choice == "0":
            print("Пока! Хорошего дня 😊")
            break

        else:
            print("Не понял выбор, попробуй ещё раз.")


if __name__ == "__main__":
    main()
