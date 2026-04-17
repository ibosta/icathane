import turtle

t = turtle.Turtle()

w = turtle.Screen()

w.title("Pac Man")
w.setup (width=900,height=600)
w.bgcolor("black")

t.up()
t.goto(0,-120)
t.color("yellow")
t.begin_fill()
t.circle(120)
t.end_fill()

t.goto(0,0)
t.color("black")
t.begin_fill()
t.left(30)
t.forward(200)
t.right(120)
t.forward(200)
t.left(60)
t.forward(200)
t.end_fill()

t.goto(-110,-190)
t.color("yellow")
t.write("Pac Man",font=("Articulate",40,"bold"))
