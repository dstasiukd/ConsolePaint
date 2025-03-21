import math
from Shapes.Shape import Shape

class Triangle(Shape):
    def __init__(self, x1, y1, a, b, c, border_char = None, fill_char = None):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.a = a
        self.b = b
        self.c = c
        self.border_char = border_char
        self.fill_char = fill_char

        self.x2 = self.x1 + a  
        self.y2 = self.y1
        self.x3 = None
        self.y3 = None

        self.calc_third_point()  

    def is_valid_triangle(self):
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)
    
    def calc_third_point(self):
        if not self.is_valid_triangle():
            print("ERROR! The given sides do not form a valid triangle!")
            return False
        
        
        angle = math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))

        
        self.x3 = self.x1 + int(self.b * math.cos(angle))
        self.y3 = self.y1 - int(self.b * math.sin(angle))  
        
        return True
    
    def draw_line(self, canvas, x1, y1, x2, y2):
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        sx, sy = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
        err = dx - dy

        while True:
            if 0 <= x1 < canvas.width and 0 <= y1 < canvas.height:
                canvas.canvas[y1][x1] = self.border_char
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def draw(self, canvas):
        canvas.save_state()
        if not self.calc_third_point():
            return
        
        self.draw_line(canvas, self.x1, self.y1, self.x2, self.y2)
        self.draw_line(canvas, self.x2, self.y2, self.x3, self.y3)
        self.draw_line(canvas, self.x3, self.y3, self.x1, self.y1)

        if self.fill_char:
            self.fill(canvas)  

    def fill(self, canvas, fill_char):
        if not self.calc_third_point():
            return
        
        self.fill_char = fill_char
        
        min_y = min(self.y1, self.y2, self.y3)
        max_y = max(self.y1, self.y2, self.y3)

        for y in range(min_y, max_y + 1):
            intersections = []
            for (x1, y1, x2, y2) in [(self.x1, self.y1, self.x2, self.y2), 
                                     (self.x2, self.y2, self.x3, self.y3), 
                                     (self.x3, self.y3, self.x1, self.y1)]:
                if y1 != y2:  
                    if min(y1, y2) <= y <= max(y1, y2):
                        x = int(x1 + (y - y1) * (x2 - x1) / (y2 - y1))
                        intersections.append(x)
            
            if len(intersections) == 2:
                x_min, x_max = sorted(intersections)
                for x in range(x_min, x_max + 1):
                    if 0 <= x < canvas.width and 0 <= y < canvas.height:
                        canvas.canvas[y][x] = self.fill_char

    def erase(self, canvas):
        if not self.calc_third_point():
            return

        self.draw_line(canvas, self.x1, self.y1, self.x2, self.y2)
        self.draw_line(canvas, self.x2, self.y2, self.x3, self.y3)
        self.draw_line(canvas, self.x3, self.y3, self.x1, self.y1)

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        self.x3 += dx
        self.y3 += dy

    def get_parameters(self):
        return (f"x1 = {self.x1}, y1 = {self.y1}, "
                f"x2 = {self.x2}, y2 = {self.y2}, "
                f"x3 = {self.x3}, y3 = {self.y3}, "
                f"a = {self.a}, b = {self.b}, c = {self.c}, "
                f"border = '{self.border_char}', fill = '{self.fill_char}'")
