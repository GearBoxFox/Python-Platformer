import Variables
import pygame
import os
import sys
import Setup

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
            img.set_colorkey(Variables.ALPHA)
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
            if self.frame > 3 * Variables.ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // Variables.ani], True, False)

        # Moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * Variables.ani:
                self.frame = 0
            self.image = self.images[self.frame // Variables.ani]

        # Touching enemy
        hit_list = pygame.sprite.spritecollide(self, Setup.enemy_list, False)

        for enemy in hit_list:
            self.health -= 1
            print(self.health)


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

    def move(self):
        """
        enemy movement
        """
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


class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(Variables.ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


class Level():
    def bad(self, lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'ImpVanillaWalk1.png')  # spawns an enemy
            enemy_list = pygame.sprite.Group()  # creates enemy group
            enemy_list.add(enemy)

        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

    def ground(self, lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], Variables.worldy - ty, tx, ty, 'platformPack_tile001.png')
                ground_list.add(ground)
                i += 1

        if lvl == 2:
            print("Level " + str(lvl))

        return ground_list

    def platform(self, lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200, Variables.worldy - ty - 128, 3))
            ploc.append((300, Variables.worldy - ty - 256, 3))
            ploc.append((500, Variables.worldy - ty - 128, 4))
            while i < len(ploc):
                plat = Platform((ploc[i][0] + (i * tx)), ploc[i][1], tx, ty, 'kenney_simplifiedPlatformer/PNG/Tiles/platformPack_tile001.png')
                plat_list.add(plat)
                i = i + 1

            if lvl == 2:
                print("Level " + str(lvl))

            return plat_list


# put Python classes and functions here
