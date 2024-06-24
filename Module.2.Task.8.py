#Обчислити ділення числа а на в, зчитавши із консолі

try:
    a = (int(input("Enter a: ")))
    b = (int(input("Enter b: ")))
except ValueError as exc:
    print("Invalid number")
else: 
    try:
        print(a/ b)
    except Exception:
        print("Division by 0 is not allowed")


