from turtle import Turtle

class Ship:
    def __init__(self, x_position, y_position, vertical_direction, length):
        self.head_position = [x_position,y_position]
        self.vertical_direction = vertical_direction
        self.length = length
        self.ship_positions = [(x_position, y_position)]

    def place_ship(self):
        space = 0
        for i in range(0, self.length):
            if self.vertical_direction:
                turtle = Turtle("square")
                turtle.color("white")
                turtle.turtlesize(2)
                turtle.penup()
                turtle.goto(self.head_position[0],self.head_position[1]-space)
                space += 40
            else:
                turtle = Turtle("square")
                turtle.color("white")
                turtle.turtlesize(2)
                turtle.penup()
                turtle.goto(self.head_position[0]-space,self.head_position[1])
                space += 40




