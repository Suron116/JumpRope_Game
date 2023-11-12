from pico2d import (open_canvas, close_canvas, get_events, load_image,
                    SDL_QUIT, SDL_MOUSEBUTTONDOWN, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_z)
import Img
import player_zxc

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

    global jump
    jump = False

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click += 1
        # 점프 키 입력
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            jump = True


def start(w, h):

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
    def level1(w, h):

        global lev1
        lev1 = True

        while lev1:
            handle_events()
            Img.draw_rope(w, h)
            player_zxc.players.player_z(w, h, jump)