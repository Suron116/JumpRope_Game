from pico2d import load_image, open_canvas


# 시직 화면 그리기
def start_img(w, h):
    st_back = load_image('start_back.png')
    st_b = load_image('start_button.png')
    exp = load_image('explain.jpg')

    st_back.draw_now(w // 2, h // 2)
    st_b.draw_now(w // 2, h // 3)


class level_background():



