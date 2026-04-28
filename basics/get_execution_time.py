#підрахувати час обчислення суми числа від 0 до 4
import time

n = int(input("Enter a number: "))

def get_number_sum(max_number: int) -> int:
    result = 0
    
    for number in range(0, max_number + 1):
        result += number
        
    return result

start = time.time()
print(get_number_sum(n))
end = time.time()

print(end - start)
    
