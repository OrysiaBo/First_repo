#Створити функціюб що поверне список квадратів чисел

lst = [1, 5, 10, 100]
lst_2 = [3, 89, 56]

def get_squeres(numbers: list[int]) -> list[int]:
    result = []
    
    for number in numbers:
        result.append(number ** 2)
        
    return result
    

print(get_squeres(lst))
print(get_squeres(lst_2))
