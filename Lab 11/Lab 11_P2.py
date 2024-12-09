class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def __str__(self):
        return f'Rectangle(length={self.length}, width={self.width})'
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
    
length1, width1 = map(int, input().split())
length2, width2 = map(int, input().split())

rectangle1 = Rectangle(length1, width1)
rectangle2 = Rectangle(length2, width2)

print(rectangle1)
print(rectangle2)

print(rectangle1.area())
print(rectangle2.perimeter())

if rectangle1 == rectangle2:
    print("equal")
elif rectangle1 < rectangle2:
    print("smaller")
else:
    print("bigger")