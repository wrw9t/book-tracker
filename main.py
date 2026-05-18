import json
import os

FILENAME = "books.json"

def load_books():
    """Загрузка данных из JSON-файла"""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    """Сохранение данных в JSON-файл"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def main():
    while True:
        print("\n--- Меню Трекера Книг ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("Выберите пункт меню (1-6): ").strip()
        
        if choice == "1":
            print("[Заглушка] Тут будет добавление книги...")
        elif choice == "2":
            print("[Заглушка] Тут будет вывод всех книг...")
        elif choice == "3":
            print("[Заглушка] Тут будет расчет средней оценки...")
        elif choice == "4":
            print("[Заглушка] Тут будет статистика по авторам...")
        elif choice == "5":
            print("[Заглушка] Тут будет удаление книги...")
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 6.")

if __name__ == "__main__":
    main()