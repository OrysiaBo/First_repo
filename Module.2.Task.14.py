#Створити функціюб яка повертає функціюб що рахує кількість своїх викликів

1 usage
def get_counter():
    count_value = 0
    
    def counter():
        nonlocal count_value
        count_value = count_value + 1
        return count_value
    
    return counter

a = get_counter()
print(a())
