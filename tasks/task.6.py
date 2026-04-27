# Task 6
## Зчитанти числа із консолі (через кому)  і вивести суму

numbers_string: str = input("Enter numbers: ")
numbers_list: list[int] = numbers_string.split(',')
int_numbers: list[int] = list(map(int, numbers_list))

print(numbers_string)
print(numbers_list)
print(int_numbers)
print(sum(int_numbers))
