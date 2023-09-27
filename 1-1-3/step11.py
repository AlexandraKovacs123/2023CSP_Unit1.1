#   a113_flower.py
#   This code draws a flower.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# ring 3
painter.goto(20,210)
painter.color("blue")

for bigger in range(24):
    painter.right(15)
    painter.forward(30)
    painter.stamp()

# ring 1
painter.color("darkorchid")
painter.goto(20, 180)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.stamp()

# ring 2
painter.goto(20,150)
painter.color("red")

for smaller in range(12):
    painter.right(30)
    painter.forward(30)
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()
