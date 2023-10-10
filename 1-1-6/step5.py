#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
width = 6
lengthOfLegs = 70
distanceOfLegs = 380 / width
spider.pensize(5)
n = 0
while (n < width):
  spider.goto(0,0)
  spider.setheading(distanceOfLegs * n)
  spider.forward(lengthOfLegs)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()