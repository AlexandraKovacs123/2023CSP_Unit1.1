#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# create a spider body
spider.pensize(40)
spider.circle(20)
width = 8

# configure the spider legs
lengthOfLegs = 70
distanceOfLegs = 360 / width - 20
spider.pensize(5)
n = 0

# draw the legs
while (n < width):
  spider.goto(0, 20)
  if (n < 4):
    spider.setheading(distanceOfLegs * n - 45)
    spider.forward(lengthOfLegs)

  else:
    spider.setheading(distanceOfLegs * n + 45)
    spider.forward(lengthOfLegs)
  n = n + 1

n = 0

while (n < width):
  spider.pensize(3)
  if (n < 4):
    spider.goto(5, 20)
    spider.color("white")
    spider.circle(5)

  else:
    spider.penup()
    spider.goto(-15,20)
    spider.color("white")
    spider.pendown()
    spider.circle(5)

  n = n + 1


spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
