from pico2d import load_image, delay, clear_canvas, update_canvas


#####   움직이지 않는 이미지들    #####


# 시직 화면 (1회 호출)
def start_img(w, h):
    st_back = load_image('start_back.png')
    st_b = load_image('start_button.png')

    st_back.draw_now(w // 2, h // 2)
    st_b.draw_now(w // 2, h // 3)


# 레벨 별 배경화면 (1회 호출)
class level_background:

    @staticmethod
    def level1_back(w, h):
        lev1_back = load_image('level_1.png')
        lev1_back.draw_now(w // 2, h // 2)

    @staticmethod
    def level2_back(w, h):
        lev2_back = load_image('level_2.png')
        lev2_back.draw_now(w // 2, h // 2)

    @staticmethod
    def level3_back(w, h):
        lev3_back = load_image('level_3.png')
        lev3_back.draw_now(w // 2, h // 2)


# 줄 돌리는 사람 (n회 호출)
def two_roper(w, h):
    img = False
    if not img:
        roper1 = load_image('roping1.png')
        roper2 = load_image('roping2.png')
        img = True

    roper1.draw_now(w // 2, 5 * h // 7)
    roper2.draw_now(w // 2, h // 7)


#####   움직이는 이미지들   #####


# n회 호출
def get_rope():
    img = False

    if not img:
        b_rope = load_image('back_rope.png')
        f_rope = load_image('front_rope.png')
        img = True

    two_roper(w, h)
    frame = 0

    # 700x150
    while True:
        clear_canvas()

        level_background.level1_back(w, h)
        two_roper(w, h)

        b_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 4 * h // 7, 2 * w // 3, h // 3)
        f_rope.clip_draw(frame * 140, 0, 93, 150, w // 2, 2 * h // 7, 2 * w // 3, h // 3)

        update_canvas()

        frame = (frame + 1) % 5
        delay(0.13)
