from turtle import Turtle, Screen
from ship import Ship

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Battleships")

ship1 = Ship(x_position=-280,y_position=280,vertical_direction=True,length=3)
ship1.place_ship()

ship2 = Ship(x_position=280,y_position=-280,vertical_direction=False,length=4)
ship2.place_ship()

screen.exitonclick()