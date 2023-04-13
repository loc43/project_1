import pygame


WIDTH = 1000
HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
PURPLE = (255, 0, 255)

FPS = 60

running = True

cactus_que = []
cloud_que = []
ptero_que = []
bonus_que = []

game_over = False

total_score = 0
bonus_timer = 0
max_score = 0

all_sprites = pygame.sprite.Group()

