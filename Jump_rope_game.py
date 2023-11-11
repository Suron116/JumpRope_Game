from pico2d import get_events, SDL_QUIT
import game_type

running = True


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

while running:
    game_type.start()
    game_type.level.level1()


