from classes import dino
from draw_screen import screen, clock
import functions
import globals
import pygame
import sys



def normal_changes():
    for item in globals.cactus_que:
        item.rect.x -= 6
        if item.rect.x < - item.width:
            globals.cactus_que.pop(0)
    for item in globals.cloud_que:
        item.rect.x -= 2
        if item.rect.x < - 100:
            globals.cloud_que.pop(0)
    for item in globals.ptero_que:
        item.rect.x -= 6
        item.move()
        if item.rect.x < - 140:
            globals.ptero_que.pop(0)
    for item in globals.bonus_que:
        item.rect.x -= 6
        if item.rect.x < - 60:
            globals.bonus_que.pop(0)
    globals.all_sprites.update()
    screen.fill(globals.WHITE)
    globals.all_sprites.draw(screen)


def basic_frame():
    normal_changes()
    clock.tick(globals.FPS)
    globals.total_score += 1
    if globals.total_score % 500 == 0:
        globals.FPS += 10
    if globals.max_score < globals.total_score:
        globals.max_score = globals.total_score
    if functions.lose_check() and not dino.hat:
        losing_screen()
    if functions.bonus_check() and not dino.hat:
        dino.wear_hat()
        globals.bonus_timer = 1
    if dino.hat:
        globals.bonus_timer += 1
    if globals.bonus_timer > 1 and globals.bonus_timer < 4.5 * globals.FPS:
        functions.draw_bonus()
    if globals.bonus_timer > 5 * globals.FPS and dino.hat:
       globals.bonus_timer = 0
       dino.lose_hat()
    functions.draw_score(globals.total_score // 10)
    functions.draw_max(globals.max_score // 10)
    pygame.display.update()


def stable_frame():
    dino.move()
    basic_frame()


def losing_screen():
    screen.fill(globals.BLUE)
    f1 = pygame.font.SysFont('playbill', 48)
    text1 = f1.render("You Lost! Press C-Play Again or Q-Quit", True, globals.BLACK)
    screen.blit(text1, (globals.WIDTH / 4, globals.HEIGHT / 2))
    clock.tick(3)
    pygame.display.update()
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    flag = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    globals.game_over = True
                    restart()
                    flag = False
            elif event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                sys.exit()

def restart():
    screen.fill(globals.WHITE)
    globals.FPS = 60
    globals.total_score = 0
    dino.straighten()
    dino.lose_hat()
    pygame.event.clear()
    globals.cactus_que.clear()
    globals.cloud_que.clear()
    globals.ptero_que.clear()
    globals.bonus_que.clear()
    globals.all_sprites.empty()
    dino.rect.bottomleft = (globals.WIDTH / 15, globals.HEIGHT / 1.5)
    globals.all_sprites.add(dino)
    globals.all_sprites.draw(screen)
    globals.game_over = False

def one_jump():
    while (dino.rect.y > (globals.HEIGHT / 1.5 - dino.height) - 260):
        if globals.total_score == 0:
            dino.rect.bottomleft = (globals.WIDTH / 15, globals.HEIGHT / 1.5)
            return
        dino.rect.y -= 10 
        basic_frame()
    for i in range(max(20 - globals.total_score // 100, 3)): 
        if globals.total_score == 0:
            dino.rect.bottomleft = (globals.WIDTH / 15, globals.HEIGHT / 1.5)
            return
        basic_frame()
    while (dino.rect.y < globals.HEIGHT / 1.5 - dino.height):
        if globals.total_score == 0:
            dino.rect.bottomleft = (globals.WIDTH / 15, globals.HEIGHT / 1.5)
            return
        dino.rect.y += 10 
        basic_frame()


def one_move_generator():
    stable_frame()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not dino.ducking:
            dino.jumping = True
            one_jump()
            dino.jumping = False
            pygame.event.clear()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dino.duck()
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            dino.straighten()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
