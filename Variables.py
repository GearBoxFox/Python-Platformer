import Classes
import pygame
import os

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
Setup
'''


class Setup:
    def setup(self):
        clock = pygame.time.Clock()  # set up the clock for the game
        pygame.init()  # initiate the game code

        world = pygame.display.set_mode([worldx, worldy])
        backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
        backdropbox = world.get_rect()

        player = Classes.Player()  # spawn player
        player.rect.x = 0  # go to x
        player.rect.y = 0  # go to y
        player_list = pygame.sprite.Group()
        player_list.add(player)
        steps = 10  # how many pixels to move

        eloc = [300, 0]
        enemy_list = Classes.Level.bad(1, 1, eloc)

        gloc = []
        tx = 64
        ty = 64

        i = 0
        while i <= (worldx / tx) + tx:
            gloc.append(i * tx)
            i = i + 1

        ground_list = Classes.Level.ground(1, 0, worldy - 240, 800, 240)
        plat_list = Classes.Level.platform(1, 1, tx, ty)

        gloc = []
        tx = 64
        ty = 64

        i = 0
        while i <= (worldx / tx) + tx:
            gloc.append(i * tx)
            i = i + 1

        ground_list = Classes.Level.ground(i, gloc, tx, ty)

# put run-once code here
