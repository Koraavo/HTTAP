import turtle

new_color = input("Enter the screen color:")
wn = turtle.Screen()
wn.bgcolor(str(new_color))        # set the window background color
tess = turtle.Turtle()
turtle_color = input("Let's color the turtle: ")
tess.color(str(turtle_color))   # make tess the color entered by the user
new_pensize = input("Enter the size of the pen: ")
tess.pensize(int(new_pensize))                 # set the width of her pen
tess.penup()
tess.setposition(-200,-200)
tess.pendown()
for i in range(5):
    tess.forward(50)    # asked her to make a star
    tess.right(145)

wn.exitonclick()                # wait for a user click on the canvas



# draw the desired shape and fill it with the desired color

wn = turtle.Screen()
june = turtle.Turtle()


sides = input("How many sides should the polygon have?: ")
length = input("What should be the length of the sides?: ")
color = input("What color should the polygon be filled with?: ")
june.fillcolor(color)
june.begin_fill()
for t in range(int(sides)):
    june.forward(int(length))
    june.left(360/int(sides))
june.end_fill()
wn.exitonclick()








