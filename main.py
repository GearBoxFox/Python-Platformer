# !/usr/bin/env python 3
# by Logan Hollowood

# GPLv3
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the Lisense, or (at your option) any later version.

# This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY: without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public Lisense for more details.

import pygame  # load pygame keywords
import sys  # let python use your file system
import os  # help python identify your OS

import Variables

'''
Main Loop
'''

game = Variables.Setup()
game.setup()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump stop')
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world)  # draw the player
    enemy_list.draw(world)  # refresh enemy
    plat_list.draw(world)  # draw the platforms
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)

# put game loop here
