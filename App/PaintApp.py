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
            print("4. Fill a shape")
            print("5. Set background character")
            print("6. Save to file")
            print("7. Load from file")
            print("8. Move shape")
            print("9. Delete shape")
            print("10. List of shapes")
            print("11. Undo")
            print("12. Redo")
            print("13. Exit")
            choice = input("Enter your choice: ")
            

            if choice == '1':
                x1, y1, width, height = map(int, input("Enter (x1, y1) coordinates and width and height: ").split())
                border_char = input("Enter border character: ")
                fill_char = input("Enter fill character (or leave blank): ") or None
                shape = Rectangle(x1, y1, width, height, border_char, fill_char)
                self.paint.add_shape(shape)
            elif choice == '2':
                x, y, a, b, c = map(int, input("Enter x y coordinates and a b c: ").split())
                border_char = input("Enter border character: ")
                fill_char = input("Enter fill character (or leave blank): ") or None
                shape = Triangle(x, y, a, b, c, border_char, fill_char)
                self.paint.add_shape(shape)
            elif choice == '3':
                x, y, radius = map(int, input("Enter (x, y) coordinates and radius: ").split())
                border_char = input("Enter border character: ")
                fill_char = input("Enter fill character (or leave blank): ") or None
                shape = Circle(x, y, radius, border_char, fill_char)
                self.paint.add_shape(shape)
            elif choice == '4':
                self.paint.fill_shape()
            elif choice == '5':
                background_char = input("Enter a single character for the background: ")
                self.paint.set_background(background_char)
            elif choice == '6':
                filename = input("Enter filename to save: ")
                self.paint.save_to_file(filename)
            elif choice == '7':
                filename = input("Enter filename to load: ")
                self.paint.load_from_file(filename)
            elif choice == '8':
                self.paint.move_shape()
            elif choice == '9':
                self.paint.delete_shape()
            elif choice == '10':
                self.paint.list_shapes()
            elif choice == '11':
                self.paint.undo()
            elif choice == '12':
                self.paint.redo()
            elif choice == '13':
                break
            else:
                print("Invalid choice. Please try again.")
