from turtle import Turtle

class Ship:
    def __init__(self, x_position, y_position, vertical_direction, length):
        self.head_position = (x_position,y_position)
        self.vertical_direction = vertical_direction
        self.length = length
        self.ship_positions = [(x_position, y_position)]

    def place_ship(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.turtlesize(2)
        turtle.goto(self.head_position)
        for i in range(self.length):
            if self.vertical_direction:
                turtle.left(90)
                turtle.pendown()
                turtle.forward(10)

