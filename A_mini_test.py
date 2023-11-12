from pico2d import *

w = 564
h = 1001
open_canvas(w, h)

play_z = load_image('z_character.png')

# 125x150
while True:
    clear_canvas()
    play_z.draw_now(w // 2, h // 2)
    update_canvas()
