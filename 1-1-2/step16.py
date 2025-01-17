# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(50)

# move the turtle to another part of the screen
painter.penup()
painter.forward(100)

# add code here for an arc
painter.pendown()
painter.circle(50, 180)

# move the turtle to another part of the screen
painter.penup()
painter.right(90)
painter.forward(50)

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.pendown()
painter.circle(75, 190, 5)

# move the turtle to another part of the screen
painter.penup()
painter.right(90)
painter.forward(150)

# add code here to create a polygon of your choice using the circle method
painter.pendown()
painter.circle(100, 360, 6)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
