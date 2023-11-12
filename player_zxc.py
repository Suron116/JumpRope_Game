from pico2d import load_image, clear_canvas, delay


class Players:
    @staticmethod
    def player_z(w, h, jump):
        play_z = load_image('z_character.png')

        # 점프 높이 변경
        jump_hight = 30
        # 125x150
        while True:
            if not jump:
                play_z.draw_now(w // 2, h // 2)
            else:
                for x in range(jump_hight):
                    play_z.draw_now(w // 2, h // 2 + x)
                    clear_canvas()
                    delay(0.01)
                for x in range(jump_hight):
                    play_z.draw_now(w // 2, h // 2 + jump_hight - x)
                    clear_canvas()
                    delay(0.01)
