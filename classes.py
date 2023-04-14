from draw_screen import hat_arr, dino_arr, duck_arr, dino_1, dino_hat_1, duck_1, ptero_1, ptero_2, hat, cactus_img, cactus2_img, cactus3_img, cactus4_img, cloud_img
from globals import WIDTH, HEIGHT
import pygame
import random


#создаем динозавра

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = dino_1
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH / 15, HEIGHT / 1.5)
        self.ducking = False
        self.jumping = False 
        self.hat = False
        self.idx = 0
        self.duck_idx = 0
        self.hat_idx = 0
        self.height = 100

    def wear_hat(self):
        self.hat = True
        self.image = dino_hat_1
        tmp = self.rect.bottomleft
        self.rect = self.image.get_rect()
        self.rect.bottomleft = tmp
        self.height = 120

    def lose_hat(self):
        self.hat = False
        self.image = dino_1
        tmp = self.rect.bottomleft
        self.rect = self.image.get_rect()
        self.rect.bottomleft = tmp
        self.height = 100

    def move(self):
        if not self.ducking and not self.hat:
            self.image = dino_arr[self.idx % 8]
            self.idx += 1    
        elif self.ducking:
            self.image = duck_arr[self.duck_idx % 8]
            self.duck_idx += 1    
        elif not self.ducking and self.hat:
            self.image = hat_arr[self.hat_idx % 8]
            self.hat_idx += 1  

    def duck(self):
        self.image = duck_1
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH / 15, HEIGHT / 1.5)
        self.ducking = True
        self.height = 60

    def straighten(self):
        if self.hat:
            self.image = dino_hat_1
            self.height = 120
        else:
            self.image = dino_1
            self.height = 100
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH / 15, HEIGHT / 1.5)
        self.ducking = False


class Ptero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ptero_1
        self.rect = self.image.get_rect()
        rand = random.choice([40, 80])
        self.rect.bottomleft = (WIDTH, HEIGHT / 1.5 - rand)
    def move(self):
        if self.image == ptero_1:
            self.image = ptero_2
        elif self.image == ptero_2:
            self.image = ptero_1



class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = hat
        self.rect = self.image.get_rect()
        rand = random.choice([40, 150])
        self.rect.bottomleft = (WIDTH, HEIGHT / 1.5 - rand)


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.height = random.randint(75, 120)
        self.width = self.height * 2 / 3
        self.image = random.choice([cactus3_img, cactus_img, cactus2_img, cactus4_img])

        if self.image == cactus3_img:
            self.width *= 1.6
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        elif self.image == cactus2_img:
            self.width *= 1.3
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            
        elif self.image == cactus_img:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        if self.image == cactus4_img:
            self.width *= 2
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH, HEIGHT / 1.5)


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cloud_img
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH, random.randint(100, 200))


dino = Player()
cactus = Cactus()
