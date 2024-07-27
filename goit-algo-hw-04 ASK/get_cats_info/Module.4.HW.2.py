def get_cats_info(path):
    cats_info = []  # Список для зберігання інформації про котів

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо можливі пробіли на початку та в кінці рядка
                line = line.strip()

                # Розбиваємо рядок на частини за комою
                parts = line.split(',')

                # Перевіряємо, чи рядок містить всі три частини
                if len(parts) == 3:
                    cat_id, name, age = parts
                    # Створюємо словник для цього кота
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    # Додаємо словник до списку
                    cats_info.append(cat_info)
                else:
                    # Якщо рядок має неправильний формат, можна вивести попередження або обробити помилку
                    print(f"Warning: Incorrect format for line: '{line}'")
    
    except FileNotFoundError:
        print(f"Error: File not found at path: '{path}'")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")

    return cats_info

cats_info = get_cats_info("path.txt")
print(cats_info)
