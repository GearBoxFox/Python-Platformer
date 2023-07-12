#!/usr/bin/env python 3
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
from classes import player, titlescreen


"""
Objects
"""

class Enemy(pygame.sprite.Sprite):
    """
    Spawns an enemy
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(Variables.ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # counter variable
        self.isJumping = True
        self.isFalling = False
        self.startX = x
        self.endX = x + 300
        self.direction = True

    def move(self):
        """
        enemy movement
        """
        # distance = 80
        # speed = 8
        #
        # if 0 <= self.counter <= distance:
        #     self.rect.x += speed
        #     self.image = pygame.transform.flip(self.image, False, False)
        # elif distance <= self.counter <= distance * 2:
        #     self.rect.x -= speed
        #     self.image = pygame.transform.flip(self.image, True, False)
        # else:
        #     self.counter = 0
        #
        # self.counter += 1

        # move right
        if self.rect.x < self.endX and self.direction:
            self.rect.x += 8

        # move left
        elif self.rect.x > self.startX and not self.direction:
            self.rect.x -= 8


        # reverse from far right
        elif self.rect.x >= self.endX and self.direction:
            self.direction = False
            self.image = pygame.transform.flip(self.image, True, False)

        # reverse from far left
        elif self.rect.x <= self.startX and not self.direction:
            self.direction = True
            self.image = pygame.transform.flip(self.image, True, False)

    def gravity(self):
        """
        Enemy gravity
        """

        if self.isJumping:
            self.rect.y += 20

        e_ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)

        # Ground collision for gravity
        for g in e_ground_hit_list:
            self.rect.bottom = g.rect.top
            self.isJumping = False  # Stop jumping


class Platform(pygame.sprite.Sprite):
    """
    Creates the bases of a platform
    """

    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(Variables.ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


class Level():
    """
    initializes enemy spawn locations
    """

    def bad(self, lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'ImpVanillaWalk1.png')  # spawns an enemy
            enemy_list = pygame.sprite.Group()  # creates enemy group
            enemy_list.add(enemy)

        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

    def ground(self, lvl, gloc, tx, ty):
        """
        sets up ground by using the earlier plaform class
        """
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], Variables.worldy - ty, tx, ty,
                                  'kenney_simplifiedPlatformer/PNG/Tiles/platformPack_tile001.png')
                ground_list.add(ground)
                i += 1

        if lvl == 2:
            print("Level " + str(lvl))

        return ground_list

    def platform(self, lvl, tx, ty):
        """
        sets up platforms
        """
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200, Variables.worldy - ty - 128, 3))
            ploc.append((300, Variables.worldy - ty - 256, 3))
            ploc.append((550, Variables.worldy - ty - 128, 4))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty,
                                    'kenney_simplifiedPlatformer/PNG/Tiles/platformPack_tile047.png')
                    plat_list.add(plat)
                    j = j + 1
                i = i + 1

            if lvl == 2:
                print("Level " + str(lvl))

            return plat_list

    def loot(self, lvl):
        tx = 60
        ty = 60
        if lvl == 1:
            loot_list = pygame.sprite.Group()
            loot = Platform(Variables.tx * 9, Variables.ty * 5, tx, ty, 'kenney_simplifiedPlatformer/PNG/Items'
                                                                        '/platformPack_item010.png')
            loot_list.add(loot)
            return loot_list


# put Python classes and functions here

clock = pygame.time.Clock()  # set up the clock for the game
pygame.init()  # initiate the game code

# generate ground
i = 0
while i <= (Variables.worldx / Variables.tx) + Variables.tx:
    Variables.gloc.append(i * Variables.tx)
    i = i + 1

# setup world and backdrop
world = pygame.display.set_mode([Variables.worldx, Variables.worldy])

backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()


# ground and platform lists
plat_list = Level.platform(1, 1, Variables.tx, Variables.ty)
ground_list = Level.ground(1, 1, Variables.gloc, Variables.tx, Variables.ty)

# enemy list
eloc = [300, 0]
enemy_list = Level.bad(1, 1, eloc)

# loot setup
loot_list = Level.loot(1, 1)

# setup player
player = player.Player(ground_list, plat_list, enemy_list, loot_list)  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move

# put run-once code here

titlescreen.run(world)

'''
Main Loop
'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        # handle keydown movement events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.jump()
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)

        # handle keyup movement events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    # Scroll the world forwards
    if player.rect.x >= Variables.forwardsx:
        scroll = player.rect.x - Variables.forwardsx
        player.rect.x = Variables.forwardsx

        # platforms
        for p in plat_list:
            p.rect.x -= scroll

        # enemies
        for e in enemy_list:
            e.startX -= scroll
            e.endX -= scroll
            e.rect.x -= scroll

        for l in loot_list:
            l.rect.x -= scroll

    # Scroll the world backwards
    if player.rect.x <= Variables.backwardsx:
        scroll = Variables.backwardsx - player.rect.x
        player.rect.x = Variables.backwardsx

        # platforms
        for p in plat_list:
            p.rect.x += scroll

        # enemies
        for e in enemy_list:
            e.startX += scroll
            e.endX += scroll
            e.rect.x += scroll

        for l in loot_list:
            l.rect.x += scroll

    # draw the world and run periodic updates
    world.blit(backdrop, backdropbox)

    player.gravity()
    player.update()

    for e in enemy_list:
        e.move()
        e.gravity()

    player_list.draw(world)  # draw the player
    enemy_list.draw(world)  # refresh enemy
    ground_list.draw(world)  # draw ground
    plat_list.draw(world)  # draw the platforms
    loot_list.draw(world)

    pygame.display.flip()
    clock.tick(Variables.fps)



# put game loop here
