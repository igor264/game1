import time
from scores import Scores
import pygame
import sys
from bird import Bird
import random


run_flag = True


def events(player):
    #отслеж нажатий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #выход
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                #right
                player.move_d = True
            elif event.key == pygame.K_a:
                #left
                player.move_a = True
            elif event.key == pygame.K_w:
                #up
                player.move_w = True
            elif event.key == pygame.K_s:
                #down
                player.move_s = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                #right
                player.move_d = False
                player.image = pygame.image.load('data/plane_f.png')
            elif event.key == pygame.K_a:
                #left
                player.move_a = False
                player.image = pygame.image.load('data/plane_f.png')
            elif event.key == pygame.K_w:
                #up
                player.move_w = False
                player.image = pygame.image.load('data/plane_f.png')
            elif event.key == pygame.K_s:
                #down
                player.move_s = False
                player.image = pygame.image.load('data/plane_f.png')


def update(sc_collor, screen, stats, sc, player, birds):
    screen.fill(sc_collor)
    sc.show_score()
    check_highscore(stats, sc)
    player.output()
    birds.draw(screen)
    pygame.display.flip()


def plane_kill(stats, screen, player, birds):
    global run_flag
    stats.life -= 1
    birds.empty()
    player.plane()
    create_army(screen, birds)
    if stats.life == 0:
        run_flag = False
    time.sleep(2)


def create_army(screen, birds):
    bird = Bird(screen)
    bird_width = bird.rect.width
    number_bird_y = 5
    bird_height = bird.rect.height

    for y_number in range(number_bird_y):
        for bird_number in range(2):
            bird = Bird(screen)
            bird.y = (bird_height + 2.5 * bird_height * y_number) * -1
            bird.x = bird_width * random.randint(0, 2)
            bird.rect.x = bird.x
            bird.rect.y = (bird.rect.height + 2.5 * bird.rect.height * y_number) * -1

            birds.add(bird)


def update_birds(stats, screen, player, birds):
    birds.update()
    screen_rect = screen.get_rect()
    for j in birds.copy():
        if j.rect.top > screen_rect.bottom:
            birds.remove(j)
    if len(birds) <= 4:
        create_army(screen, birds)
    if pygame.sprite.spritecollideany(player, birds):
        plane_kill(stats, screen, player, birds)


def check_highscore(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_highscore()
        with open ('data/highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
