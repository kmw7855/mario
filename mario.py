from pico2d import *


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
                right = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                right = 0
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
character = load_image('animation_sheet.png')
right = 1
running = True
x = 800 // 2
frame = 0
dir = 0
y = 0
jump  = 0
jum = 0
while running:
    clear_canvas()
    grass.draw(400, 30)
    
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
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5

    delay(0.01)

close_canvas()

