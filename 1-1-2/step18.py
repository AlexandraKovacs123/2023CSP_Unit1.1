# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pencolor("purple")
painter.fillcolor("red")
painter.begin_fill()
painter.circle(180)
painter.end_fill()

# move the turtle to another part of the screen
painter.penup()
painter.goto(-200, -200)
painter.pendown()

# change both the pen and fill colors
# then draw a polygon of your choice
painter.pencolor("blue")
painter.fillcolor("purple")
painter.begin_fill()
painter.circle(100, 360, 12)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
