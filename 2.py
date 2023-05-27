import math, unittest
from math import sin, cos, radians
#x = float(input("Введите х: "))
def calcut(c):
    if c == None: c = False
    elif c < 0.1:
        c = (c**0.5)*(c**2)
    else:
        c = math.sin(math.radians(c)) + math.cos(math.radians(c))
    return (c)
#m = calcut(x)

class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(calcut(5), 1.0833504408394037)
    def test_2(self):
        self.assertEqual(calcut(0.01), 1e-05)
    def test_3(self):
        self.assertFalse(calcut(None), False)
