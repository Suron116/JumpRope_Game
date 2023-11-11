from pico2d import *
import Img

# 캔버스 사이즈
w = 564
h = 1001
open_canvas(w, h)

def start():

    Img.start_img(w, h)
    exp = load_image('explain.jpg')

    def handle_events():
        global starting
        global click
        click = 0

        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN:
                click += 1

    starting = True

    while starting:
        handle_events()


        if click == 1:
            exp.draw_now(w // 2, h // 2)
        elif click == 2:
            starting = False

class level:

    @staticmethod
    def level1():
        Img.level_background.level1(w, h)
        Img.two_roper(w, h)
        Img.draw_rope(w, h)

        def handle_events():
            global level1

            events = get_events()
            for event in events:
                if event.type == SDLK_z:
                    pass

        level1 = False

        while level1:
            handle_events()
        pass