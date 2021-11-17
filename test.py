from pico2d import *

ground_height = [[90] * 320]
print(ground_height)

class grass:
    def __init__(self):
        self.img = load_image('cloud.jpg')

    def draw(self):
        self.img.clip_draw(0+moving,0 ,800, 600, 400,300)




class mario:
    def __init__(self):
        #self.x = 100, self.y = 90
        self.img = load_image('mario.png')
        self.img2 = load_image('supermario2.png')
        self.img3 = load_image('death.png')
        self.img4 = load_image('supermario3.png')


    def draw(self):
        if mario_die == 1:
            self.img3.draw(x, ground + y)
        elif state == 0:
            self.img.clip_draw(frame * 75, 75 * right, 75, 75, x, ground + y)
        elif state == 1:
            self.img4.clip_draw(frame * 75, 75 * right, 75, 75, x, ground + y)
        elif state == 2:
            self.img2.clip_draw(3 * 75, 75 * superright, 75, 75, x, ground + y -5)

    def update(self):
        global low_jump, y, low_jump_y, jum, running, frame, highjump, jump, can_move, right, state, superright, x, next, moving
        if mario_die == 1:
            if low_jump == 1:
                y += 10
                low_jump_y += 10
            
            if low_jump_y == 70:
                jum = 1
                low_jump = 0
                low_jump_y = 0
            elif jum == 1:
                y -= 10
                if y <= -90:
                    jum = 0
                    running = False
        else:
            if low_jump == 1:
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    y += 10
                    low_jump_y += 10
                    if low_jump_y == 70:
                        jum = 1
                        low_jump = 0
                        low_jump_y = 0
            elif highjump == 1:
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    y += 15
                    low_jump_y += 15
                    if low_jump_y == 360:
                        jum = 1
                        highjump = 0
                        low_jump_y = 0
            elif jum == 1:
                y -= 10
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    if y <= 0 or now == ground:
                        jum = 0
        
            elif jump == 1:
                y += 10
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    if y == 200:
                        jum = 1
                        jump = 0
            
            else:
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
        
        if state == 2:
            if right == 3:
                superright = 0
            else:
                superright = 1
           
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

        if hyper == 0:
            state = 0


        next = x + dir * 5
        x += dir * 5
        if move == 1:
            moving += 5


class monster_1:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('monster1.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 60
        self.side = 30
        self.right = 1
        global jum
    def update(self, range):
        if self.move < range:
            self.right = 1
            self.x += 3
            self.move += 3
            self.turn += 3           
        else:
            self.right = 0
            self.x -= 3
            self.turn -= 3
            if self.turn < 0:
                self.move = 0

    def draw(self, mario_x, mario_y):
        global mario_die, state, point, stop_attack, low_jump, hyper
        if mario_die == 0:
            if self.die == 1 and jum == 1 and  mario_y == self.height + self.y and self.x -self.side <= mario_x < self.x + self.side:
                self.die = 0
                point += 3
                low_jump = 1
            elif self.die ==1 and hyper == 0 and jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1  
                    low_jump = 1       
            elif self.die ==1 and hyper == 0 and jum == 1 and mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1
                    low_jump = 1
            elif attack_state == 1 and self.y <attack_y < self.height + self.y and self.x -self.side <attack_x < self.side + self.x:
                self.die = 0
                point += 3
                stop_attack = 1
            elif attack_state == 2 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                self.die = 0
                point += 3
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(75, 0, 75, 75, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 75, 75, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20


class monster_2:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('monster2.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 80
        self.side = 30
        self.right = 1
        self.hp = 3
        global jum
    def update(self, range):
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
        global mario_die, state, point, stop_attack, low_jump, hyper
        if mario_die == 0:
            if self.die ==1 and hyper == 0 and jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1  
                    low_jump = 1
            elif self.die ==1 and jum == 1 and hyper == 0 and mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1  
                    low_jump = 1
            elif attack_state == 1 and hyper == 0 and self.y <attack_y < self.height + self.y and self.x -self.side <attack_x < self.side + self.x:
                self.hp -= 1
                stop_attack = 1
                if self.hp == 0:
                    self.die = 0
                    point += 3                
            elif attack_state == 2 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                self.die = 0
                point += 3
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(75, 0, 75, 75, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 75, 75, self.x, self.y)

class monster_3:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('ghost.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 50
        self.side = 30
        self.right = 1
        self.mario = 0
        global jum
    def update(self, range,mario_x, mario_y, arrow):
        if arrow == 3:
            self.mario = 1
        elif arrow == 1:
            self.mario = 0
        if -300 < mario_x - self.x < 300 or -300 < mario_x - self.x < 300:
            if self.x < mario_x:
                self.right = 1
                if self.right == self.mario:
                    self.x += 3
                else:
                   pass 
            else:
                self.right = 0
                if self.right == self.mario:
                    self.x -= 3
                else:
                   pass 
            if self.y < mario_y:
                if self.right == self.mario:
                    self.y += 2
                else:
                   pass 
            else:
                if self.right == self.mario:
                    self.y -= 2
                else:
                   pass 
        elif self.move < range:
            self.right = 1
            self.x += 1.5
            self.move += 1.5
            self.turn += 2           
        else:
            self.right = 0
            self.x -= 1.5
            self.turn -= 1.5
            if self.turn < 0:
                self.move = 0

    def draw(self, mario_x, mario_y):
        global mario_die, state, point, stop_attack, low_jump, hyper
        if mario_die == 0:
            if self.die ==1 and hyper == 0 and jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1  
                    low_jump = 1
            elif self.die ==1 and jum == 1 and hyper == 0 and mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1  
                    low_jump = 1
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(38, 0, 38, 38, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 38, 38, self.x, self.y)

class item_1:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('item1.png')
        self.die = 0
    def draw(self,mario_x, mario_y):
        global state
        global point
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 30 <= mario_x <= self.x + 30:
            self.die = 1
            point += 10 
            state = 1
        if self. die == 0:
            self.image.draw(self.x, self.y)

class item_2:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = load_image('item2.png')
        self.die = 0
    def draw(self,mario_x, mario_y):
        global state
        global point
        global hyper
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 10 
            state = 2
            hyper = 300
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
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 2 
        if self. die == 0:
            self.image.draw(self.x, self.y)

class pad:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.jump = 0
        self.jum = 0
        self.image = load_image('pad.png')
    def draw(self,mario_x, mario_y):
        global ground
        global highjump
        global can_move 
        self.image.draw(self.x, self.y)
        if self.x - 35 <= mario_x <= self.x + 35:
            pass
        else:
            pass
        if self.y + 20 <= mario_y <= self.y + 40 and self.x - 30 <= mario_x <= self.x + 30:
            highjump = 1

    def height(self,mario_x, mario_y):
        global ground
        global y
        if self.x - 35 <= mario_x <= self.x + 35: 
        #and self.y <= mario_y <= self.y + 70:
            ground = 130
            

class box:
    def __init__(self, x, y, status):
        self.x, self.y = x, y
        self.status = status
        self.image1 = load_image('box1.png')
        self.image2 = load_image('box2.png')
    def draw(self,mario_x, mario_y):
        if self.status == 1:
            self.image1.draw(self.x, self.y)
        elif self.status == 2:
            self.image2.draw(self.x, self.y)
    def update(self,mario_x, mario_y):
        global jum, high_jump, high_jump_y, jump
        if self.x - 30 <= mario_x <= self.x + 30 and self.y <= mario_y + 70 <= self.y + 20:
            jum = 1
            high_jump = 0
            high_jump_y = 0
            jump = 0
            if self.status == 2:
                self.status = 1
    
    def height(self,mario_x, mario_y):
        global ground
        print(self.y, mario_y)
        if self.x - 35 <= mario_x <= self.x + 35 and self.y +30 < mario_y :
    
            ground = self.y + 50


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
    global move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and mario_die == 0 and can_move == 1:
            if event.key == SDLK_RIGHT:
                dir += 1
                right = 3
                move = 1
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
        elif event.type == SDL_KEYDOWN and mario_die == 1:
            if event.key == SDLK_ESCAPE:
                running = False
                print(point)        
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
        if event.type == SDL_KEYUP and mario_die == 0 and can_move == 1:
            if event.key == SDLK_RIGHT:
                move = 0
            


open_canvas(800, 600)
#grass = load_image('grass.png')
def enter():
    sky = load_image('cloud.jpg')
    character = load_image('mario.png')
    supermario = load_image('supermario2.png')
    diemario = load_image('death.png')
    firemario = load_image('supermario3.png')
    right = 3
    superright = 0
    state = 0
    before_state = 0
    can_move = 1
    running = True
    x = 1600 // 2
    frame = 0
    dir = 0
    y = 0   #점프높이
    ground = 90 #땅
    now = y+ground
    jump  = 0  #점프
    jum = 0  #점프후 내려오기
    mario_die = 0  #주인공 죽음
    point = 0
    mush_1 = monster_1(1000, 80)
    flower_1 = item_1(1000, 80)
    star_1 = item_2(1400, 80)
    turtle_1 = monster_2(1200,80)
    ghost_1 = monster_3(-2100,200)
    pad_1 = pad(900,80)
    Fire = fire()
    Coin = [coin((i+3)*200, 200) for i in range(4)]
    box1 = box(400, 200, 2)
    Mario = mario()
    attack = 0
    attack_x = 0
    attack_y = 0
    attack_state = 0
    stop_attack = 0
    low_jump = 0
    low_jump_y = 0
    highjump = 0
    highjump_y = 0
    hyper = 0
    Delay = 0.01
    change = 0

right = 3
superright = 0
state = 0
before_state = 0
can_move = 1
running = True
x = 300
frame = 0
dir = 0
y = 0   #점프높이
ground = 90 #땅
now = y+ground
jump  = 0  #점프
jum = 0  #점프후 내려오기
mario_die = 0  #주인공 죽음
point = 0
mush_1 = monster_1(500, 80)
flower_1 = item_1(1000, 80)
star_1 = item_2(1400, 80)
turtle_1 = monster_2(1200,80)
ghost_1 = monster_3(-2100,200)
pad_1 = pad(900,80)
Fire = fire()
Coin = [coin((i+3)*200, 200) for i in range(4)]
box1 = box(400, 200, 2)
Mario = mario()
sky = grass()
attack = 0
attack_x = 0
attack_y = 0
attack_state = 0
stop_attack = 0
low_jump = 0
low_jump_y = 0
highjump = 0
highjump_y = 0
hyper = 0
Delay = 0.01
change = 0
move = 0
moving = 0
Delay = 0.01

while running:
    ground = 90
    clear_canvas()
    now = y+ground
    sky.draw()
    
    print(moving)
    ghost_1.update(200,x,now,right)
    Fire.update(stop_attack)
    mush_1.update(500)
    turtle_1.update(300)
    box1.update(x, now)
    Mario.update()
    pad_1.height(x, now)
    box1.height(x,now)
    for money in Coin:
        money.draw(x, now)    
    mush_1.draw(x , now)
    flower_1.draw(x, now)
    star_1.draw(x,now)
    turtle_1.draw(x, now)
    ghost_1.draw(x,now)
    pad_1.draw(x, now)
    box1.draw(x, now)
    Mario.draw()
    Fire.draw()
    #now = y+ground
    if hyper > 0:
        hyper -= 1
    if attack == 1:
        stop_attack = 0
        Fire.shoot(x, now, right)
        attack = 0

    handle_events()       

    update_canvas()
    
    #if 
    
    delay(Delay)

close_canvas()

 