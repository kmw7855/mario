from pico2d import *
from test2 import *


class pad:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.jump = 0
        self.jum = 0
        self.image = load_image('pad.png')
    def draw(self,mario_x, mario_y):
        global ground
        global highjump
        global can_move 
        self.image.draw(self.x, self.y)
        if self.x - 35 <= mario_x <= self.x + 35:
            pass
        else:
            pass
        if self.y + 20 <= mario_y <= self.y + 40 and self.x - 30 <= mario_x <= self.x + 30:
            highjump = 1

    def height(self,mario_x, mario_y):
        global ground
        global y
        if self.x - 35 <= mario_x <= self.x + 35: 
        #and self.y <= mario_y <= self.y + 70:
            ground = 130
