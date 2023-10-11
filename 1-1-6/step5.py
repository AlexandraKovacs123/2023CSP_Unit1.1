#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# create a spider body
spider.pensize(40)
spider.circle(20)
width = 8

#configure the spider legs
lengthOfLegs = 70
distanceOfLegs = 360 / width
spider.pensize(5)
n = 0

# draw the legs
while (n < width):
  if (n < 4):
    spider.goto(0,20)
    spider.setheading(distanceOfLegs * n - 45)
    spider.forward(lengthOfLegs)
    n = n + 1

  else:
    spider.goto(0, 20)
    spider.setheading(distanceOfLegs * n + 45)
    spider.forward(lengthOfLegs)
    n = n + 1

 # n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()