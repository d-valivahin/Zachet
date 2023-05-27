import math
from math import sin, cos, radians
x = float(input("Введите х: "))
def calcut(c):
    if c == None: c = False
    elif c < 0.1:
        c = (c**0.5)*(c**2)
    else:
        c = math.sin(math.radians(c)) + math.cos(math.radians(c))
    return (c)
print(calcut(x))