from pico2d import open_canvas, load_music
import game_type

# 캔버스 사이즈
w = 564
h = 1001
open_canvas(w, h)

bgm = load_music('all_bgm.mp3')
bgm.set_volume(30)
bgm.repeat_play()

# 시작화면
#game_type.start(w, h)

# 레벨 1
#game_type.Level.level1(w, h)

#game_type.Level.level2(w, h)

game_type.Level.level3(w, h)

game_type.Level.ending(w, h)