from pico2d import (open_canvas, close_canvas, get_events, load_image,
                    SDL_QUIT, SDL_MOUSEBUTTONDOWN, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_z)
import Img
import player_zxc

# 루프 돌아서 빼놔야 무한 0 리셋 안됨
global click
click = 0

def handle_events():
    global jump
    jump = False

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
        # 1회성 코드
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click += 1
        # 점프 키 입력
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            jump = True


def start(w, h):

    Img.start_img(w, h)
    exp = load_image('explain.jpg')

    clicking_one = False

    while True:
        handle_events()

        if click == 1 and not clicking_one:
            exp.draw_now(w // 2, h // 2)
            # 무한 루프를 막기 위함
            clicking_one = True
        elif click == 2:
            return 0


class Level:

    @staticmethod
    def level1(w, h):

        while True:
            handle_events()
            Img.get_rope()
            player_zxc.Players.player_z(w, h, jump)