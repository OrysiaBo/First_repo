def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                # Видаляємо зайві символи (наприклад, новий рядок) та розділяємо по комі
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        # Перше значення - прізвище, друге - зарплата
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Помилка в обробці зарплати в рядку: {line.strip()}")
            
            if count == 0:
                raise ValueError("Файл не містить коректних даних про зарплати.")
            
            average = total / count
            return total, average
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Приклад виклику функції
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
