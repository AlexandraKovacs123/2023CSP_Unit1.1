#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition
start_loop = 'y'

while (start_loop == 's'):
    painter.color("green")
    painter.circle(25,360,4)

# Add an infinite loop
painter.penup()
painter.pencolor("salmon")

line = 4

while (line % 2 != 2):
    painter.left(30)
    painter.pendown()
    painter.circle(25,360,6)
    line = line + 2
    if (line % 54 == 0):
        painter.color("lime")
    if (line % 108 == 0):
        painter.color("salmon")
wn = trtl.Screen()
wn.mainloop()
