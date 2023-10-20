#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_Color = turtle_colors.pop()



# sets the turtle's position
startx = 0
starty = 0

# where the turtle goes
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.fillcolor(new_Color)
  t.pencolor(new_Color)
  t.right(45)
  t.forward(50)


# new starting position of turtle
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
