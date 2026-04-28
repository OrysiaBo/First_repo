age = input("Your age: ")

try:
    age = int(age)

    if age >= 18:
    print("access allowed")
    else:
    print("access denied")
except ValueError:
    print(f"{age} is not a number. Please write a number!")    
