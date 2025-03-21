from Shapes.Shape import Shape

class Rectangle(Shape):
    def __init__(self, x1, y1, width, height, border_char = None, fill_char = None):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height

        self.x2 = x1 + width - 1
        self.y2 = y1 + height - 1

        self.border_char = border_char
        self.fill_char = fill_char

    def get_parameters(self):
        return f"x1 = {self.x1}, y1 = {self.y1}, x2 = {self.x2}, y2 = {self.y2}, border = '{self.border_char}', fill = '{self.fill_char}'"

    def draw(self, canvas):
        canvas.save_state()
        if 0 > self.x1 or self.x1 >= canvas.width or 0 > self.y1 or self.y1 >= canvas.height or 0 > self.x2 or self.x2 >= canvas.width or 0 > self.y2 or self.y2 >= canvas.height:
            print("----------INCORRECT INPUT! THE FIGURE SIZE VALUES ARE OUTSIDE THE CANVAS BOUNDARIES!!!----------")
        else:
            for x in range(self.x1, self.x2 + 1):
                for y in range(self.y1, self.y2 + 1):
                    if 0 <= x < canvas.width and 0 <= y < canvas.height:
                        if x == self.x1 or x == self.x2 or y == self.y1 or y == self.y2:
                            canvas.canvas[y][x] = self.border_char
                        elif self.fill_char:
                            canvas.canvas[y][x] = self.fill_char

    def erase(self, canvas):
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                if 0 <= x < canvas.width and 0 <= y < canvas.height:
                    canvas.canvas[y][x] = canvas.background

    def move(self, dx , dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy


    def fill(self, canvas, fill_char):
        self.fill_char = fill_char
        for x in range(self.x1 + 1, self.x2):
            for y in range(self.y1 + 1, self.y2):
                if 0 <= x < canvas.width and 0 <= y < canvas.height:
                    canvas.canvas[y][x] = self.fill_char
