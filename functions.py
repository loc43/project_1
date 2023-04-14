from classes import dino
from draw_screen import screen
import globals
import pygame
import pygame.font




def draw_score(counter):
    f1 = pygame.font.SysFont('playbill', 48)
    text1 = f1.render("Total score:" + str(counter), True, globals.BLACK)
    screen.blit(text1, (10, 50))


def draw_max(counter):
    f1 = pygame.font.SysFont('playbill', 48)
    text1 = f1.render('Best score:' + str(counter), True, globals.BLACK)
    screen.blit(text1, (10, 100))

def draw_bonus():
    f1 = pygame.font.SysFont('playbill', 48)
    text1 = f1.render('Congratulations! Your bonus: ' + 'The Hat of Immortality', True, globals.BLACK)
    screen.blit(text1, (globals.WIDTH / 3, 50))
    f2 = pygame.font.SysFont('playbill', 48)
    text2 = f2.render('Your ability: temporal immortality', True, globals.BLACK)
    screen.blit(text2, (globals.WIDTH / 3, 100))

def lose_check():
    for elem in globals.cactus_que:
        if pygame.sprite.collide_rect_ratio(0.8)(dino, elem):
            return True
    for elem in globals.ptero_que:
        if pygame.sprite.collide_rect (dino, elem):
            return True
    return False

def bonus_check():
    for elem in globals.bonus_que:
        if pygame.sprite.collide_rect(dino, elem):
            elem.kill()
            return True
    return False

