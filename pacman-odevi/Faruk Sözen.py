import turtle

scr = turtle.Screen()
kalem = turtle.Turtle()

scr.title("Pacman")
scr.setup (width=600,height=400)
scr.bgcolor("black")

kalem.speed(10)
kalem.up()
kalem.goto(0,-100)
kalem.color("yellow")
kalem.begin_fill()
kalem.circle(120)
kalem.end_fill()

#göz
kalem.goto(25,80)
kalem.color("black")
kalem.begin_fill()
kalem.circle(20)
kalem.end_fill()
#ağız
kalem.up()
kalem.goto(0,20)
kalem.down()

kalem.begin_fill()
kalem.right(40)
kalem.forward(150)
kalem.left(110)
kalem.forward(200)

kalem.end_fill()

#metin
kalem.goto(-110,-190)
kalem.color("yellow")
kalem.write("PACMAN",font=("Articulate",40,"bold"))










