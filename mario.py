from pico2d import *

class monster_1:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('character.png')
        self.move = 0
    def update(self, range):
        self.frame = (self.frame + 1) % 8
        if self.move < range:
            self.x += 5
            self.move += 5
        else:
            self.x -= 5
            if self .x < range * -1:
                self.move = 0

    def draw(self,x, y):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    global dir
    global jump
    global right
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                right = 3
            elif event.key == SDLK_LEFT:
                dir -= 1
                right = 1
            elif event.key == SDLK_UP:
                jump = 1 
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            


open_canvas()
grass = load_image('grass.png')
character = load_image('mario_not bg.png')
right = 3
running = True
x = 800 // 2
frame = 0
dir = 0
y = 0
jump  = 0
jum = 0
mush_1 = monster_1()

while running:
    clear_canvas()
    grass.draw(400, 30)
    mush_1.update(100)
    mush_1.draw(90,90)
    if jum == 1:
        y -= 10
        character.clip_draw(frame * 100, 100 * right, 100, 100, x, 90 + y)
        if y == 0:
            jum = 0
    
    elif jump == 1:
        y += 10
        character.clip_draw(frame * 100, 100 * right, 100, 100, x, 90 + y)
        if y == 200:
            jum = 1
            jump = 0
    else:
        character.clip_draw(frame * 100, 100 * right, 90, 90, x, 90)
    update_canvas()

    handle_events()
    if right == 3:
        if dir == 1:
            frame = (frame + 1) % 3 + 1
        else:
            frame = 0
    elif right == 1:
        if dir == -1:
            frame = (frame + 1) % 3 + 6
        else:
            frame = 9

    x += dir * 5

    delay(0.01)

close_canvas()

