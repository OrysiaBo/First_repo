def caching_fibonacci():
    # Створюємо порожній словник для кешування результатів
    cache = {}

    # Внутрішня рекурсивна функція для обчислення чисел Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевіряємо, чи є значення в кеші
        if n in cache:
            return cache[n]
        
        # Обчислюємо значення та зберігаємо його в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Повертаємо обчислене значення
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10)) 
print(fib(15))  
