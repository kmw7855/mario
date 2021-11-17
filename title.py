import game_framework
from pico2d import *
import test2


name = "TitleState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('title.png')



def exit():
    global image
    del(image)



def update():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(800, 512)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(test2)

def pause(): pass


def resume(): pass