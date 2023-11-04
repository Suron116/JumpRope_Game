from pico2d import *

# 캔버스 사이즈
w = 564
h = 1001

open_canvas(w, h)

st_back = load_image('start_back.png')

st_b = load_image('start_button.png')
exp = load_image('explain.jpg')

st_back.draw_now(w//2, h//2)
st_b.draw_now(w//2, h//3)

click = 0
def handle_events():
    global starting
    global click
    global play

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            starting = False
            play = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click += 1

starting = True
saw_ex = False
while starting:
    handle_events()

    # 설명창 안봄
    if click == 1:
        exp.draw_now(w // 2, h // 2)
        saw_ex = True
    elif click == 2:
        play == True

play = False

while play:
    pass