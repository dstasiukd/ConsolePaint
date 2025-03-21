import abc

class Shape(abc.ABC):
    shape_counter = 0

    def __init__(self):
        Shape.shape_counter += 1
        self.id = Shape.shape_counter

    @abc.abstractmethod
    def get_parameters(self):
        pass

    @abc.abstractmethod
    def draw(self, canvas):
        pass

    @abc.abstractmethod
    def move(self, dx, dy, canvas):
        pass

    @abc.abstractmethod
    def erase(self, canvas):
        pass

    @abc.abstractmethod
    def fill(self, canvas, fill_char):
        pass