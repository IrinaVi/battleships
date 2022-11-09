from turtle import Turtle, Screen, textinput
from ship import Ship

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Battleships")

textinput("Battleships", "Enter ship position")

ship1 = Ship(x_position=-230,y_position=230,vertical_direction=True,length=3)
ship1.place_ship()

ship2 = Ship(x_position=230,y_position=-225,vertical_direction=False,length=4)
ship2.place_ship()

screen.exitonclick()