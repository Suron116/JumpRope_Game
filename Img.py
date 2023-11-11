from pico2d import *

#####   움직이지 않는 이미지들    #####


# 시직 화면 그리기
def start_img(w, h):
    st_back = load_image('start_back.png')
    st_b = load_image('start_button.png')

    st_back.draw_now(w // 2, h // 2)
    st_b.draw_now(w // 2, h // 3)


# 레벨 별 배경화면
class level_background:

    @staticmethod
    def level1(w, h):
        lev1_back = load_image('level1_back.png')
        lev1_back.draw_now(w // 2, h // 2)

    @staticmethod
    def level2(w, h):
        lev2_back = load_image('level2_back.png')
        lev2_back.draw_now(w // 2, h // 2)

    @staticmethod
    def level3(w, h):
        lev3_back = load_image('level3_back.png')
        lev3_back.draw_now(w // 2, h // 2)


# 줄 돌리는 사람
def two_roper(w, h):
    roper1 = load_image('roping1.png')
    roper2 = load_image('roping2.jpg')
    roper1.draw_now(w // 2, 4 * h // 5)
    roper2.draw_now(w // 2, h // 5)


#####   움직이는 이미지들   #####


def draw_rope(w, h):
    b_rope = load_image('back_rope.png')
    f_rope = load_image('front_rope.jpg')
    b_rope.clip_draw(b_rope.frame * 100, b_rope.action * 100, 100, 150, w // 2, 4*h // 5)
    f_rope.clip_draw(f_rope.frame * 100, f_rope.action * 100, 100, 150, w // 2, h // 5)