import turtle

def koch(size, order):
    if order > 0:
        koch(size/3, order - 1)
        turtle.left(60)
        koch(size/3, order - 1)
        turtle.right(120)
        koch(size/3, order - 1)
        turtle.left(60)
        koch(size/3, order - 1)
    else:
        turtle.forward(size)

turtle.ht()
turtle.setheading(0)
turtle.speed(200)
for i in range(44):
    koch(size=300, order=4)
    turtle.right(233)

turtle.exitonclick()
