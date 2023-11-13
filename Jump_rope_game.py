from pico2d import open_canvas
import game_type

# 캔버스 사이즈
w = 564
h = 1001
open_canvas(w, h)

game_type.start(w, h)
game_type.Level.level1(w, h)


