import os

import pygame

import Variables
import classes.person


class Player(classes.person.Character):

    def __init__(self, ground_list, platform_list, hit_list, loot_list):
        super().__init__("hero1", ground_list, platform_list, hit_list, loot_list)

        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(Variables.ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def hitCharacter(self):
        hit_list = pygame.sprite.spritecollide(self, self.hit_list, False)
        loot_list = pygame.sprite.spritecollide(self, self.loot_list, True)

        for _ in hit_list:
            self.health -= 1

        for _ in loot_list:
            self.score += 1

