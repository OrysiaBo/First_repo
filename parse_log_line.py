import sys

def parse_log_line(line):
    """Парсинг рядка логу в словник."""
    parts = line.split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }

def load_logs(file_path):
    """Завантаження логів з файлу."""
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)

def filter_logs_by_level(logs, level):
    """Фільтрація логів за рівнем логування."""
    return [log for log in logs if log["level"] == level.upper()]

def count_logs_by_level(logs):
    """Підрахунок записів за рівнем логування."""
    levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
    return {level: sum(1 for log in logs if log["level"] == level) for level in levels}

def display_log_counts(counts):
    """Відображення кількості записів для кожного рівня."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")

def display_logs(logs):
    """Відображення відфільтрованих логів."""
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логу.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            display_log_counts(count_logs_by_level(logs))
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            display_logs(filtered_logs)
        else:
            print(f"Логи для рівня '{level.upper()}' не знайдено.")
    else:
        display_log_counts(count_logs_by_level(logs))

if __name__ == "__main__":
    main()
