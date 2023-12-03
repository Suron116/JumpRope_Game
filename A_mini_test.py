from pico2d import load_image, open_canvas, delay

w = 564
h = 1001
open_canvas(w, h)
# 시직 화면 (1회 호출)

st_back = load_image('start_back.png')
st_b = load_image('start_button.png')

st_back.draw(w // 2, h // 2)
st_b.draw(w // 2, h // 3)

delay(100)