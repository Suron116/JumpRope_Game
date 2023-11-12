from pico2d import load_image, clear_canvas, update_canvas

class palyers:

    @staticmethod
    def player_z(w, h):
        play_z = load_image('z_character.png')

        # 125x150
        while True:
            clear_canvas()
            play_z.draw_now(w // 2, h // 2)
            update_canvas()