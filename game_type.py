from pico2d import (close_canvas, get_events, load_image, clear_canvas, update_canvas, delay, load_wav,
                    SDL_QUIT, SDL_MOUSEBUTTONDOWN, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_z, SDLK_x, SDLK_c)
import Img
import player_zxc

#global jump_s
#jump_s = load_wav('MP_Jump.wav')

# 루프 돌아서 빼놔야 무한 0 리셋 안됨
click = 0
cnt = 0
cnt2 = 0
cnt3 = 0

def handle_events():
    global jump_z
    jump_z = False

    global jump_x
    jump_x = False

    global jump_c
    jump_c = False

    global cnt
    global cnt2
    global cnt3

    global click

    #global jump_s

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
            jump_z = True
            #jump_s.sound.set_volume(30)
            #jump_s.play()
            cnt += 1
            # print(cnt)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            jump_x = True
            cnt2 += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            jump_c = True
            cnt3 += 1


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

        global cnt
        global frame
        frame = 0

        while True:
            handle_events()

            # 700x150
            clear_canvas()

            Img.level_background.level1_back(w, h)
            Img.two_roper(w, h)

            b_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 4 * h // 7, 2 * w // 3, h // 3)
            f_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 2 * h // 7, 2 * w // 3, h // 3)
            player_zxc.Players.player_z(w, h, jump_z)
            frame = (frame + 1) % 5

            update_canvas()
            delay(0.13)

            if cnt > 9:
                cnt = 0
                return 0

    @staticmethod
    def level2(w, h):
        # 줄 이미지 다운
        b_rope = load_image('back_rope.png')
        f_rope = load_image('front_rope.png')

        global cnt
        global frame
        frame = 0

        while True:
            handle_events()

            # 700x150
            clear_canvas()

            Img.level_background.level2_back(w, h)
            Img.two_roper(w, h)

            b_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 4 * h // 7, 2 * w // 3, h // 3)
            f_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 2 * h // 7, 2 * w // 3, h // 3)
            player_zxc.Players.player_zx(w, h, jump_z, jump_x)
            frame = (frame + 1) % 5

            update_canvas()
            delay(0.13)

            if cnt2 > 9:
                cnt = 0
                return 0

    @staticmethod
    def level3(w, h):
        # 줄 이미지 다운
        b_rope = load_image('back_rope.png')
        f_rope = load_image('front_rope.png')

        global cnt
        global frame
        frame = 0

        while True:
            handle_events()

            # 700x150
            clear_canvas()

            Img.level_background.level3_back(w, h)
            Img.two_roper(w, h)

            b_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 4 * h // 7, 2 * w // 3, h // 3)
            f_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 2 * h // 7, 2 * w // 3, h // 3)
            player_zxc.Players.player_zxc(w, h, jump_z, jump_x, jump_c)
            frame = (frame + 1) % 5

            update_canvas()
            delay(0.13)

            if cnt3 > 9:
                cnt = 0
                return 0

    @staticmethod
    def ending(w, h):
        while True:
            handle_events()
            Img.level_background.ending_back(w, h)