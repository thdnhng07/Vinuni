from math import sqrt
from math import pi

def calculate_rectangle(a, b):

    area = a * b
    perimeter = (a + b) * 2

    return area, perimeter

def calculate_circle(a):

    area = pi * (a ** 2)
    permeter= 2 * pi * a

    return area, permeter

def calculate_triangle(a, b, c):

    s = (a + b + c) / 2

    area = sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c

    return area, perimeter