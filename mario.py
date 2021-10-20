from pico2d import *

class monster_1:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('monster1.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 80
        self.side = 30
        self.right = 1
        global jum
    def update(self, range):
        self.frame = (self.frame + 1) % 8
        if self.move < range:
            self.right = 1
            self.x += 4
            self.move += 4
            self.turn += 4           
        else:
            self.right = 0
            self.x -= 4
            self.turn -= 4
            if self.turn < 0:
                self.move = 0

    def draw(self, mario_x, mario_y):
        global mario_die, state, point, stop_attack
        if jum == 1 and  mario_y == self.height + self.y and self.x -self.side <= mario_x < self.x + self.side:
            self.die = 0
            point += 3
        elif self.die ==1 and jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
            mario_die = 1
            state = 0
        elif self.die ==1 and jum == 1 and  mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
            mario_die = 1
            state = 0
        elif attack_state == 1 and self.y <attack_y < self.height + self.y and self.x -self.side <attack_x < self.side + self.x:
            self.die = 0
            point += 3
            stop_attack = 1
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(100, 0, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 100, 100, self.x, self.y)

class monster_2:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('monster2.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 80
        self.side = 30
        self.right = 1
        global jum
    def update(self, range):
        self.frame = (self.frame + 1) % 8
        if self.move < range:
            self.right = 1
            self.x += 2
            self.move += 2
            self.turn += 2           
        else:
            self.right = 0
            self.x -= 2
            self.turn -= 2
            if self.turn < 0:
                self.move = 0

    def draw(self, mario_x, mario_y):
        global mario_die, state, point, stop_attack
        if self.die ==1 and jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
            mario_die = 1
            state = 0
        elif self.die ==1 and jum == 1 and  mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
            mario_die = 1
            state = 0
        elif attack_state == 1 and self.y <attack_y < self.height + self.y and self.x -self.side <attack_x < self.side + self.x:
            self.die = 0
            point += 3
            stop_attack = 1
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(100, 0, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 100, 100, self.x, self.y)

class item_1:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('item1.png')
        self.die = 0
    def draw(self,mario_x, mario_y):
        global state
        global point
        if self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 10 
            state = 1
        if self. die == 0:
            self.image.draw(self.x, self.y)

class coin:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('coin.png')
        self.die = 0
    def draw(self,mario_x, mario_y):
        global state
        global point
        if self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 2 
        if self. die == 0:
            self.image.draw(self.x, self.y)


class fire:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('fire.png')
        self.die = 0
        self.range = 0
        self.attack = 0
        self.right = 0
    def shoot(self, x, y, arrow):
        self.x, self.y = x, y
        self.right = arrow
        self.range = 0
        self.attack = 1
    def update(self, stop_attack):
        if self.attack == 1:
            if stop_attack == 1:
                self.range = 300
            if self.right == 3:
                if self.range < 300:
                    self.x += 20
                    self.range += 20
                else:
                    self.attack = 0           
            else:
                if self.range < 300:
                    self.x -= 20
                    self.range += 20
                else:
                    self.attack = 0
            
    def draw(self):
        global attack_x, attack_y, attack_state
        if self.attack == 1:
            self.image.draw(self.x,self.y)
            attack_x,attack_y, attack_state = self.x, self.y, 1
        else:
            attack_state = 0


def handle_events():
    global running
    global dir
    global jump
    global right
    global attack
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
            elif event.key == SDLK_z:
                if state == 1:
                    attack = 1
            elif event.key == SDLK_ESCAPE:
                running = False
                print(point)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            


open_canvas()
grass = load_image('grass.png')
character = load_image('mario_not bg.png')
supermario = load_image('supermario2.png')
right = 3
superright = 0
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
point = 0
mush_1 = monster_1(200, 80)
flower_1 = item_1(700, 90)
turtle_1 = monster_2(400,80)
Fire = fire()
Coin = [coin((i+3)*100, 200) for i in range(4)]
attack = 0
attack_x = 0
attack_y = 0
attack_state = 0
stop_attack = 0

while running:
    clear_canvas()
    now = y+ground
    grass.draw(400, 30)
    Fire.update(stop_attack)
    mush_1.update(200)
    turtle_1.update(100)
    for money in Coin:
        money.draw(x, now)    
    mush_1.draw(x , now)
    flower_1.draw(x, now)
    turtle_1.draw(x, now)
    Fire.draw()
    if attack == 1:
        stop_attack = 0
        Fire.shoot(x, now, right)
        attack = 0
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
            character.clip_draw(frame * 100, 100 * right, 90, 90, x, 90)

        if mario_die == 1:
            point += 1

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
    elif state == 1:
        if right == 3:
            superright = 0
        else:
            superright = 1
        if jum == 1:
            y -= 10
            supermario.clip_draw(frame * 100, 100 * superright, 100, 100, x, 90 + y)
            if y == 0:
                jum = 0
    
        elif jump == 1:
            y += 10
            supermario.clip_draw(frame * 100, 100 * superright, 100, 100, x, 90 + y)
            if y == 200:
                jum = 1
                jump = 0
        else:
            supermario.clip_draw(frame * 100, 100 * superright, 90, 90, x, 90)

        if mario_die == 1:
            point += 1

        handle_events()
        if superright == 1:
            if dir == -1:
                frame = (frame + 1) % 3 + 4
            else:
                frame = 6
        elif superright == 0:
            if dir == 1:
                frame = (frame + 1) % 3 
            else:
                frame = 0
    update_canvas()
   
    x += dir * 5

    delay(0.05)

close_canvas()

