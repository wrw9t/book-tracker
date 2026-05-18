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

def delete_book():
    """Удаление книги по её индексу (Пункт меню 5)"""
    books = load_books()
    if not books:
        print("\nСписок книг пуст. Удалять нечего.")
        return
        
    print("\n--- Доступные для удаления книги ---")
    for idx, book in enumerate(books, 1):
         print(f"{idx}. {book['author']} — «{book['title']}»")
         
    while True:
        try:
            choice = int(input("\nВведите номер книги для удаления (или 0 для отмены): "))
            if choice == 0:
                print("Удаление отменено.")
                return
            if 1 <= choice <= len(books):
                removed = books.pop(choice - 1)
                save_books(books)
                print(f"\n[Успех] Книга '{removed['title']}' успешно удалена!")
                break
            print("Ошибка: Неверный номер. Выберите индекс из списка.")
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")

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
            delete_book()  # Вызов функции удаления
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 6.")

if __name__ == "__main__":
    main()