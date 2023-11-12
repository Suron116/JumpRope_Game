from pico2d import *
import Img

# 캔버스 사이즈
w = 564
h = 1001
open_canvas(w, h)

lev1 = False


click = 0
def handle_events():
    global starting
    global click

    global lev1

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click += 1
        elif event.type == SDLK_z:
            pass

def start():

    Img.start_img(w, h)
    exp = load_image('explain.jpg')

    global level1
    starting = True

    clicking_one = False

    while starting:
        handle_events()

        if click == 1 and not clicking_one:
            exp.draw_now(w // 2, h // 2)
            # 무한 루프를 막기 위함
            clicking_one = True
        elif click == 2:
            return 0


class level:

    @staticmethod
    def level1():

        global lev1
        lev1 = True

        while lev1:
            handle_events()
            Img.draw_rope(w, h)
            pass