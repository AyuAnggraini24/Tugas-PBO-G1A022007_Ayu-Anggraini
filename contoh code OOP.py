class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
my_rectangle = Rectangle(4, 5)
print(my_rectangle.area()) # output: 20
print(my_rectangle.perimeter()) # output: 18

