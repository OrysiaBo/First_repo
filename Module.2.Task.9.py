a = "10"
b = "0"

try:
    a = int(a)
    b = int(b)
    print(a/ b)
except ValueError:
    print("Invalid integers")
except ZeroDivisionError:
    print("Div by 0 is not allowed")