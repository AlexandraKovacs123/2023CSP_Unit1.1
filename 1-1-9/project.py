import turtle as trtl

trtl.penup()
trtl.goto(-50,200)
trtl.fillcolor("white")
trtl.speed(12)
trtl.pendown()

# draw snowflakes


# draw that guy 2
trtl.forward(150)
trtl.right(90)
trtl.forward(55)
trtl.left(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(15)
trtl.left(90)
trtl.forward(85)
trtl.left(90)
trtl.forward(60)
trtl.right(90)
trtl.forward(65)
trtl.right(90)
trtl.forward(60)
trtl.left(90)
trtl.forward(15)
trtl.left(90)
trtl.forward(40)
trtl.right(90)
trtl.forward(60)
trtl.right(90)
trtl.forward(85)
trtl.right(90)
trtl.forward(60)
trtl.left(90)
trtl.forward(15)
trtl.left(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(70)
trtl.left(90)
trtl.forward(45)
trtl.right(90)
trtl.forward(70)
trtl.right(90)
trtl.forward(50)
trtl.right(90)
trtl.forward(30)
trtl.left(90)
trtl.forward(15)
trtl.left(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(40)
trtl.left(90)
trtl.forward(50)
trtl.right(90)
trtl.forward(60)
trtl.right(90)
trtl.forward(60)
trtl.left(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(15)
trtl.left(90)
trtl.forward(40)
trtl.left(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(15)
trtl.right(90)
trtl.forward(15)
trtl.left(90)
trtl.forward(60)
trtl.right(90)
trtl.forward(10)

# Starting location of eyes and color
trtl.penup()
trtl.fillcolor("black")
trtl.forward(10)
trtl.right(90)
trtl.forward(90)
trtl.left(90)
trtl.penup()
trtl.forward(20)

trtl.pendown()

# Draw accessories of guy 2
for eyes in range (2):
    trtl.shape("square")
    # trtl.forward(40)
    trtl.turtlesize(2)
    trtl.stamp()
    trtl.penup()
    trtl.forward(80)
    trtl.pendown()

trtl.penup()
trtl.goto(-15,110)
for smallEyes in range(2):
    trtl.turtlesize(1)
    trtl.fillcolor("white")
    trtl.stamp()
    trtl.forward(80)

# nose
trtl.goto(15,80)
trtl.color("orange")
trtl.penup()
trtl.shape("arrow")
trtl.turtlesize(2)
trtl.stamp()



"""
for bow in range(2):
    trtl.penup()
    trtl.goto(-15,50)
    trtl.color("black")
"""


"""
import turtle as trtl
penup
goto somewhere in the middle of screen
set turtle size and color
pendown
draw that guy #2
move somewhere else
make loop to
    draw that guy #1
    move somewhere else
draw snow flakes using loop
"""


wn = trtl.Screen()
wn.mainloop()
