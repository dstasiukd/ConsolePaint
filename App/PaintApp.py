from App.Canvas import ASCIIPaint
from Shapes.Rectangle import Rectangle
from Shapes.Triangle import Triangle
from Shapes.Circle import Circle

class PaintApp:
    def __init__(self):
        self.paint = ASCIIPaint()

    def menu(self):
        while True:
            self.paint.display()
            print("\nASCII Paint Menu:")
            print("1. Draw a rectangle")
            print("2. Draw a triangle")
            print("3. Draw a circle")
            print("4. Set background character")
            print("5. Save to file")
            print("6. Load from file")
            print("7. Undo")
            print("8. Redo")
            print("9. Move shape")
            print("10. List of shapes")
            print("11. Delete shape")
            print("12. Exit")
            choice = input("Enter your choice: ")
            

            if choice == '1':
                x1, y1, x2, y2 = map(int, input("Enter x1, y1, height and width coordinates: ").split())
                border_char = input("Enter border character: ")
                fill_char = input("Enter fill character (or leave blank): ") or None
                shape = Rectangle(x1, y1, x2, y2, border_char, fill_char)
                self.paint.add_shape(shape)
            elif choice == '2':
                x, y, a, b, c = map(int, input("Enter x y coordinates and a b c: ").split())
                char = input("Enter character: ")
                shape = Triangle(x, y, a, b, c, char)
                self.paint.add_shape(shape)
            elif choice == '3':
                x, y, radius = map(int, input("Enter x y coordinates and radius: ").split())
                char = input("Enter character: ")
                shape = Circle(x, y, radius, char)
                self.paint.add_shape(shape)
            # elif choice == '4':
            #     x, y = map(int, input("Enter x y coordinates to erase: ").split())
            #     self.paint.erase(x, y)
            elif choice == '4':
                background_char = input("Enter a single character for the background: ")
                self.paint.set_background(background_char)
            elif choice == '5':
                filename = input("Enter filename to save: ")
                self.paint.save_to_file(filename)
            elif choice == '6':
                filename = input("Enter filename to load: ")
                self.paint.load_from_file(filename)
            elif choice == '7':
                self.paint.undo()
            elif choice == '8':
                self.paint.redo()
            elif choice == '9':
                dx, dy = map(int, input("Enter x y coordinates to move: ").split())
                self.paint.move_shape()
            elif choice == '10':
                self.paint.list_shapes()
            elif choice == '11':
                self.paint.delete_shape()
            elif choice == '12':
                break
            else:
                print("Invalid choice. Please try again.")
