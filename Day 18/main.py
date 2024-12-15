import colorgram,random
rgbcolors=[]
colors=colorgram.extract('painting.jpg',30)

from turtle import Turtle,Screen
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgbcolors.append((r,g,b))

turtle=Turtle()
srceen=Screen()
srceen.colormode(255)
turtle.penup()

def paint():
    for i in range(0,7):
        for j in range (0,7):
            turtle.dot(20,random.choice(rgbcolors))
            if not j==6:
                turtle.forward(50)
        if i==0 or i%2==0:
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
        else:
            
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
paint()
srceen.exitonclick()