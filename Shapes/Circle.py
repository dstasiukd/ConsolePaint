from Shapes.Shape import Shape
import math 

class Circle(Shape):
    def __init__(self, x, y, radius, border_char = None, fill_char = None):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.border_char = border_char
        self.fill_char = fill_char

    def get_parameters(self):
        return f"x = {self.x}, y = {self.y}, radius = {self.radius}, border_char = '{self.border_char}, fill_char ='{self.fill_char}'"

    def draw(self, canvas):
        canvas.save_state()
        if 0 > self.x or self.x > canvas.width or 0 > self.y or self.y > canvas.height or 0 > self.radius or self.radius > (canvas.height - self.y) or self.radius > (canvas.width - self.x):
            print("----------INCORRECT INPUT! THE FIGURE SIZE VALUES ARE OUTSIDE THE CANVAS BOUNDARIES!!!----------")
        else:
            for i in range(canvas.height):
                for j in range(canvas.width):
                    distance = math.sqrt((j - self.x) ** 2 + (i - self.y) ** 2)
                    
                    if distance <= self.radius:
                        if abs(distance - self.radius) < 1:
                            canvas.canvas[i][j] = self.border_char if self.border_char else self.char
                        elif self.fill_char:
                            canvas.canvas[i][j] = self.fill_char

    def erase(self, canvas):
        for i in range(canvas.height):
                for j in range(canvas.width):
                    if math.sqrt((j - self.x) ** 2 + (i - self.y) ** 2) <= self.radius:
                        canvas.canvas[i][j] = canvas.background

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def fill(self, canvas, fill_char):
        self.fill_char = fill_char
        for i in range(canvas.height):
            for j in range(canvas.width):
                if math.sqrt((j - self.x) ** 2 + (i - self.y) ** 2) < self.radius:
                    canvas.canvas[i][j] = self.fill_char

