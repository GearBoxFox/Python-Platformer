import pygame
import os
from Variables import worldx, worldy, tx, font_path, font_size
from pygame import draw, mouse, Rect, freetype

freetype.init()


fontaquebold = freetype.Font(font_path, font_size)

def run(window):
    startgame = False
    window.fill("purple")

    # Generate a rectangle to draw
    startButton = Rect(worldx * 1/4, worldy * 1/2, worldx * 1/2, worldy * 1/4)

    while not startgame:
        # draw the startbutton rectangle
        draw.rect(window, (0, 0, 255), startButton, 0, 1)
        fontaquebold.render_to(window, (worldx * 1/2 - 200, 240), "Tux's Turmoil", (0, 0, 0), None, size=64)
        fontaquebold.render_to(window, (worldx * 1/4 + 80, worldy * 1/2 + 60), "Start Game", (255, 255, 255), None, size=64)

        for event in pygame.event.get():
            # quit event for closing the window
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # on click
                x = mouse.get_pos()[0]
                y = mouse.get_pos()[1]

                lowx = worldx * 1/4
                highx = (worldx * 1/4) + (worldx * 1/2)

                lowy = worldy * 1/2
                highy = (worldy * 1/2) + (worldy * 3/4)

                if (lowx <= x <= highx) and (lowy <= y <= highy):
                    startgame = True
        #end game loop

        pygame.display.flip()

