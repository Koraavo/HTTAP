import turtle
import string

def countAll(text):
    letter_count = {}
    for characters in text:
        if characters in string.ascii_lowercase:
            letter_count.setdefault(characters, 0)
            letter_count[characters] += 1
    return letter_count


def histogram(text):
    dicta = countAll(text)
    list_keys = list(dicta.keys())
    sorted_key_list = sorted(list_keys)
    final_list = [dicta[elements] * 100 for elements in sorted_key_list]
    return final_list


def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()  # start filling this shape
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()  # stop filling this shape
    """End of drawing"""

def fillColor(t, height):
    if height >= 300:
        t.fillcolor("red")
    elif height >= 200 and height < 300:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    drawBar(t, height)


"""Data from the histogram"""
text = "banana"
sorted_keys = histogram(text)


"""Setting up my turtle and screen"""
maxheight = max(sorted_keys)
numbars = len(sorted_keys)
border = 10
wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0 - border, 0 - border, 40 * numbars + border, maxheight + border)
tess = turtle.Turtle()  # create tess and set some attributes
tess.color("black")
tess.pensize(3)

"""accessing data and callng the drawing"""
for a in sorted_keys:
    fillColor(tess, a)

wn.exitonclick()
