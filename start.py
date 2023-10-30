from pico2d import *

# 캔버스 사이즈
w = 564
h = 1001

open_canvas(w, h)

st_back = load_image('start_back.png')

st_b = load_image('start_button.png')
exp = load_image('explain.jpg')
exp_b = load_image('explain_button.png')

st_back.draw_now(w//2, h//2)
st_b.draw_now(2*w//3, 2*h//5)
exp_b.draw_now(2*w//3, h//5)

x1, y1 = 0, 0
points = [x1, y1]

#설명창을 누른 상태인지 토글
ex_to = False

def handle_events():
    global clicking

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            clicking == False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            points[0], points[1] = event.x, h - 250 - event.y

clicking = True

while clicking:
    handle_events()

    # 트리거 설정이 없는데 설명 버튼을 눌렀을 때
    if ex_to == False:
        if 2 * w // 3 - 50 < points[0] < 2 * w // 3 + 50 and h // 5 - 50 < points[1] < h // 5 + 50:
            exp_b.draw_now(w//2, h//2) #설명창 띄우기
            ex_to = True #토글 키기

    # 트리거 설정이 눌렸는데 설명 버튼을 눌렀을 때
    elif ex_to == True:
        if 2*w//3 - 50 < points[0] < 2*w//3 + 50 and h//5 - 50 < points[1] < h//5 + 50:
            update_canvas() #설명창 지우기?
            ex_to = False #토글 끄기

    if points[0] == 2*w//3 and points[1] == 2*h//5: #시작 버튼을 눌렀을 때
        pass #시작하기