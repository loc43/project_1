import os
import pygame


pygame.display.init()
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("NOTHING TO WRITE HOME ABOUT: THE GAME")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'dino')

dino_1 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'dino_1.png')).convert_alpha(), (100, 100))
dino_2 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'dino_2.png')).convert_alpha(), (100, 100))
dino_hat_1 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'dino_hat_1.png')).convert_alpha(), (100, 120))
dino_hat_2 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'dino_hat_2.png')).convert_alpha(), (100, 120))
duck_1 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'duck_1.png')).convert_alpha(), (120, 60))
duck_2 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'duck_2.png')).convert_alpha(), (120, 60))
dino_arr = [dino_1, dino_1, dino_1, dino_1, dino_2, dino_2, dino_2, dino_2]
duck_arr = [duck_1, duck_1, duck_1, duck_1, duck_2, duck_2, duck_2, duck_2]
hat_arr = [dino_hat_1, dino_hat_1, dino_hat_1, dino_hat_1, dino_hat_2, dino_hat_2, dino_hat_2, dino_hat_2]

ptero_1 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'ptero_1.png')).convert_alpha(), (120, 60))
ptero_2 = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'ptero_2.png')).convert_alpha(), (120, 60))


hat = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'hat.png')).convert_alpha(), (60, 40))


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'cactus_place')


cloud_img = pygame.transform.scale(pygame.image.load(os.path.join(img_folder, 'cloud.png')).convert_alpha(), (100, 50))

cactus_img = pygame.image.load(os.path.join(img_folder, '1_cactus.png')).convert_alpha()
cactus2_img = pygame.image.load(os.path.join(img_folder, '2_cactuses.png')).convert_alpha()
cactus3_img = pygame.image.load(os.path.join(img_folder, '3_cactuses.png')).convert_alpha()
cactus4_img = pygame.image.load(os.path.join(img_folder, '4_cactuses.png')).convert_alpha()

