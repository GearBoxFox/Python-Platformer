import os

import pygame

import Variables


class Character(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self, img, ground_list, platform_list, hit_list, loot_list):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.moveX = 0  # move along X
        self.moveY = 0  # move along Y
        self.frame = 0  # count frames
        self.health = 10  # keep track of hp
        self.images = []
        self.img = img
        self.ground_list = ground_list
        self.plat_list = platform_list
        self.hit_list = hit_list
        self.loot_list = loot_list

        # Jumping code below
        self.is_jumping = True
        self.is_falling = True

        img = pygame.image.load(os.path.join('images', self.img + '.png')).convert()
        img.convert_alpha()
        img.set_colorkey(Variables.ALPHA)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player
        """

        self.moveX += x
        self.moveY += y

    def gravity(self):
        """
        makes the player fall down
        """

        if self.is_jumping:
            self.moveY += 3.2

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def registerJump(self):
        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.moveY -= 33

    def voidFall(self):
        if self.rect.y >= Variables.worldy:
            self.health -= 1
            print(self.health)
            self.rect.x = Variables.tx
            self.rect.y = Variables.ty

    def registerPlatform(self):
        plat_hit_list = pygame.sprite.spritecollide(self, self.plat_list, False)

        for p in plat_hit_list:
            self.is_jumping = False
            self.moveY = 0

            # Approach from bottom
            if self.rect.bottom <= p.rect.bottom:
                self.rect.bottom = p.rect.top
            else:
                self.rect.y += 6.4
                self.is_jumping = True
                self.is_falling = True

    def registerGround(self):
        ground_hit_list = pygame.sprite.spritecollide(self, self.ground_list, False)

        for g in ground_hit_list:
            self.moveY = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # Stop jumping

    def movement(self):
        # This chunk of code controls the walk animations for most objects

        # Moving left
        if self.moveX < 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * Variables.ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // Variables.ani], True, False)

        # Moving right
        if self.moveX > 0:
            self.is_jumping = True
            self.frame += 1
            if self.frame > 3 * Variables.ani:
                self.frame = 0
            self.image = self.images[self.frame // Variables.ani]

    def hitCharacter(self):
        return

    def update(self):
        """
        Update sprite position
        """

        # Movement animation
        self.movement()

        # Ground collision for gravity
        self.registerGround()

        # Platform collision
        self.registerPlatform()

        # Falling off the world
        self.voidFall()

        # Register and collisions
        self.hitCharacter()

        # Jumping code
        self.registerJump()

        # Update player code
        self.rect.x += self.moveX

        self.rect.y += self.moveY
