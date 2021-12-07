from pico2d import *
import game_framework
#from pad import *
import game_world
import title
import time
speed = 20

ground_height = [[90] * 320]
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
now = 90
jump  = 0  #점프
jum = 0  #점프후 내려오기
mario_die = 0  #주인공 죽음
point = 0
mush_1 = None
flower_1 = None
star_1 = None
turtle_1 = None
ghost_1 = None
pad_1 = None
pad_2 = None
Fire = None
Coin = None
box1 = None
Mario = None
sky = None
#coin1 = None
attack = 0
attack_x = 0
attack_y = 0
attack_state = 0
stop_attack = 0
low_jump = 0
low_jump_y = 0
highjump = 0
highjump_y = 0
jumping = 0
hyper = 0
Delay = 0.01
change = 0
move = 0
moving = 0
camera_move = 0
can_move2 = 1
secs = time.time()
tm = time.localtime(secs)
sec = tm.tm_sec
limit_time = 300


class pad:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.jump = 0
        self.jum = 0
        if pad.image == None:
            pad.image = load_image('pad.png')
        
    def draw(self,mario_x, mario_y):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        global ground
        global highjump
        global can_move 
        self.image.draw(self.x, self.y)
   
        draw_rectangle(*self.get_bb())

    def height(self):
        global ground
        global highjump
        highjump = 1
        
        ground += 40 

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20

    def obj_y(self):
        return self.y + 20
class Sky:
    image = None
    def __init__(self):
        if Sky.image == None:
            Sky.image = load_image('map1.png')
        

    def draw(self):
        self.image.clip_draw(0 + moving,0 ,1600, 1024, 800,512)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def updown(a, b): #상하충돌
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return True
    if right_a < left_b: return True
    if top_a < bottom_b: return False
    if bottom_a > top_b: return True
    return True

def downup(a, b): #상하충돌
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return True
    if right_a < left_b: return True
    if top_a < bottom_b: return True
    if bottom_a > top_b: return False
    return True

def leftright(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    #print(left_a, right_b)
    if left_a == right_b: return False
    if right_a < left_b: return True
    if top_a < bottom_b: return True
    if bottom_a > top_b: return True
    return True

def rightleft(a,b):  
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    #print(right_a, left_b)
    if left_a > right_b: return True
    if right_a == left_b: return False
    if top_a < bottom_b: return True
    if bottom_a > top_b: return True
    return True

def leftandright(a,b): 
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return True
    if bottom_a > top_b: return True
    return True

class mario:
    def __init__(self):
        #self.x = 100, self.y = 90
        self.img = load_image('mario.png')
        self.img2 = load_image('supermario2.png')
        self.img3 = load_image('death.png')
        self.img4 = load_image('supermario3.png')
        self.superframe = 0
        self.start_time = get_time()
        mario.font = load_font('ENCR10B.TTF', 30)
    def draw(self):
        if mario_die == 1:
            self.img3.draw(x, now)
        elif state == 0:
            self.img.clip_draw(frame * 75, 75 * right, 75, 75, x, now)
        elif state == 1:
            self.img4.clip_draw(frame * 75, 75 * right, 75, 75, x, now)
        elif state == 2:
            self.img2.clip_draw(self.superframe * 75, 75 * superright, 75, 75, x, now -5)
        draw_rectangle(*self.get_bb())
        self.font.draw(1300, 1000, 'time: %3.2f' % (300 - (get_time() - self.start_time)), (0, 152, 0))
        self.font.draw(100, 1000, 'point: %5d' % (point * 10), (0, 152, 0))


    def update(self):
        global low_jump, now, low_jump_y, jum, running, frame, highjump, jump, can_move, right, state, superright, x, next, moving, camera_move, superright, Delay, jumping, now
        global limit_time
        limit_time = (10 - (get_time() - self.start_time))
        
        if right == 3:
            superright = 0
        else:
            superright = 1
        if mario_die == 1:
            
            Delay = 0.05
            if low_jump == 1:
                now += 10
                low_jump_y += 10
            
            if low_jump_y == 70:
                jum = 1
                low_jump = 0
                low_jump_y = 0
            elif jum == 1:
                now -= 10
                if now < 0:
                    jum = 0
                    game_framework.change_state(title)
                    print('die')
        else:
            if low_jump == 1:
                self.superframe = 3
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    self.superframe = 3
                    now += 10
                    low_jump_y += 10
                    if now >= 120 + ground:
                        jum = 1
                        jumping += low_jump_y 
                        low_jump = 0
                        low_jump_y = 0
            elif highjump == 1:
                self.superframe = 3
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    now += 15
                    jumping += 15
                    if jumping == 360:
                        jum = 1
                        highjump = 0
            elif jum == 1:
                self.superframe = 3
                now -= 10
                jumping -= 10
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    if now == ground:
                        jum = 0
                        jump = 0
            
            elif jump == 1:
                self.superframe = 3
                now += 10
                jumping += 10
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    if jumping == 200:
                        jum = 1
                        jump = 0
                        jumping = 0
            
            elif now >= ground:
                self.superframe = 3
                now -= 10
                jumping = 0
                if right == 3:
                    frame = 6
                else:
                    frame = 3
                if can_move == 1:
                    if now == ground:
                        jum = 0
                        jump = 0

            else:
                if state == 2:
                    if superright == 1:
                        if dir == -1:
                            self.superframe = (self.superframe + 1) % 3 + 4
                        else:
                            self.superframe = 6
                    elif superright == 0:
                        if dir == 1:
                            self.superframe = (self.superframe + 1) % 3 
                        else:
                            self.superframe = 0
                    if hyper == 0:
                        state = 0
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
        camera_move = moving
        next = x + dir * 5
        if can_move2 == 1:
            if right == 1:
                x += dir * speed
            elif 0 < x < 800:
                x += dir * speed
            
            elif move == 1: 
                moving += speed
            
    def fire_attack(self):
        global attack_state
        Fire = fire(x, now, right)
        game_world.add_object(Fire, 1)
        attack_state = 0

    def die(self):
        global low_jump, now, low_jump_y, jum
        Delay = 0.05
        self.img3.draw(x, now)
        if low_jump == 1:
            now += 10
            low_jump_y += 10
            
        if low_jump_y >= 70:
            jum = 1
            low_jump = 0
            low_jump_y = 0
        elif jum == 1:
            now -= 10
            if now <= ground:
                jum = 0
                game_framework.change_state(title)
                print('die')
        
            
        
    def get_bb(self):
        return x - 20, now - 30, x + 20, now + 20


        
class monster_1:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.point = self.x
        if monster_1.image == None:
            monster_1.image = load_image('monster1.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 60
        self.side = 30
        self.right = 1
        global jum
    def update(self, range):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        if self.move > range:
            self.right *= -1
            self.move = 0
        if self.right == 1:
            self.x += 3
            self.move +=3
        elif self.right == -1:
            self.x -= 3
            self.move +=3

    def turn_move(self):
        #print('turn', self.right)
        self.right *= -1
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
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if monster_2.image == None:
            monster_2.image = load_image('monster2.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 80
        self.side = 30
        self.right = 1
        self.hp = 3
        global jum
    def update(self, range):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        if self.move > range:
            self.right *= -1
            self.move = 0
        if self.right == 1:
            self.x += 3
            self.move +=3
        elif self.right == -1:
            self.x -= 3
            self.move +=3

    def turn_move(self):
        #print('turn', self.right)
        self.right *= -1
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
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class monster_3:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if monster_3.image == None:
            monster_3.image = load_image('ghost.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 50
        self.side = 30
        self.right = 1
        self.mario = 0
        global jum
    def update(self, range,mario_x, mario_y, arrow):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
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

        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.arrow())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def arrow(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60


class item_1:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if item_1.image == None:
            item_1.image = load_image('item1.png')
        self.die = 0
    def update(self,mario_x, mario_y):
        global state
        global point
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 30 <= mario_x <= self.x + 30:
            self.die = 1
            point += 10 
            state = 1
    def draw(self):
        
        if self. die == 0:
            self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20    

class item_2:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if item_2.image == None:
            item_2.image = load_image('item2.png')
        self.die = 0
    def draw(self,mario_x, mario_y):
        global state
        global point
        global hyper
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 10 
            state = 2
            hyper = 300
        if self. die == 0:
            self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class coin:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if coin.image == None:
            coin.image = load_image('coin.png')
        self.die = 0

    def update(self,mario_x, mario_y):
        global state
        global point
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 2 
    def draw(self):
        
        if self. die == 0:
            self.image.draw(self.x, self.y)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
       

class box:
    image1 = None
    image2 = None
    def __init__(self, x, y, status):
        self.x, self.y = x, y
        self.status = status
        if box.image1 == None:
            box.image1 = load_image('box1.png')
        if box.image2 == None:
            box.image2 = load_image('box2.png')
    def draw(self,mario_x, mario_y):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
        if self.status == 1:
            self.image1.draw(self.x, self.y)
        elif self.status == 2:
            self.image2.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
    def update(self,mario_x, mario_y):
        global jum, high_jump, high_jump_y, jump
        if self.x - 30 <= mario_x <= self.x + 30 and self.y <= mario_y + 50 <= self.y + 20:
            jum = 1
            high_jump = 0
            high_jump_y = 0
            jump = 0
            if self.status == 2:
                self.status = 1
                box_item = item_1(self.x, self.y+50)
                game_world.add_object(box_item, 0)


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def obj_y(self):
        return self.y + 30


class fire:
    image = None               #오류있음
    def __init__(self, x, y, arrow):
        self.x, self.y = x, y
        if fire.image == None:
            fire.image = load_image('fire.png')
        self.die = 0
        self.range = 0
        self.attack = 0
        self.right = arrow

    def update(self, x, now):
        global attack_state 
        if self.right == 3:
            self.x += 20
        else:
            self.x -= 20
        self.range += 20

        if self.range == 300:
            
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20
    



class flag:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if flag.image == None:
            flag.image = load_image('flag.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed

    def get_bb(self):
        return self.x - 60, self.y - 340, self.x + 40, self.y + 350


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
            game_framework.quit()
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
                    attack_state = 1
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                pass

        elif event.type == SDL_KEYDOWN and mario_die == 1:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
                print(point)        
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
        if event.type == SDL_KEYUP and mario_die == 0 and can_move == 1:
            if event.key == SDLK_RIGHT:
                move = 0

def enter():
    
    global sky, Mario, right, superright, state, before_state, can_move, running, x, frame, dir, y, ground, now, jump, jum, mario_die, point, mush_1, flower_1, star_1, turtle_1, ghost_1, pad_1, Fire, Coin, box1, attack_x, attack_y, attack, attack_state, stop_attack, low_jump, low_jump_y, high_jump, high_jump_y, hyper, Delay, change, move, moving
    global can_move2, jumping, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16 , boxs1, pad_2, box2, boxs3, clear
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
    now = 90
    jump  = 0  #점프
    jum = 0  #점프후 내려오기
    mario_die = 0  #주인공 죽음
    point = 0
    mush_1 = monster_1(1700, 80)
    flower_1 = item_1(8000, 80)
    game_world.add_object(flower_1, 0)
    star_1 = item_2(2000, 80)
    turtle_1 = monster_2(5000,80)
    #ghost_1 = monster_3(3000,200)
    pad_1 = pad(8600,80)
    pad_2 = pad(9300, 80)
    Coin = [coin((i+3)*200, 200) for i in range(4)]
    for money in Coin:
        game_world.add_object(money, 0)
    
    box1 = box(3000, 150, 2)
    boxs1 = [box(5500+ i*50, 150, 1) for i in range(8)]
    boxs3 = [box(6000+ i*50, 300, 1) for i in range(5)]
    box2 = box(5950, 300, 2)
    out1 = 1400
    out2 = 1550
    out3 = 3160
    out4 = 3300
    out5 = 3880
    out6 = 4020
    out7 = 4220
    out8 = 4350
    out9 = 4540
    out10 = 4670
    out11 = 4840
    out12 = 4970
    out13 = 8710
    out14 = 9200
    out15 = 9420
    out16 = 9820

    clear = flag(11500, 380)
    Mario = mario()
    sky = Sky()
    attack = 0
    attack_x = 0
    attack_y = 0
    attack_state = 0
    stop_attack = 0
    low_jump = 0
    low_jump_y = 0
    highjump = 0
    highjump_y = 0
    jumping = 0
    hyper = 0
    Delay = 0.01
    change = 0
    move = 0
    moving = 0
    can_move2 = 1
    print(mario_die, x, now)

def exit():
    game_world.clear()
    pass



def update():
    
    global sky, Mario, right, superright, state, before_state, can_move, running, x, frame, dir, y, ground, now, jump, jum, mario_die, point, mush_1, flower_1, star_1, turtle_1, ghost_1, pad_1, Fire, Coin, box1, attack_x, attack_y, attack, attack_state, stop_attack, low_jump, low_jump_y, high_jump, high_jump_y, hyper, Delay, change, move, moving
    global can_move2, jumping, mario_die, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16 , boxs1, pad_2, box2, boxs3
    global secs, tm, sec, limit_time
    
    
    if mario_die == 0 and limit_time <= -80:
        mario_die = 1
        low_jump = 1
        Mario.die()
    
    ground = 90
    if now == 0:
        mario_die = 1
        low_jump = 1
        Mario.die()
    if collide(Mario, clear):
        state = 1
        game_framework.change_state(title)
        print('1 stage clear')
    
    if out1 <= x <= out2 or out3 <= x <= out4 or out5 <= x <= out6 or out7 <= x <= out8 or out9 <= x <= out10 or out11 <= x <= out12 or out13 <= x <= out14 or out15 <= x <= out16:
        ground = 0
    if right == 3 and camera_move < moving:
        out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16 = out1-speed, out2-speed, out3-speed, out4-speed, out5-speed, out6-speed, out7-speed, out8-speed, out9-speed, out10-speed, out11-speed, out12-speed, out13-speed, out14-speed, out15-speed, out16-speed
    if collide(mush_1, pad_1):
        mush_1.turn_move()
    if collide(Mario, flower_1):
        state = 1
    if leftright(Mario, pad_1) == False and now < pad_1.obj_y():
        x += 5
        can_move2 = 0
    if rightleft(Mario, pad_1) == False and now < pad_1.obj_y():
        x -= 5
        can_move2 = 0    
    if downup(Mario, pad_1) and leftandright(Mario, pad_1) :
        pad_1.height()

    if leftright(Mario, pad_2) == False and now < pad_2.obj_y():
        x += 5
        can_move2 = 0
    if rightleft(Mario, pad_2) == False and now < pad_2.obj_y():
        x -= 5
        can_move2 = 0    
    if downup(Mario, pad_2) and leftandright(Mario, pad_2) :
        pad_2.height()

    if leftright(Mario, box1) == False and now < box1.obj_y() + 40 and now + 75 >  box1.obj_y() - 20:
        x += 5
        can_move2 = 0
    if rightleft(Mario, box1) == False and now < box1.obj_y() + 40 and now + 75 >  box1.obj_y() - 20:  
        x -= 5
        can_move2 = 0 
    
    if now > box1.obj_y() and leftandright(Mario, box1):
        ground = box1.obj_y() + 30


    if leftright(Mario, box2) == False and now < box2.obj_y() + 40 and now + 75 >  box2.obj_y() - 20:
        x += 5
        can_move2 = 0
    if rightleft(Mario, box2) == False and now < box2.obj_y() + 40 and now + 75 >  box2.obj_y() - 20:  
        x -= 5
        can_move2 = 0 
    
    if now > box2.obj_y() and leftandright(Mario, box2):
        ground = box2.obj_y() + 30

        
    for boxs2 in boxs1:
        if leftright(Mario, boxs2) == False and now < boxs2.obj_y() + 40 and now + 75 >  boxs2.obj_y() - 20:
            x += 5
            can_move2 = 0
        if rightleft(Mario, boxs2) == False and now < boxs2.obj_y() + 40 and now + 75 >  boxs2.obj_y() - 20:  
            x -= 5
            can_move2 = 0 
    
        if now > boxs2.obj_y() and leftandright(Mario, boxs2):
            ground = boxs2.obj_y() + 30


    for boxs4 in boxs3:
        if leftright(Mario, boxs4) == False and now < boxs4.obj_y() + 40 and now + 75 >  boxs4.obj_y() - 20:
            x += 5
            can_move2 = 0
        if rightleft(Mario, boxs4) == False and now < boxs4.obj_y() + 40 and now + 75 >  boxs4.obj_y() - 20:  
            x -= 5
            can_move2 = 0 
    
        if now > boxs4.obj_y() and leftandright(Mario, boxs4):
            ground = boxs4.obj_y() + 30

    #grass.draw(400, 30)
    #grass.draw(1200,30)
    #ghost_1.update(200,x,now,right)

    if attack_state == 1:
        Mario.fire_attack(x, now, right)

    mush_1.update(200)
    turtle_1.update(300)
    box1.update(x, now)
    box2.update(x, now)
    for boxs2 in boxs1:
        boxs2.update(x, now)

    for boxs4 in boxs3:
        boxs4.update(x, now)
    

    secs = time.time()
    tm = time.localtime(secs)
    sec = tm.tm_sec
    if sec != tm.tm_sec:
        limit_time -= 1
        print(limit_time)

    for game_object in game_world.all_objects():
        game_object.update(x, now)

    Mario.update()
    clear.update()
    if hyper > 0:
        hyper -= 1
    
       
    
    else:
        can_move2 = 1
        
def draw():
    clear_canvas()
    global sky, Mario, right, superright, state, before_state, can_move, running, x, frame, dir, y, ground, now, jump, jum, mario_die, point, mush_1, flower_1, star_1, turtle_1, ghost_1, pad_1, Fire, Coin, box1, attack_x, attack_y, attack, attack_state, stop_attack, low_jump, low_jump_y, high_jump, high_jump_y, hyper, Delay, change, move, moving
    global boxs1
    sky.draw()
    
    mush_1.draw(x , now)
    
    star_1.draw(x,now)
    turtle_1.draw(x, now)
    #ghost_1.draw(x,now)
    pad_1.draw(x, now)
    pad_2.draw(x, now)
    box2.draw(x, now)
    for boxs2 in boxs1:
        boxs2.draw(x, now)
    for boxs4 in boxs3:
        boxs4.draw(x, now)
    Mario.draw()
    #boxs1.draw(x, now)

    clear.draw()    
    for game_object in game_world.all_objects():
        game_object.draw()
    

    handle_events()       

    update_canvas()
    
    #if 
    
    delay(Delay)






def pause(): pass


def resume(): pass