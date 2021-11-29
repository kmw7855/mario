import game_framework
import pico2d
import test3
import start_state



pico2d.open_canvas(1600, 1024)
game_framework.run(start_state)
#game_framework.run(test3)
pico2d.close_canvas()