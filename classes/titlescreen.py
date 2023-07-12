import pygame
import Variables
from pygame import draw, color, Rect, freetype

freetype.init()


def run(window):
    startgame = False
    window.fill("purple")

    startButton = Rect(Variables.worldx * 1/4, Variables.worldy * 1/2, Variables.worldx * 1/2, Variables.worldy * 1/4)

    while not startgame:
        draw.rect(window, (0, 0, 255), startButton, 0, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.x
                y = event.y

        pygame.display.flip()

