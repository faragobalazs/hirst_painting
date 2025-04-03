import turtle as turtle_module
import random
import colorgram

turtle_module.Turtle()
turtle_module.shape("classic")
turtle_module.color("black")
turtle_module.colormode(255)
turtle_module.speed("fastest")

# ---------------------------------------------------------------------------------- #
#for i in range(4):
#    tim.forward(100)
#    tim.right(90)

# ---------------------------------------------------------------------------------- #
#for i in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

# ---------------------------------------------------------------------------------- #
#colors = ["red", "blue", "black", "white", "yellow"]
#side = 3
#while side < 11:
#    color = random.choice(colors)
#    for i in range(side):
#        tim.pencolor(color)
#        tim.forward(100)
#        tim.right(360/side)
#    side += 1

# ---------------------------------------------------------------------------------- #

#def random_colour():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)

#    colors = (r, g, b)
#    return colors

# ---------------------------------------------------------------------------------- #
#directions = [0, 90, 180, 270]
#tim.pensize(10)
#tim.speed(10)

#for i in range(100):
#    tim.color(random_colour())
#    tim.setheading(random.choice(directions))
#    tim.forward(30)

# ---------------------------------------------------------------------------------- #

#def random_colour():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)

#    colors = (r, g, b)
#    return colors

#tim.speed(15)
#angle = 5
#turn = int(360 / angle)

#for i in range(turn):
#    tim.color(random_colour())
#    tim.left(angle)
#    tim.circle(100, None, None)

# ----------------------------------------------------------------------------------------------------- #

#rgb_colors = []

#colors = colorgram.extract("image.jpg", 101)

#for x in colors:
#    r = x.rgb.r
#    g = x.rgb.g
#    b = x.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)

color_list = [(2, 13, 31), (52, 25, 17), (219, 127, 106), (10, 105, 159), (241, 213, 69), (149, 84, 39), (214, 87, 64), (164, 162, 32), (157, 7, 24), (156, 63, 102), (11, 62, 31), (97, 6, 19), (206, 74, 104), (11, 96, 57), (1, 63, 145), (171, 135, 162), (8, 172, 216), (157, 34, 24), (4, 212, 207), (8, 140, 86), (146, 227, 216), (122, 193, 148), (101, 219, 229), (221, 178, 217), (80, 135, 179), (253, 196, 0), (122, 168, 189), (31, 85, 92), (227, 175, 167), (182, 191, 204), (67, 71, 43)]


def drawing():
    for x in range(10):
        random_number = random.randint(0, len(color_list)-1)
        random_color = color_list[random_number]
        turtle_module.dot(20, random_color)
        turtle_module.penup()
        turtle_module.forward(50)
        turtle_module.pendown()

y = -250
for _ in range(10):
    turtle_module.teleport(-250, y)
    drawing()
    y = y + 50

# ----------------------------------------------------------------------------------------------------- #

screen = turtle_module.Screen()
screen.exitonclick()













