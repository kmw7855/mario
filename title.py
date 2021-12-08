import game_framework
from pico2d import *
import test3


name = "TitleState"
image = None
image2 = None


def enter():
    global image, image2
    image = load_image('title.png')
    image2 = load_image('space.png')



def exit():
    global image, image2
    del(image)
    del(image2)



def update():
    pass

def draw():
    global image, image2
    clear_canvas()
    image.draw(800, 512)
    image2.draw(800, 312)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(test3)

def pause(): pass


def resume(): pass