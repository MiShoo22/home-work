from turtle import *

#we want to paint a house

# 1 draw a square

speed(30)
width(7)
color("green")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#End of scuare

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()
color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(150, 150)
left (120)
right(90)
pendown()

color("blue")
forward(50)

left(90)
forward(40)

left (90)
forward(50)

left(90)
forward(40)

penup()
goto(170, 150)
pendown()
left(90)
forward(50)


penup()
goto(150, 125)
pendown()
left(90)
forward(40)


penup()
goto(10,100)
pendown()
left(90)
forward(50)

pendown()
right(90)
forward(50)

pendown()
right(90)
forward(50)

pendown()
right(90)
forward(50)

penup()
goto(10,125)
pendown()
left(180)
forward(50)


penup()
goto(35, 100)
pendown()
left(90)
forward(50)


penup()
goto(120,60)

pendown()
left(1)
forward(1)

exitonclick()





