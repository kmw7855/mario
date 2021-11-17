import game_framework
import pico2d
#import mario
import start_state


pico2d.open_canvas(1600, 1024)
game_framework.run(start_state)
pico2d.close_canvas()