import unittest
from App.Canvas import ASCIIPaint
from Shapes.Rectangle import Rectangle
from Shapes.Triangle import Triangle

class TestASCIIPaint(unittest.TestCase):

    def setUp(self):
        """Create a fresh canvas before each test"""
        self.paint = ASCIIPaint(width=20, height=10, background='.')

    def test_canvas_initialization(self):
        """Test that the canvas initializes correctly"""
        self.assertEqual(len(self.paint.canvas), 10)  
        self.assertEqual(len(self.paint.canvas[0]), 20)  
        self.assertTrue(all(cell == '.' for row in self.paint.canvas for cell in row))

    def test_add_rectangle(self):
        """Test adding a rectangle to the canvas"""
        rect = Rectangle(2, 2, 5, 3, border_char='*')
        self.paint.add_shape(rect)

        self.assertIn(rect.id, self.paint.shapes)
        self.assertEqual(self.paint.shapes[rect.id], rect)

    def test_draw_rectangle(self):
        """Test drawing a rectangle"""
        rect = Rectangle(2, 2, 5, 3, border_char='*')
        self.paint.add_shape(rect)

        self.assertEqual(self.paint.canvas[2][2], '*')  
        self.assertEqual(self.paint.canvas[4][6], '*')  

    def test_move_rectangle(self):
        """Test moving a rectangle"""
        rect = Rectangle(2, 2, 5, 3, border_char='*')
        self.paint.add_shape(rect)
        rect.move(3, 2)

        self.assertEqual(rect.x1, 5)
        self.assertEqual(rect.y1, 4)

    def test_fill_rectangle(self):
        """Test filling a rectangle"""
        rect = Rectangle(2, 2, 5, 3, border_char='*')
        self.paint.add_shape(rect)
        rect.fill(self.paint, fill_char='#')

        self.assertEqual(self.paint.canvas[3][3], '#')  

    def test_add_triangle(self):
        """Test adding a triangle"""
        tri = Triangle(5, 5, 3, 4, 5, border_char='*')
        self.paint.add_shape(tri)

        self.assertIn(tri.id, self.paint.shapes)
        self.assertEqual(self.paint.shapes[tri.id], tri)

    def test_fill_triangle(self):
        """Test filling a triangle"""
        tri = Triangle(5, 5, 3, 4, 5, border_char='*')
        self.paint.add_shape(tri)
        tri.fill(self.paint, fill_char='#')

        self.assertEqual(tri.fill_char, '#')

    # def test_undo(self):
    #     """Test undo functionality"""
    #     rect = Rectangle(2, 2, 5, 3, border_char='*')
    #     self.paint.add_shape(rect)
    #     self.paint.undo()

    #     self.assertTrue(all(cell == '.' for row in self.paint.canvas for cell in row))

    def test_redo(self):
        """Test redo functionality"""
        rect = Rectangle(2, 2, 5, 3, border_char='*')
        self.paint.add_shape(rect)
        self.paint.undo()
        self.paint.redo()

        self.assertEqual(self.paint.canvas[2][2], '*')

if __name__ == '__main__':
    unittest.main()
