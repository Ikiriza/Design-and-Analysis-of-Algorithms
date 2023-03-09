import turtle


screen=turtle.Screen()
screen=turtle.Screen()
screen.setup(558,688,startx=0,starty=180)
t=turtle.Turtle()
turtle.Terminator
screen.setup(558,688,startx=0,starty=180)
t=turtle.Turtle()

turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(45)
turtle.right(11)

for i in range(150):
    turtle.circle(25)
    if 7 < i < 62:
       turtle.left(5)
    if 80 < i < 133:
       turtle.right(5)
    if i < 80:
       turtle.forward(10)
    else:
       turtle.forward(5)
