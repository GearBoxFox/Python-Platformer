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

'''
Variables
'''

worldx = 960
worldy = 720

fps = 40  # frame rate
ani = 4  # animation cycles

main = True

ALPHA = (255, 255, 255)

# put variables here

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.health = 10  # keep track of hp
        self.images = []

        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player
        """

        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex

        self.rect.y = self.rect.y + self.movey

        # Moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # Moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        # Touching enemy
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)

        for enemy in hit_list:
            self.health -= 1
            print(self.health)


class Enemy(pygame.sprite.Sprite):
    '''
    Spawns an enemy
    '''

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # counter variable

    def move(self):
        '''
        enemy movement
        '''
        distance = 80
        speed = 8

        if 0 <= self.counter <= distance:
            self.rect.x += speed
            self.image = pygame.transform.flip(self.image, False, False)
        elif distance <= self.counter <= distance * 2:
            self.rect.x -= speed
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.counter = 0

        self.counter += 1


class Level():
    def bad(self, lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'ImpVanillaWalk1.png')  # spawns an enemy
            enemy_list = pygame.sprite.Group()  # creates enemy group
            enemy_list.add(enemy)

        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

    def ground(self, lvl, x, y, w, h):
        ground_list = pygame.sprite.Group()
        if lvl == 1:
            ground = Platform(x, y, w, h, 'GrassGround.png')
            ground_list.add(ground)
        if lvl == 2:
            print("Level " + str(lvl))

    def platform(self, lvl):
        plat_list = pygame.sprite.Group()
        if lvl == 1:
            plat = Platform(200, worldy-97-128, 285, 67, "GrassGround.png")
            plat_list.add(plat)
            plat = Platform(500, worldy-97-320, 197, 54, "GrassGround.png")
            plat_list.add(plat)

# X location, Y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha(self)
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc



# put Python classes and functions here

'''
Setup
'''

clock = pygame.time.Clock()  # set up the clock for the game
pygame.init()  # initiate the game code

world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move

eloc = []
eloc = [300, 0]
enemy_list = Level.bad(1, 1, eloc)

# put run-once code here

'''
Main Loop
'''

while main:
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
    enemy_list.draw(world) # refresh enemy
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)



# put game loop here
