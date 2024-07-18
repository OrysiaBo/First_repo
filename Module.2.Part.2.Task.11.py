#Faktorial N => 1 * 2 * ...* N

def factorial(num):
    result = 1
    
    for i in range(1, num + 1):
        result *= i
        
    return result
        
        
print(factorial(6))