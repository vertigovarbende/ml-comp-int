import turtle

# (1) turtle

# drawing board
drawing_board = turtle.Screen()
drawing_board.bgcolor("Yellow")
drawing_board.title("Python turtle")

# turtle instance
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle.exitonclick()

# ex1: basic square
import turtle

# drawing_board

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("basic square")

# turtle
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle.exitonclick()


# drawing_board
drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("basic square")

# turtle_instance
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")

for i in range(4):
    turtle_instance.left(90)
    turtle_instance.forward(300)
turtle.exitonclick()


# ex2: basic star

import turtle

# drawing_board
drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("basic star")

# turtle_instance
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
for i in range(5):
    turtle_instance.forward(300)
    turtle_instance.right((360 / 5) * 2)
turtle.exitonclick()


# ex3: cokgen ve ucgen

ucgen_ciz = turtle.Turtle()
ucgen_ciz.shape('turtle')
num_size = int(input("enter the size: "))
for i in range(num_size):
    ucgen_ciz.left((180 / num_size) * 2)
    ucgen_ciz.forward(200)
turtle.done()


# ex4: daire - circle()

# drawing_board
drawing_board = turtle.Screen()
drawing_board.bgcolor("gray")
drawing_board.title("circle")

# turtle_instance
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.speed(6)

turtle_instance.circle(90, 360)
turtle_instance.reset()

# yarim_cember
turtle_instance.forward(180)
turtle_instance.left(90)
turtle_instance.circle(90, 180)
turtle_instance.reset()

# cokgen with circle() method
turtle_instance.circle(90, 360, 3)
turtle.exitonclick()


# (2) methods

# turtle.shape()
# turtle, triangle, classic, arrow, circle, square

# turtle.color("red", "green")
# red -> turtle shape'in dıs hat rengi ve cizilen cizginin rengi
# green -> turtle shape'ın ic hat rengi

import turtle

# drawing_board
drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("renkli kare")

# turtle_instance
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("red", "green")
for i in range(4):
    turtle_instance.right(90)
    turtle_instance.forward(300)
turtle.exitonclick()



# ex5:

from turtle import *

# drawing_board
drawing_board = Screen()
drawing_board.bgcolor("gray")
drawing_board.title("steps")

# turtle_instance
turtle_instance = Turtle()
turtle_instance.speed(6)
turtle_instance.shape("turtle")
turtle_instance.color("red", "green")

# steps
for i in range(5):
    turtle_instance.forward(50)
    turtle_instance.right(90)
    turtle_instance.forward(50)
    turtle_instance.left(90)
exitonclick()


# (2) method
# shapesize()

# ex6: Ekrana çizgi rengi kırmızı dolgu rengi sarı olan
# bir yıldız çizen programı yazınız.


from turtle import *

# drawing_board
drawing_board = Screen()
drawing_board.bgcolor("gray")
drawing_board.title("star")

# turtle_instance
turtle_instance = Turtle()
turtle_instance.speed(5)
turtle_instance.color("red", "yellow")
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)

turtle_instance.begin_fill()
# star
for i in range(5):
    turtle_instance.right((360 / 5) * 2)
    turtle_instance.forward(200)
turtle_instance.end_fill()
exitonclick()


# ex7: Ekrana dolgu rengi sarı, kenar çizgi rengi
# birbirinden farklı olan kare çizen programı
# yazınız

from turtle import *
colors = ["black","violet","cyan","red"]

# drawing_board
drawing_board = Screen()
drawing_board.bgcolor("gray")
drawing_board.title("squares")

# turtle_instance
turtle_instance = Turtle()
turtle_instance.speed(5)
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)
turtle_instance.pensize(4)


turtle_instance.begin_fill()
for i in colors:
    turtle_instance.color(i, "yellow")
    for j in range(4):
        turtle_instance.forward(200)
        turtle_instance.left(90)
turtle_instance.end_fill()
exitonclick()


turtle_instance.begin_fill()
for i in colors:
    turtle_instance.pencolor(i)
    turtle_instance.forward(200)
    turtle_instance.left(90)
turtle_instance.end_fill()
exitonclick()


# ex8: ic ice kare 4 kare

from turtle import *

# drawing_board
drawing_board = Screen()
drawing_board.title("ic ice kare")
drawing_board.bgcolor("gray")

# turtle_instance
turtle_instance = Turtle()
turtle_instance.speed(5)
turtle_instance.shape("turtle")
turtle_instance.color("green", "green")
turtle_instance.pensize(5)

turtle_instance.begin_fill()
# 1
for i in range(4):
    turtle_instance.forward(160)
    turtle_instance.left(90)
turtle_instance.end_fill()

turtle_instance.color("red", "red")
turtle_instance.begin_fill()
# 2
turtle_instance.penup()
turtle_instance.goto(20, 20)
turtle_instance.pendown()
for i in range(4):
    turtle_instance.forward(120)
    turtle_instance.left(90)
turtle_instance.end_fill()

turtle_instance.color("blue", "blue")
turtle_instance.begin_fill()
# 3
turtle_instance.penup()
turtle_instance.goto(40, 40)
turtle_instance.pendown()
for i in range(4):
    turtle_instance.forward(80)
    turtle_instance.left(90)
turtle_instance.end_fill()

turtle_instance.color("yellow", "yellow")
turtle_instance.begin_fill()
# 4
turtle_instance.penup()
turtle_instance.goto(60, 60)
turtle_instance.pendown()
for i in range(4):
    turtle_instance.forward(40)
    turtle_instance.left(90)
turtle_instance.end_fill()

exitonclick()




# ex9: japon bayragi

from turtle import *

# drawing_board
drawing_board = Screen()
drawing_board.bgcolor("white")
drawing_board.title("japanese flag")

# turtle_instance
turtle_instance = Turtle()
turtle_instance.shape("turtle")
turtle_instance.speed(5)
turtle_instance.pencolor("black")
turtle_instance.pensize(5)

for i in range(2):
    turtle_instance.forward(150)
    turtle_instance.right(90)
    turtle_instance.forward(100)
    turtle_instance.right(90)

turtle_instance.penup()
turtle_instance.color("red", "red")
turtle_instance.goto(75, -80)
turtle_instance.begin_fill()
turtle_instance.circle(30)
turtle_instance.end_fill()

exitonclick()





# ex10: chess board


from turtle import *

colors_matrix = []
for i in range(8):
    row = []
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                row.append("white")
            else:
                row.append("black")
        else:
            if j % 2 == 0:
                row.append("black")
            else:
                row.append("white")
    colors_matrix.append(row)

# drawing_board
drawing_board = Screen()
drawing_board.bgcolor("gray")
drawing_board.title("chess board")

# turtle_instance
turtle_instance = Turtle()
turtle_instance.shape("turtle")
turtle_instance.speed(0)
turtle_instance.shapesize(2)


# chess board

for i in range(8):
    for j in range(8):
        turtle_instance.color(colors_matrix[i][j], colors_matrix[i][j])
        turtle_instance.begin_fill()
        for k in range(4):
            turtle_instance.forward(20)
            turtle_instance.right(90)
        turtle_instance.end_fill()
        turtle_instance.penup()
        turtle_instance.setx(j * 20)
        turtle_instance.pendown()
    turtle_instance.penup()
    turtle_instance.sety(20 * i)
    turtle_instance.pendown()


for i in range(-1,8):
    for j in range(8):
        turtle_instance.color(colors_matrix[i][j], colors_matrix[i][j])
        turtle_instance.begin_fill()
        for k in range(4):
            turtle_instance.forward(20)
            turtle_instance.right(90)
        turtle_instance.end_fill()
        turtle_instance.penup()
        turtle_instance.setx(j * 20)
        turtle_instance.pendown()
    turtle_instance.penup()
    turtle_instance.sety(20 * (i + 1))
    turtle_instance.pendown()
exitonclick()


# ex11:
from turtle import *

x_coordinate = int(input("Please enter the bound of the x line: "))
y_coordinate = int(input("Please enter the bound of the y line: "))
origin = 0, 0


# drawing_board
drawing_board = Screen()
drawing_board.bgcolor("gray")
drawing_board.title("coordinate system")


# turtle_instance
turtle_instance = Turtle()
turtle_instance.speed(0)
turtle_instance.color("black", "black")
turtle_instance.shape("arrow")
turtle_instance.shapesize(0.5)

# origin_circle
turtle_instance.begin_fill()
turtle_instance.circle(1)
turtle_instance.end_fill()

# x-line
turtle_instance.forward(x_coordinate)
turtle_instance.penup()
turtle_instance.goto(origin)
turtle_instance.pendown()
turtle_instance.left(180)
turtle_instance.forward(x_coordinate)

# y-line
turtle_instance.penup()
turtle_instance.goto(origin)
turtle_instance.pendown()
turtle_instance.right(90)
turtle_instance.forward(y_coordinate)
turtle_instance.penup()
turtle_instance.goto(origin)
turtle_instance.pendown()
turtle_instance.left(180)
turtle_instance.forward(y_coordinate)

exitonclick()
