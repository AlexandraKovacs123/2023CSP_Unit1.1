#   a113_forward_and_right.py
import turtle as trtl

painter = trtl.Turtle()

# Add code to make the turtle move forward 20 pixels
# and then turn right 20 degrees

for line in range(18):
    painter.forward(20)
    painter.right(20)

painter.penup()
painter.forward(150)
painter.pendown()

for square in range(4):
    painter.forward(25)
    painter.right(90)

painter.penup()
painter.left(90)
painter.forward(100)
painter.pendown()

for octagon in range(8):
    painter.forward(40)
    painter.left(45)

painter.penup()
painter.forward(150)
painter.left(90)
painter.forward(100)
painter.pendown()



wn = trtl.Screen()
wn.mainloop()

