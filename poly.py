class Shape:
    def __init__(self,color,is_filled):
        self.color = color;
        self.is_filled = is_filled;
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}");
class Circle(Shape):
        
        def __init__(self,radius,color,is_filled):
            super().__init__(color,is_filled);
            self.radius = radius;
        def describe(self):
            super().describe();
            print(f"It's area is: {3.14 * self.radius ** 2} cm² ")
class Square(Shape):
    def __init__(self,color,is_filled,side):
            super().__init__(color,is_filled);
            self.side = side;

class Triangle(Shape):
    def __init__(self,width,height,color,is_filled):
            super().__init__(color,is_filled);
            self.width = width;
            self.height = height;

circle=Circle(5,"red", True);

print("This is a circle.");
circle.describe();



