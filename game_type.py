from pico2d import (close_canvas, get_events, load_image, clear_canvas, update_canvas, delay,
                    SDL_QUIT, SDL_MOUSEBUTTONDOWN, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_z)
import Img
import player_zxc

# 루프 돌아서 빼놔야 무한 0 리셋 안됨
click = 0


def handle_events():
    global jump
    jump = False

    global click

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

        # 줄 이미지 다운
        b_rope = load_image('back_rope.png')
        f_rope = load_image('front_rope.png')

        while True:
            handle_events()

            Img.two_roper(w, h)
            frame = 0
            frame = (frame + 1) % 5

            # 700x150
            clear_canvas()

            Img.level_background.level1_back(w, h)
            Img.two_roper(w, h)

            b_rope.clip_draw(frame * 140, 0, 100, 150, w // 2, 4 * h // 7, 2 * w // 3, h // 3)
            player_zxc.Players.player_z(w, h, jump)
            f_rope.clip_draw(frame * 140, 0, 100, 150, w // 2, 2 * h // 7, 2 * w // 3, h // 3)

            update_canvas()


            delay(0.13)

