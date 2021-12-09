import title
import map1
import map3
import map2
from pico2d import *
import game_framework

Game_over = None
over = None
image = None
wait_time =0
die_bgm = None

class game_over:
    def __init__(self):
        self.font = load_font('mario.ttf', 150)

    def draw(self):
        if game_framework.life == 0:
            self.font.draw(500, 512, 'Game Over', (255, 255, 255))
        else:
            self.font.draw(500, 512, 'life : %d' % (game_framework.life), (255, 255, 255))



def enter():
    global Game_over,image, wait_time, die_bgm
    Game_over = game_over()
    image = load_image('gameover.png')
    die_bgm = load_music('gameover.mp3')
    die_bgm.set_volume(64)
    game_framework.life -= 1
    #die_bgm.play(1)
    wait_time =0



def exit():
    global Game_over, image
    del(Game_over)
    del(image)


def update():
    
    global wait_time
    if (wait_time > 1.0):
        wait_time = 0
        #game_framework.quit()
        if game_framework.life != 0:
            if game_framework.stage == 1:
                game_framework.change_state(map1)
            if game_framework.stage == 2:
                game_framework.change_state(map2)
            if game_framework.stage == 3:
                game_framework.change_state(map3)
        else:
            game_framework.change_state(title)
            game_framework.stage = 1
    delay(0.01)
    wait_time += 0.01

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
            game_framework.change_state(title)

def pause(): pass


def resume(): pass