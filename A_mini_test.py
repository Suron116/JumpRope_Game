from pico2d import *

w = 564
h = 1001
open_canvas(w, h)


b_rope = load_image('back_rope.png')
f_rope = load_image('front_rope.png')

frame = 0

# 700x150
while True:
    clear_canvas()

    b_rope.clip_draw(frame * 100, 0, 100, 150, w // 2, 2*h // 3, 2*w//3, h//3)
    f_rope.clip_draw(frame * 100, 0, 100, 150, w // 2, 1*h // 3, 2*w//3, h//3)

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.1)