from pico2d import *
import game_framework
#from pad import *
import game_world
import title
import next_world
import gameover
import time
import random
speed = 5

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
can_move2 = 1

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
limit_time = 250
time_limit = 250
map1_bgm = None
die_bgm = None
jump_bgm = None
clear_bgm = None
Fire_bgm = None
monster_bgm = None
item_bgm = None
box_bgm = None
coin_bgm = None
ghost = None
clear_state = 0
pad_list = []
monster_list = []
box_list = []
ghost_list = []

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
   
        #draw_rectangle(*self.get_bb())

    def height(self):
        global ground
        global highjump, jumping
        highjump = 1
        jump_bgm.play()
        ground += 40 
        jumping = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def obj_y(self):
        return self.y + 20
class Sky:
    image = None
    def __init__(self):
        if Sky.image == None:
            Sky.image = load_image('map3.png')
        

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


def arrow_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.arrow()
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
        self.wait_time = 0
        
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
        #draw_rectangle(*self.get_bb())
        self.font.draw(1300, 1000, 'time: %3.2f' % (time_limit - (get_time() - self.start_time)), (0, 152, 0))
        self.font.draw(100, 1000, 'point: %05d' % (point * 10), (0, 152, 0))
        self.font.draw(600, 1000, 'life: %d   stage: 1-1' % (game_framework.life), (0, 152, 0))

    def update(self):
        global low_jump, now, low_jump_y, jum, running, frame, highjump, jump, can_move, right, state, superright, x, next, moving, camera_move, superright, Delay, jumping, now
        global limit_time
        if limit_time >= 0:
            limit_time = (time_limit - (get_time() - self.start_time))
        else:
            limit_time = 0
        
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
                    if (self.wait_time > 3.0):
                        self.wait_time = 0
                        jum = 0
                        #game_framework.quit()
                        game_framework.change_state(gameover)
                    delay(0.01)
                    self.wait_time += 0.1
                    
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
                    jum = 0
                    jumping += 15
                    if jumping == 360:
                        jum = 1
                        jumping = 0
                        highjump = 0
                        jump = 0
                        low_jump = 0
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
                        jumping = 0
            
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
            if right == 1 and x > 0:
                x += dir * speed
            elif x <= 0:
                x = 1
            elif 0 < x < 800:
                x += dir * speed            
            elif move == 1: 
                moving += speed
            
    def fire_attack(self):
        global attack_state
        print('fire')
        Fire = fire(x, now, right)
        game_world.add_object(Fire, 0)
        attack_state = 0

    def die(self):
        global low_jump, now, low_jump_y, jum
        #self.die_bgm.play(1)
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
                
                if (self.wait_time > 3.0):
                    self.wait_time = 0
                    jum = 0
                    #game_framework.quit()
                    game_framework.change_state(gameover)
                delay(0.01)
                self.wait_time += 0.1
                
                print('die')
        
            
        
    def get_bb(self):
        return x - 20, now - 30, x + 20, now + 20


        
class monster_1:
    image = None
    def __init__(self, x, y, range = 200):
        self.x, self.y = x, y
        self.point = self.x
        if monster_1.image == None:
            monster_1.image = load_image('monster1.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 60
        self.side = 30
        self.rand = [1, -1]
        self.right = random.choice(self.rand)
        self.range = range
        global jum
    def update(self):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        if self.move > self.range:
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
        global mario_die, state, point, stop_attack, low_jump, hyper, die_bgm
        if mario_die == 0:
            if self.die == 1 and jum == 1 and  mario_y == self.height + self.y and self.x -self.side <= mario_x < self.x + self.side:
                self.die = 0
                monster_bgm.play()
                point += 3
                low_jump = 1
                jump_bgm.play()
            elif self.die ==1 and hyper == 0 and jum == 0 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:
                      
                    mario_die = 1
                    die_bgm.play(1)  
                    low_jump = 1       
            elif self.die ==1 and hyper == 0 and jum == 1 and mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1
                    die_bgm.play(1)
                    low_jump = 1
                    jump_bgm.play()
            elif attack_state == 2 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                self.die = 0
                monster_bgm.play()
                point += 3
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(75, 0, 75, 75, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 75, 75, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20

    def monster_die(self):
        self.die = 0
        monster_bgm.play(1)

class monster_2:
    image = None
    def __init__(self, x, y, range = 200):
        self.x, self.y = x, y
        if monster_2.image == None:
            monster_2.image = load_image('monster2.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.height = 80
        self.side = 30
        self.rand = [1, -1]
        self.right = random.choice(self.rand)
        self.hp = 2
        self.range = range
        global jum
    def update(self):
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        if self.move > self.range:
            self.right *= -1
            self.move = 0
        if self.right == 1:
            self.x += 2
            self.move +=2
        elif self.right == -1:
            self.x -= 2
            self.move +=2

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
                    die_bgm.play(1)
                    low_jump = 1
            elif self.die ==1 and jum == 1 and hyper == 0 and mario_y < self.height + self.y - 10 and self.x -self.side<= mario_x < self.x + self.side:
                if state == 1:
                    state = 0
                    hyper = 50
                else:    
                    mario_die = 1  
                    die_bgm.play(1)
                    low_jump = 1                
            elif attack_state == 2 and mario_y < self.height + self.y and self.x -self.side<= mario_x < self.x + self.side:
                self.die = 0
                monster_bgm.play()
                point += 3
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(75, 0, 75, 75, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 75, 75, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def monster_die(self):
        self.hp -= 1
        if self.hp == 0:
            self.die = 0
            monster_bgm.play(1)

class monster_3:
    image = None
    def __init__(self, x, y,range = 200):
        self.x, self.y = x, y
        if monster_3.image == None:
            monster_3.image = load_image('ghost.png')
        self.move = 0
        self.turn = 0
        self.die = 1
        self.speed = 2
        self.right = 1
        self.range = range
        global jum
    def update(self):
            if right == 3 and camera_move < moving:
                self.x = self.x - speed
            if self.move > self.range:
                self.right *= -1
                self.move = 0
            if self.right == 1:
                self.x += self.speed
                self.move += self.speed
            elif self.right == -1:
                self.x -= self.speed
                self.move += self.speed
            self.speed = 2

    def draw(self, mario_x, mario_y):
        if self.die == 1:
            if self.right == 1:
                self.image.clip_draw(38, 0, 38, 38, self.x, self.y)
            else:
                self.image.clip_draw(0, 0, 38, 38, self.x, self.y)

        #draw_rectangle(*self.get_bb())
        #draw_rectangle(*self.arrow())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def arrow(self):
        return self.x - 150, self.y - 150, self.x + 150, self.y + 150

    def mario_kill(self):
        global mario_die, state, point, stop_attack, low_jump, hyper
        if hyper == 0:
            if state == 1:
                state = 0
                hyper = 50
            elif mario_die == 0:    
                mario_die = 1
                die_bgm.play(1)  
                low_jump = 1

    def arrow_mario(self):
        self.move = 0
        if right == 3 and self.right == -1 and x < self.x:
            self.speed = 0
        elif right == 1 and self.right == 1 and x > self.x:
            self.speed = 0
        else:
            if x < self.x:
                self.right = -1
                self.speed = 3.5
            else:
                self.right = 1
                self.speed = 3.5
            if y < self.y and self.y > ground:
                self.y = self.y - 3.5
            else:
                self.y = self.y + 3.5

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
            item_bgm.play(1)
            point += 10 
            state = 1
    def draw(self):
        
        if self. die == 0:
            self.image.draw(self.x, self.y)

        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20    

class item_2:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if item_2.image == None:
            item_2.image = load_image('item2.png')
        self.die = 0
    def update(self,mario_x, mario_y):
        global state
        global point
        global hyper
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            point += 10
            item_bgm.play() 
            state = 2
            hyper = 300
    
    def draw(self):
        if self. die == 0:
            self.image.draw(self.x, self.y)

        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

class coin:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if coin.image == None:
            coin.image = load_image('coin.png')
        self.die = 0
        #self.coin_bgm = load_music('coin.mp3')
        #self.coin_bgm.set_volume(32)
    def update(self,mario_x, mario_y):
        global state
        global point
        if right == 3 and camera_move < moving:
            self.x = self.x - speed
        
        if self.die == 0 and self.y <= mario_y <= self.y + 50 and self.x - 50 <= mario_x <= self.x + 50:
            self.die = 1
            coin_bgm.play(1)
            point += 2 
    def draw(self):
        
        if self. die == 0:
            self.image.draw(self.x, self.y)

        #draw_rectangle(*self.get_bb())

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
        #draw_rectangle(*self.get_bb())
    def update(self,mario_x, mario_y):
        global jum, high_jump, high_jump_y, jump
        if self.x - 40 <= mario_x <= self.x + 40 and self.y <= mario_y + 50 <= self.y + 20:
            jum = 1
            high_jump = 0
            high_jump_y = 0
            jump = 0
            if self.status == 2:
                self.status = 1
                box_bgm.play()
                box_item = item_1(self.x, self.y+50)
                game_world.add_object(box_item, 0)


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25
    def obj_y(self):
        return self.y +30


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
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 20
    
def clear_map():
    clear_bgm.play()
    time.sleep(2)
    game_framework.change_state(next_world)
    print('1 stage clear')


class flag:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if flag.image == None:
            flag.image = load_image('flag.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        #draw_rectangle(*self.get_bb())

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
    global attack_state
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
                
                if mario_die == 0 and highjump == 0 and low_jump == 0 and jump == 0 and ground - 20 <= now <= ground + 20:
                    jump_bgm.play()
                    jump = 1 
            elif event.key == SDLK_z:
                if state == 1:
                    attack_state = 2
                    Fire_bgm.play()
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title)
            elif event.key == SDLK_SPACE:
                pass

        elif event.type == SDL_KEYDOWN and mario_die == 1:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title)
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
    
    global sky, Mario, right, superright, state, before_state, can_move, running, x, frame, dir, y, ground, now, jump, jum, mario_die, point, mush_1, flower_1, star_1, turtle_1, ghost_1, pad_1, Fire, Coin, box1, attack_x, attack_y, attack, attack_state, stop_attack, low_jump, low_jump_y, high_jump, high_jump_y, hyper, Delay, change, move, moving, clear_state
    global can_move2, jumping, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16 , boxs1, pad_2, box2, boxs3, clear
    global map1_bgm, die_bgm, time_limit, jump_bgm, clear_bgm, Fire_bgm, monster_bgm, item_bgm, box_bgm, coin_bgm, pad_list, monster_list, box_list, ghost_list, ghost
    for boxs in box_list:
        del(boxs)
    for pads in pad_list:
        del(pads)
    for monsters in monster_list:
        del(monsters)

    pad_list = []
    monster_list = []
    box_list = []
    ghost_list = []

    jump_bgm = load_wav('jump.wav')
    jump_bgm.set_volume(16)
    clear_bgm = load_music('clear.mp3')
    clear_bgm.set_volume(32)
    Fire_bgm = load_wav('fire.wav')
    Fire_bgm.set_volume(64)
    monster_bgm = load_wav('monster.wav')
    monster_bgm.set_volume(32)
    item_bgm = load_wav('power.wav')
    item_bgm.set_volume(32)
    box_bgm = load_wav('box.wav')
    box_bgm.set_volume(32)
    coin_bgm = load_wav('coin.wav')
    coin_bgm.set_volume(32)
    die_bgm = load_music('gameover.mp3')
    die_bgm.set_volume(64)
    map1_bgm = load_music('map3.mp3')
    map1_bgm.set_volume(32)
    
    map1_bgm.repeat_play()
    
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
    mush_1 = [monster_1(4300+ i*200, 460 - i * 100, 10) for i in range(4)]
    for monsters in mush_1:
        monster_list.append(monsters)

    #flower_1 = item_1(3800, 500)
    #game_world.add_object(flower_1, 0)
    star_1 = item_2(1550, 450)
    game_world.add_object(star_1, 0)
    star_2 = item_2(6260, 80)
    game_world.add_object(star_2, 0)

    turtle_1 = [monster_2(1900 + i * 50, 80, 50) for i in range(5)]
    for monsters in turtle_1:
        monster_list.append(monsters)
    
    

    ghost = monster_3(1250, 200)
    ghost_list.append(ghost)
    ghost2 = monster_3(2900, 200)
    ghost_list.append(ghost2)
    ghost3 = monster_3(6300, 300)
    ghost_list.append(ghost3)
    ghost4 = monster_3(7200, 200)
    ghost_list.append(ghost4)

    pad_1 = pad(5100,200)
    pads1 = [pad(5100 + i * 350,200) for i in range(4)]
    pad_2 = pad(4860, 80)

    pad_list.append(pad_1)
    pad_list.append(pad_2)

    for pads in pads1:
        pad_list.append(pads)

    Coin = [coin(800 + i*50, 200) for i in range(7)]
    for money in Coin:
        game_world.add_object(money, 0)
    Coin2 = [coin(2700+ i*100, 200) for i in range(5) ]
    for money2 in Coin2:
        game_world.add_object(money2, 0)
    Coin3 = [coin(1850 + i * 150, 150) for i in range(3) ]
    for money3 in Coin3:
        game_world.add_object(money3, 0)
    Coin4 = [coin(5200 + i * 350, 400) for i in range(3) ]
    for money4 in Coin4:
        game_world.add_object(money4, 0)
    
    
    box1 = box(1700, 200, 1)
    box2 = box(1550, 150, 1)
    box3 = box(1400, 300, 1)
    box4 = box(2200, 200, 1)
    box5 = box(2400, 200, 1)
    box6 = box(2500, 50, 1)
    box7 = box(5100, 150, 1)
    boxs1 = [box(800+ i*50, 150, 1) for i in range(7)]

    boxs2 = [box(3300+ i*150, 100 + i * 100, 1) for i in range(5)]

    boxs3 = [box(5100 + 350 * i, 150, 1) for i in range(4)]

    boxs4 = [box(4100+ i*200, 500 - i * 100, 1) for i in range(5)]

    boxs5 = [box(6400 + 400 * i, 150, 1) for i in range(4)]
    boxs6 = [box(6600 + 400 * i, 260, 1) for i in range(4)]

    box_list = boxs1 + boxs2 + boxs4 + boxs3 + boxs5 + boxs6
    box_list.append(box1)
    box_list.append(box2)
    box_list.append(box3)
    box_list.append(box4)
    box_list.append(box5)
    box_list.append(box6)
    box_list.append(box7)
    

    out1 = 760
    out2 = 1170
    out3 = 1420
    out4 = 1830
    out5 = 2200
    out6 = 2620
    out7 = 3200
    out8 = 4800
    out9 = 4930
    out10 = 6220
    out11 = 6330
    out12 = 7620
    

    clear = flag(8000, 380)
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
    limit_time = 150
    time_limit = 150
    clear_state = 0
    print(mario_die, x, now)

def exit():
    global map1_bgm, box_list, pad_list, monster_list
    for boxs in box_list:
        del(boxs)
    for pads in pad_list:
        del(pads)
    for monsters in monster_list:
        del(monsters)
    game_world.clear()
    map1_bgm.stop()
    pass



def update():
    
    global sky, Mario, right, superright, state, before_state, can_move, running, x, frame, dir, y, ground, now, jump, jum, mario_die, point, mush_1, flower_1, star_1, turtle_1, ghost_1, pad_1, Fire, Coin, box1, attack_x, attack_y, attack, attack_state, stop_attack, low_jump, low_jump_y, high_jump, high_jump_y, hyper, Delay, change, move, moving, clear_state
    global can_move2, jumping, mario_die, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, boxs1, pad_2, box2, boxs3
    global secs, tm, sec, limit_time, can_move2
    
    if mario_die == 0 and limit_time < 0:
        mario_die = 1
        low_jump = 1
        limit_time = 300
        die_bgm.play(1)
        Mario.die()

    for ghosts in ghost_list:    
        if collide(ghosts, Mario):
            ghosts.mario_kill()
        if arrow_collide(ghosts, Mario):
            ghosts.arrow_mario()

    ground = 90
    if mario_die == 0 and now == 0:
        mario_die = 1
        low_jump = 1
        die_bgm.play(1)
        Mario.die()
    if collide(Mario, clear):
        if clear_state == 0:
            game_framework.stage = 4
            clear_map()
            clear_state = 1
    
    if out1 <= x <= out2 or out3 <= x <= out4 or out5 <= x <= out6 or out7 <= x <= out8 or out9 <= x <= out10 or out11 <= x <= out12:
        ground = 0
    if right == 3 and camera_move < moving:
        out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12 = out1-speed, out2-speed, out3-speed, out4-speed, out5-speed, out6-speed, out7-speed, out8-speed, out9-speed, out10-speed, out11-speed, out12-speed
    for pads in pad_list:
        for monsters in monster_list:
            if collide(monsters, pads):
                monsters.turn_move()

    
    for pads in pad_list:
        if leftright(Mario, pads) == False and now < pads.obj_y():
            x += speed * 1
            can_move2 = 0
        if rightleft(Mario, pads) == False and now < pads.obj_y():
            x -= speed * 1
            can_move2 = 0    
        if downup(Mario, pads) and leftandright(Mario, pads) :
            pads.height()

    for boxs in box_list:
        if leftright(Mario, boxs) == False and boxs.obj_y() + 25 > now >  boxs.obj_y() - 25:
            print(boxs.obj_y(), now)
            x += speed * 1
            can_move2 = 0
        if rightleft(Mario, boxs) == False and boxs.obj_y() + 25 > now >  boxs.obj_y() - 25:
            print(boxs.obj_y(), now)  
            x -= speed * 1
            can_move2 = 0 

        if now > boxs.obj_y() - 20 and leftandright(Mario, boxs):
            ground = boxs.obj_y() + 40

    for game_object in game_world.all_objects():
        for monsters in monster_list:
            if collide(game_object, monsters):
                monsters.monster_die()
                game_world.remove_object(game_object)
    #grass.draw(400, 30)
    #grass.draw(1200,30)
    #ghost_1.update(200,x,now,right)

    if attack_state == 2:
        Mario.fire_attack()

    for boxs in box_list:
        boxs.update(x, now)
    
    for monsters in monster_list:
        monsters.update()
    
    for ghosts in ghost_list:
        ghosts.update()

    for game_object in game_world.all_objects():
        game_object.update(x, now)
    #ghost.update()
    Mario.update()
    clear.update()
    #print(jump, jum, low_jump, highjump, jumping)
    if hyper > 0:
        hyper -= 1
    can_move2 = 1
        
def draw():
    clear_canvas()
    global sky, Mario, right, superright, state, before_state, can_move, running, x, frame, dir, y, ground, now, jump, jum, mario_die, point, mush_1, flower_1, star_1, turtle_1, ghost_1, pad_1, Fire, Coin, box1, attack_x, attack_y, attack, attack_state, stop_attack, low_jump, low_jump_y, high_jump, high_jump_y, hyper, Delay, change, move, moving
    global boxs1
    sky.draw()
    
    for monsters in monster_list:
        monsters.draw(x, now)
    for pads in pad_list:
        pads.draw(x, now)
    for boxs in box_list:
        boxs.draw(x, now)
    for ghosts in ghost_list:
        ghosts.draw(x, now)
    #ghost.draw(x, now)
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