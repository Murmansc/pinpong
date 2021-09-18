from pygame import * 
from ay import Player
from qq import GameSprite


def game():
    back = (200, 255, 255)
    win_width = 600
    win_height = 500
    window = display.set_mode((win_width, win_height))
    window.fill(back)

    run = True
    finish = False
    clock = time.Clock()
    FPS = 60
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
        display.update()
        clock.tick(FPS)
if __name__ == '__main__':
    game()