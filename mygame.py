import game_framework
import pico2d
import test4
import map2
import start_state



pico2d.open_canvas(1600, 1024, sync = True)
#game_framework.run(start_state)
game_framework.run(map2)
pico2d.close_canvas()