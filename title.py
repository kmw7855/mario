import game_framework
from pico2d import *
import next_world


name = "TitleState"
image = None
image2 = None
title_bgm = None


def enter():
    global image, image2
    image = load_image('title.png')
    image2 = load_image('space.png')
    title_bgm = load_music('start.mp3')
    title_bgm.set_volume(64)
    title_bgm.repeat_play()

def exit():
    global image, image2, wait_time
    del(image)
    del(image2)
    #del(wait_time)


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
            game_framework.change_state(next_world)
            game_framework.stage = 1
            

def pause(): pass


def resume(): pass