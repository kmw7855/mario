import title
from pico2d import *
import game_framework

Game_over = None
over = None
image = None


class game_over:
    def __init__(self):
        self.font = load_font('mario.ttf', 150)

    def draw(self):
        self.font.draw(500, 512, 'Game Over', (255, 255, 255))




def enter():
    global Game_over,image 
    Game_over = game_over()
    image = load_image('gameover.png')
    pass



def exit():
    global Game_over, image
    del(Game_over)
    del(image)


def update():
    pass

def draw():
    global Game_over, image
    clear_canvas()
    Game_over.draw()
    image.draw()
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