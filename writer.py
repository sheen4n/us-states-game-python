from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_content(self, x, y, content):
        self.goto(x, y)
        self.write(content, align=ALIGNMENT, font=FONT)
