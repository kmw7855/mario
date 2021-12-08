import game_framework
from pico2d import *
import title


name = "StartState"
image = None
logo_time = 0.0
logo_music = None

def enter():
    global image, logo_music
    image = load_image('kpu.png')
    logo_music = load_wav('logo.wav')
    logo_music.set_volume(12)


def exit():
    global image
    del(image)



def update():
    global logo_time, logo_music
    logo_music.play(1)
    if (logo_time > 3):
        logo_time = 0
        #game_framework.quit()
        game_framework.change_state(title)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(800, 512)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




