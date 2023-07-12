import pygame
from Variables import worldx, worldy
from pygame import draw, color, Rect, freetype

freetype.init()


def run(window):
    startgame = False
    window.fill("purple")

    # Generate a rectangle to draw
    startButton = Rect(worldx * 1/4, worldy * 1/2, worldx * 1/2, worldy * 1/4)

    while not startgame:
        # draw the startbutton rectangle
        draw.rect(window, (0, 0, 255), startButton, 0, 1)

        for event in pygame.event.get():
            # quit event for closing the window
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # on click
                x = event.x
                y = event.y

        pygame.display.flip()

