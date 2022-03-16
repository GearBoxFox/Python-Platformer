import Classes
import Variables
import pygame
import os


def setup():
    global world
    global backdrop
    global backdropbox
    global player
    global player_list
    global enemy_list
    global plat_list
    global ground_list
    global clock
    global steps

    clock = pygame.time.Clock()  # set up the clock for the game
    pygame.init()  # initiate the game code

    world = pygame.display.set_mode([Variables.worldx, Variables.worldy])
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

    i = 0
    while i <= (Variables.worldx / Variables.tx) + Variables.tx:
        Variables.gloc.append(i * Variables.tx)
        i = i + 1

    plat_list = Classes.Level.platform(1, 1, Variables.tx, Variables.ty)
    ground_list = Classes.Level.ground(1, 1, Variables.gloc, Variables.tx, Variables.ty)

# put run-once code here
