import test4
import map2
from pico2d import *
import game_framework

Game_over = None
over = None
image = None
next_time = 0.0

class game_over:
    def __init__(self):
        self.font = load_font('mario.ttf', 150)

    def draw(self):
        if game_framework.stage == 1:
            self.font.draw(700, 512, '1 - 1', (255, 255, 255))
        if game_framework.stage == 2:
            self.font.draw(700, 512, '1 - 2', (255, 255, 255))
        if game_framework.stage == 3:
            self.font.draw(700, 512, '1 - 3', (255, 255, 255))




def enter():
    global Game_over,image , next_time
    Game_over = game_over()
    #next_time = 0.0
    image = load_image('gameover.png')
    pass



def exit():
    global Game_over, image, next_time
    del(Game_over)
    del(image)
    #del(next_time)


def update():
    global next_time
    if (next_time > 1.0):
        next_time = 0
        #game_framework.quit()
        game_framework.change_state(map2)
    delay(0.01)
    next_time += 0.05

def draw():
    global Game_over, image
    clear_canvas()
    image.draw(800, 512)
    Game_over.draw()
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            pass

def pause(): pass


def resume(): pass