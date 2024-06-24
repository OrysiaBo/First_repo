#Знайти суму чисел списку
# 1 + sum([5, 10, 15])
lst = [1, 5, 10, 15]

def ger_sum(numbers: list[int]) -> list[int]:
    print(numbers)
    if not numbers:
        return 0
    
    return numbers[0] + ger_sum(numbers[1:]) #1 +...

print(ger_sum([1, 2]))