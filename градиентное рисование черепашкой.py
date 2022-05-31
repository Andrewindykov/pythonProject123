import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()


def polygon(n, size=80):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(100)

colors = ['orange', 'cyan', 'blue', 'green', 'red', 'aqua', 'white']

size = 45

# colored on black 5-angles
window.bgcolor("black")
window.colormode(255)
for i in range(5, 290):

    turtlePen.color((7*i%256,8,50))
    polygon(3, size)
    size = size + 1
    turtlePen.left(16)

window.mainloop()
