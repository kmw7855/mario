import title
from pico2d import *
import game_framework

Game_over = None

class game_over:
    def __init__(self):
        game_over.font = load_font('mario.ttf', 90)
    def draw(self):
        self.font.draw(600, 512, 'Game Over', (0, 152, 0))

def enter():
    Game_over = game_over()
    pass



def exit():
    global Game_over
    del(Game_over)



def update():
    pass

def draw():
    global Game_over
    clear_canvas()
    Game_over.draw()
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(title)

def pause(): pass


def resume(): pass