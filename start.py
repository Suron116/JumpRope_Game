from pico2d import *
import Img

# 캔버스 사이즈
w = 564
h = 1001
open_canvas(w, h)

# 시작 이미지 불러오기
Img.start_img(w, h)

# 설명창
exp = load_image('explain.jpg')

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


#레벨1 배경 이미지 호출
Img.level_background.level1(w, h)
#줄 돌리는 사람 이미지
Img.two_roper(w, h)

#움직이는 로프 이미지
Img.draw_rope(w, h)


level1 = False

while level1:
    handle_events()

    #if