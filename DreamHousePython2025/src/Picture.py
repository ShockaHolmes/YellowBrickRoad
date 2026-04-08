import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=1200, height=1200, bg='lightblue')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.door = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):
        self.wall = Square(canvas=self.canvas, size=300, color="blue", fill="Blue", line=2)
        self.wall.move_horizontal(80)
        self.wall.move_vertical(-350)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=175, color="blue", fill="Blue", line=2)
        self.wall.move_horizontal(370)
        self.wall.move_vertical(-225)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=1000, color="green", fill="green", line=2)
        self.wall.move_horizontal(-40)
        self.wall.move_vertical(-50)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=40, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(215)
        self.wall.move_vertical(-50)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=40, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(215)
        self.wall.move_vertical(-10)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=40, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(215)
        self.wall.move_vertical(10)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=40, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(215)
        self.wall.move_vertical(30)
        self.wall.make_visible()

        self.window = Square(canvas=self.canvas, size=60, color="black", fill="black", line=1)
        self.window.move_horizontal(130)
        self.window.move_vertical(-300)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=60, color="black", fill="black", line=1)
        self.window.move_horizontal(280)
        self.window.move_vertical(-300)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=60, color="black", fill="black", line=1)
        self.window.move_horizontal(120)
        self.window.move_vertical(-150)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=100, color="black", fill="black", line=1)
        self.window.move_horizontal(400)
        self.window.move_vertical(-150)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=80, color="gray", fill="gray", line=1)
        self.window.move_horizontal(415)
        self.window.move_vertical(-50)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=80, color="gray", fill="gray", line=1)
        self.window.move_horizontal(415)
        self.window.move_vertical(0)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=60, color="black", fill="black", line=1)
        self.window.move_horizontal(280)
        self.window.move_vertical(-150)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=60, color="tan", fill="tan", line=1)
        self.window.move_horizontal(200)
        self.window.move_vertical(-120)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=60, color="tan", fill="tan", line=1)
        self.window.move_horizontal(200)
        self.window.move_vertical(-150)
        self.window.make_visible()


        self.roof = Triangle(canvas=self.canvas, height=150, width=350, color="tan", fill="tan", line=2)
        self.roof.move_horizontal(45)
        self.roof.move_vertical(135)
        self.roof.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=225, width=75, color="green", fill="green", line=2)
        self.roof.move_horizontal(600)
        self.roof.move_vertical(500)
        self.roof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="yellow", fill="yellow", line=1)
        self.sun.move_horizontal(500)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
