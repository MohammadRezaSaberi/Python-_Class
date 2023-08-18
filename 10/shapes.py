import turtle

t = turtle.Turtle()

t.shape('turtle')
t.speed(10)

t.penup()
t.goto(-100, 0)
t.pendown()
for i in range(5):
    t.forward(100)
    t.right(144)

t.penup()
t.goto(100, 0)
t.pendown()
for i in range(36):
    t.circle(50)
    t.left(10)

turtle.mainloop()