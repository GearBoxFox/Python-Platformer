import os

import pygame

import Variables
import classes.person


class Player(classes.person.Character):

    def __init__(self, ground_list, platform_list, hit_list):
        super().__init__("hero1", ground_list, platform_list, hit_list)

        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(Variables.ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def hitCharacter(self):
        enemy_hit_list = pygame.sprite.spritecollide(self, self.hit_list, False)

        for enemy in enemy_hit_list:
            self.health -= 1
