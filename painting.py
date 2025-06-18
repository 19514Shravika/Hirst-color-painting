import turtle as turtle_module
import random
t=turtle_module.Turtle()
turtle_module.colormode(255)
colors_list=[(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]
t.hideturtle()             #remove the turtle mark and get only formatted dots
t.speed("fastest")
t.penup()                  #to remove the formatted line
t.setheading(225)          #set the direction
t.forward(300)             #make the movement
t.setheading(0)
no_of_colors=100
for color_count in range(1,no_of_colors+1):
    t.dot(20,random.choice(colors_list))
    t.forward(50)
    if color_count%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
screen=turtle_module.Screen()
screen.exitonclick()