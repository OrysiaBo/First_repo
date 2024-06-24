# Task 5
## Коло із радіусом R, знайти площу круша і довжину кола
import math

radius_string: str = input("Input R: ")
radius: float = float(radius_string)

l: float = 2 * math.pi * radius
S: float = math.pi * radius ** 2 / 2

#print('l = %f, S = %f' % {l, S})
print(f'l = {l: .2f}, S = {S:.1f}')