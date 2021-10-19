from pico2d import *

class monster_1:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('character.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 90
        self.side = 30
        global jum
    def update(self, range):
        self.frame = (self.frame + 1) % 8
        if self.move < range:
            self.x += 2
            self.move += 2
            self.turn += 2           
        else:
            self.x -= 2
            self.turn -= 2
            if self.turn < 0:
                self.move = 0

    def draw(self, mario_x, mario_y):
        global mario_die
        if jum == 1 and  mario_y == self.height + self.y and self.x -self.side <= mario_x < self.x + self.side:
            self.die = 0
        elif jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
            mario_die = 1
        elif jum == 1 and  mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
            mario_die = 1
        if self.die == 1:
            self.image.draw(self.x, self.y)


class item_1:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('item1.png')
        self.die = 0
    def draw(self,mario_x, mario_y):
        if self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
        if self. die == 0:
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
                right = 0
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
character = load_image('supermario2.png')
supermario = load_image('supermario.png')
right = 0
state = 0
running = True
x = 800 // 2
frame = 0
dir = 0
y = 0   #점프높이
ground = 90 #땅
now = y+ground
jump  = 0  #점프
jum = 0  #점프후 내려오기
mario_die = 0  #주인공 죽음
mush_1 = monster_1(200, 90)
flower_1 = item_1(700, 90)
point = 0

while running:
    clear_canvas()
    now = y+ground
    grass.draw(400, 30)
    mush_1.update(200)
    mush_1.draw(x , now)
    flower_1.draw(x, now)
    if state == 0:
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
            character.clip_draw(frame * 100, 100 * right, 100, 100, x, 90)

        if mario_die == 1:
            point += 1

    handle_events()
    if right == 1:
        if dir == -1:
            frame = (frame + 1) % 3 + 4
        else:
            frame = 6
    elif right == 0:
        if dir == 1:
            frame = (frame + 1) % 3 
        else:
            frame = 0
    update_canvas()
   
    x += dir * 5

    delay(0.05)

close_canvas()