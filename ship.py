import turtle

class Ship:
    def __init__(self, x_position, y_position, direction, length):
        self.x_pos = x_position
        self.y_pos = y_position
        self.direction = direction
        self.length = length

    def place_ship(self):