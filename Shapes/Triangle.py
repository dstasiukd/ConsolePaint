from Shapes.Shape import Shape

class Triangle(Shape):
    def __init__(self, x, y, height, char = None):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.char = char

    def get_parameters(self):
        return f"x = {self.x}, y = {self.y}, height = {self.height}, char = '{self.char}'"
    
    def draw(self, canvas):
        canvas.save_state()
        if 0 > self.x or self.x > canvas.width or 0 > self.y or self.y > canvas.height or 0 > self.height or self.height > (canvas.width - self.height) or self.height > (canvas.height - self.height):
            print("----------INCORRECT INPUT! THE FIGURE SIZE VALUES ARE OUTSIDE THE CANVAS BOUNDARIES!!!----------")
        else:
            for i in range(self.height):
                for j in range(-i, i + 1):
                    px, py = self.x + j, self.y + i
                    if 0 <= px < canvas.width and 0 <= py < canvas.height:
                        canvas.canvas[py][px] = self.char

    def erase(self, canvas):
        for i in range(self.height):
            for j in range(-i, i + 1):
                px, py = self.x + j, self.y + i
                if 0 <= px < canvas.width and 0 <= py < canvas.height:
                    canvas.canvas[py][px] = canvas.background

    def move (self, dx, dy):
        self.x += dx
        self.y += dy

        
