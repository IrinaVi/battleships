from turtle import Turtle, Screen
from ship import Ship

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Battleships")

ship = Ship(x_position=10,y_position=10,vertical_direction=True,length=2)
ship.place_ship()

screen.exitonclick()