import pygame
from pygame import draw, color, Rect, freetype

freetype.init()


def run(window):
    startgame = False
    window.fill("purple")

    while not startgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()

