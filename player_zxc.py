from pico2d import load_image, delay, update_canvas


class Players:
    @staticmethod
    def player_z(w, h, jump_z):
        global img
        img = False

        if not img:
            play_z = load_image('z_character.png')
            img = True

        # 점프 높이 변경
        jump_hight = 30

        # 125x150
        if not jump_z:
            play_z.draw_now(w // 2, h // 2)
        else:
            for x in range(jump_hight):
                play_z.draw_now(w // 2, h // 2 + x)
                update_canvas()
                delay(0.01)
            for x in range(jump_hight):
                play_z.draw_now(w // 2, h // 2 + jump_hight - x)
                update_canvas()
                delay(0.01)

    @staticmethod
    def player_zx(w, h, jump_z, jump_x):
        global img2
        img2 = False

        if not img2:
            play_z = load_image('z_character.png')
            play_x = load_image('x_charecter.png')
            img2 = True

        # 점프 높이 변경
        jump_hight = 30

        # 125x150
        if not jump_z:
            play_z.draw_now(w // 3, h // 2)
        else:
            play_x.draw_now(2 * w // 3, h // 2)
            for x in range(jump_hight):
                play_z.draw_now(w // 3, h // 2 + x)
                update_canvas()
                delay(0.01)
            for x in range(jump_hight):
                play_z.draw_now(w // 3, h // 2 + jump_hight - x)
                update_canvas()
                delay(0.01)

        if not jump_x:
            play_x.draw_now( 2 * w // 3, h // 2)
        else:
            for x in range(jump_hight):
                play_x.draw_now( 2 * w // 3, h // 2 + x)
                update_canvas()
                delay(0.01)
            for x in range(jump_hight):
                play_x.draw_now(2 * w // 3, h // 2 + jump_hight - x)
                update_canvas()
                delay(0.01)

    @staticmethod
    def player_zxc(w, h, jump_z, jump_x, jump_c):
        global img3
        img3 = False

        if not img3:
            play_z = load_image('z_character.png')
            play_x = load_image('x_charecter.png')
            play_c = load_image('c_character.png')
            img3 = True

        # 점프 높이 변경
        jump_hight = 30

        # 125x150
        if not jump_z:
            play_z.draw_now(w // 7, h // 2)
        else:
            play_x.draw_now(w // 2, h // 2)
            play_c.draw_now(6 * w // 7, h // 2)
            for x in range(jump_hight):
                play_z.draw_now(w // 7, h // 2 + x)
                update_canvas()
                delay(0.01)
            for x in range(jump_hight):
                play_z.draw_now(w // 7, h // 2 + jump_hight - x)
                update_canvas()
                delay(0.01)

        if not jump_x:
            play_x.draw_now(w // 2, h // 2)
        else:
            play_c.draw_now(6 * w // 7, h // 2)
            for x in range(jump_hight):
                play_x.draw_now(w // 2, h // 2 + x)
                update_canvas()
                delay(0.01)
            for x in range(jump_hight):
                play_x.draw_now(w // 2, h // 2 + jump_hight - x)
                update_canvas()
                delay(0.01)

        if not jump_c:
            play_c.draw_now(6 * w // 7, h // 2)
        else:
            for x in range(jump_hight):
                play_c.draw_now(6 * w // 7, h // 2 + x)
                update_canvas()
                delay(0.01)
            for x in range(jump_hight):
                play_c.draw_now(6 * w // 7, h // 2 + jump_hight - x)
                update_canvas()
                delay(0.01)