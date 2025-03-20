import os
 
class ASCIIPaint:
    def __init__(self, width = 100, height = 20, background=' '):
        self.width = width
        self.height = height
        self.background = background
        self.canvas = [[background for _ in range(width)] for _ in range(height)]
        self.history = []
        self.redo_history = []
        self.shapes = {}

    def add_shape(self, shape):
        self.shapes[shape.id] = shape
        shape.draw(self)
        self.save_state()
        self.redo_history.clear()
    
    def delete_shape(self):
        if not self.shapes:
            print("No shapes to delete!")
            return
        
        self.list_shapes()
        shape_id = int(input("Enter the ID of the shape to delete: "))

        if shape_id in self.shapes:
            del self.shapes[shape_id] 
            self.redraw_canvas()  
            self.save_state()
            self.redo_history.clear()
            print(f"Shape {shape_id} deleted successfully.")
        else:
            print("Error: Shape ID not found.")

    def redraw_canvas(self):
        """Clears the canvas and redraws all remaining shapes."""
        self.canvas = [[self.background for _ in range(self.width)] for _ in range(self.height)]  
        for shape in self.shapes.values():
            shape.draw(self) 
        self.save_state()

    def list_shapes(self):
        if not self.shapes:
            print("No shapes on the canvas")
            return
        
        print("\nCurrent Shapes on Canvas:")
        print("------------------------------------------------------")
        print(f"{'ID':<5} {'Shape':<10} {'Parameters'}")
        print("------------------------------------------------------")

        for shape in self.shapes.values():
            shape_name = shape.__class__.__name__
            params = shape.get_parameters()
            print(f"{shape.id:<5} {shape_name:<10} {params}")

        print("------------------------------------------------------")
    
    def save_state(self):
        self.history.append([row[:] for row in self.canvas])
    
    def set_background(self, background_char):
        for y in range(self.height):
            for x in range(self.width):
                if self.canvas[y][x] == self.background:  
                    self.canvas[y][x] = background_char

        self.background = background_char
        self.save_state()
    
    def display(self):
        print("+" + "-" * self.width + "+")
        for row in self.canvas:
            print("|" + "".join(row) + "|")
        print("+" + "-" * self.width + "+")
    
    
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.canvas:
                file.write("".join(row) + "\n")
    
    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print(f"Warning: File '{filename}' doesn't exist!")
            return
        try:
            with open(filename, 'r') as file:
                self.canvas = [list(line.rstrip('\n')) for line in file]
            print(f"Canvas loaded from '{filename}' successfully!")
        except Exception as e:
            print(f"Error loading file: {e}")
    
    def undo(self):
        if self.history:
            self.history.append([row[:] for row in self.canvas])
            self.canvas = self.history.pop()
            print("Undo successful.")
        else:
            print("Nothing to undo!")

    def redo(self):
        if self.redo_history:
            self.history.append([row[:] for row in self.canvas])
            self.canvas = self.redo_history.pop()
            print("Redo successful.")
        else:
            print("Nothing to redo!")

    def move_shape(self):
        if not self.shapes:
            print("No shapes to move!")
            return

        self.list_shapes()
        
        try:
            shape_id = int(input("Enter the ID of the shape to move: "))  
        except ValueError:
            print("Error: Please enter a valid numeric ID!")
            return

        if shape_id in self.shapes:
            shape = self.shapes[shape_id]
            
            try:
                dx, dy = map(int, input("Enter the amount to move (dx dy): ").split())
            except ValueError:
                print("Error: Please enter two valid integers for dx and dy!")
                return

            self.save_state()  
            shape.move(dx, dy)  
            self.redraw_canvas()  
            print(f"Shape {shape_id} moved successfully.")
        else:
            print("Error: Shape ID not found.")


   
