import turtle


width = 1200
height = 630
screen = turtle.Screen()
screen.setup(width, height, 20, 20)


def seg(t, ln):
    if ln > 6:
        ln3 = ln // 3
        seg(t, ln3)
        t.left(60)
        seg(t, ln3)
        t.right(120)
        seg(t, ln3)
        t.left(60)
        seg(t, ln3)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)


tu = turtle.Turtle()
tu.speed(100)
print(1)

tu.penup()
tu.goto(-380, 100)
tu.pendown()


tu.color('red', 'yellow')
tu.begin_fill()
for i in range(50):
    tu.forward(200)
    tu.left(170)

tu.end_fill()
# done()


tu.penup()
tu.goto(-480, -300)
tu.seth(0)
tu.pendown()

print(1)
seg(tu, 400)
print(2)
turtle.exitonclick()
