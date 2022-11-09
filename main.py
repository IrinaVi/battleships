from turtle import Turtle, Screen, textinput
from ship import Ship

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Battleships")

# position = textinput("Battleships", "Enter ship position")
y_positions = {
    '1': 230,
    '2': 190,
    '3': 150,
    '4': 110,
    '5': 70,
    '6': 30,
    '7': -10,
    '8': -50,
    '9': -90,
    '10': -130
}

ship1 = Ship(x_position=-130,y_position=0,vertical_direction=True,length=1)
ship1.place_ship()
#
# ship2 = Ship(x_position=230,y_position=-225,vertical_direction=False,length=4)
# ship2.place_ship()

screen.exitonclick()