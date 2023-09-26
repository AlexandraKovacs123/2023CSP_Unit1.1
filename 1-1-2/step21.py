# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

#change pen color and fill
#then draw a circle
painter.pencolor("green")
painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(90)
painter.end_fill()

#change pen color and fill again
#draw circles around the first circle
painter.penup()
painter.right(90)
painter.pendown()
painter.pencolor("red")
painter.fillcolor("pink")
painter.begin_fill()
painter.circle(75)
painter.end_fill()

wn = trtl.Screen()
wn.mainloop()
