from pico2d import *

w = 564
h = 1001
open_canvas(w, h)

def handle_events():

    global jump
    jump = False

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            jump = True

play_z = load_image('z_character.png')

# 125x150
while True:
    handle_events()

    if not jump:
        play_z.draw_now(w // 2, h // 2)
    else:
        for x in range (20):
            play_z.draw_now(w // 2, h // 2 + x)
            clear_canvas()
            delay(0.01)
        for x in range(20):
            play_z.draw_now(w // 2, h // 2 + 20 - x)
            clear_canvas()
            delay(0.01)