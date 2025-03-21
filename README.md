# ConsolePaint
Simple Paint app by Darya Stasiuk from group 353505
## UI description
The UI includes a canvas (width = 100, height = 20) with a frame and a drop-down menu where you can select one of the suggested commands. 
```
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+

ASCII Paint Menu:
1. Draw a rectangle
2. Draw a triangle
3. Draw a circle
4. Fill a shape
5. Set background character
6. Save to file
7. Load from file
8. Move shape
9. Delete shape
10. List of shapes
11. Undo
12. Redo
13. Exit
Enter your choice:
```
## Functions
# 
# save_to_file [filename]

# load_from_file [filename]
# undo
# redo
# set_background [background_char]
# list_shapes
It is possible to view the list of shapes, which contains the id, what shape (circle, rectangle or triangle) and their parameters (for example: radius, height, width, fill_char etc.)
```
Current Shapes on Canvas:
------------------------------------------------------
ID    Shape      Parameters
------------------------------------------------------
1     Rectangle  x1 = 2, y1 = 3, x2 = 46, y2 = 4, border = '$', fill = '$'
2     Circle     x = 4, y = 5, radius = 1, border_char = '#, fill_char ='None'
------------------------------------------------------
```