from pico2d import *
import Img_no_change

# 캔버스 사이즈
w = 564
h = 1001

# 시작 이미지 불러오기
Img_no_change.start_img(w, h)
open_canvas(w, h)

click = 0

def handle_events():
    global starting
    global click
    global level1

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            starting = False
            level1 = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click += 1
        #elif event.type == SDLK_z

starting = True
saw_ex = False
while starting:
    handle_events()

    # 설명창 안봄
    if click == 1:
        exp.draw_now(w // 2, h // 2)
        saw_ex = True
    elif click == 2:
        level1 == True
        starting == False

#플레이 이미지
ropper1 = load_image('ropping1.png')
ropper2 = load_image('ropping2.jpg')

#움직이는 로프 이미지
b_rope = load_image('back_rope.png')
f_rope = load_image('front_rope.jpg')

#레벨 이미지
lev1_back = load_image('level1_back.png')

lev1_back.draw_now(w//2, h//2)
ropper1.draw_now(w//2, 4*h//5)
ropper2.draw_now(w//2, h//5)

level1 = False

while level1:
    handle_events()

    #if