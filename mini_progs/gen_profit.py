import re

def generator_numbers(text):
    # Знаходимо всі числа в тексті
    pattern = r'\b\d+\.\d+\b|\b\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text, func):
    # Підсумовуємо всі знайдені числа
    return sum(func(text))

# Приклад використання
text = """
Загальний дохід працівника складається з декількох частин: 
/1000.01 як основний дохід, доповнений додатковими надходженнями 
/27.45 і 324.00 доларів.
"""
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")




