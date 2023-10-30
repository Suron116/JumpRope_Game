from pico2d import *

w = 564
h = 1001

open_canvas(w, h)

st_back = load_image('start_back.png')
st_b = load_image('start_button.png')
exp = load_image('explain.jpg')
exp_b = load_image('explain_button.png')

st_back.draw_now(w//2, h//2)

delay(3)