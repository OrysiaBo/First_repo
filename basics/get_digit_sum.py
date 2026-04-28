#Task_7
## 3-Значне число
## знайти суму останньої і передотанньої 
## останньої й першої цифри.

#number = int(input("Enter 3-x number: "))

#print(number % 10)
#print(number // 10 % 10)
#print(number // 100)

## а 5-Значне число?

number = int(input("Enter 5-x number: "))

first_digit = number // 10000 % 10
second_digit = number // 1000 % 10 
third_digit = number // 100 % 10
forth_digit = number // 10 % 10  
fifth_digit = number % 10

print(third_digit + second_digit)
print(third_digit + first_digit)
print(forth_digit + fifth_digit)

