#Task3
## a i b - катети, c - гіпотенуза, c - ?
## C - ? a ^ 2 + b ^ 2 = C ^ 2 -> C = (a ^ 2 + b ^2) ^0.5
## S -? a * b / 2

a = int(input("Enter 'a' value: "))
b = int(input("Enter 'b' value: "))

c = (a ** 2 + b ** 2) ** 0.5
s = a * b / 2
print(f'c = {c}, s = {s}')