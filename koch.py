import turtle
turtle.speed(10)
turtle.up()
turtle.goto(-200,100)
turtle.down()
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)
def koch1(size,n):
    for i in range(3):
        koch(size,n)
        turtle.right(120)
koch1(400, 2)
turtle.up()
turtle.goto(-75,30)
turtle.down()
koch1(150, 2)

