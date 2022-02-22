import pygame, control
import sys
import start
from plane import Player
from pygame.sprite import Group
import os
from stats import Stats
from scores import Scores


start_screen = True
pygame.init()
FPS = 24
size = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('MENU')
music, sound_effects = 0, 0
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load('data/music.mp3')
pygame.mixer.music.play(-1)
pygame.display.flip()



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def mouse(pos):
    image = load_image("mouse.png")
    screen.blit(image, pos)


def start_screen():
    global sound_effects
    global music
    start.get_screen(screen)
    s = start.StartScreenButtons()
    x, y = (-70, -70)
    mouse_cursor = False
    while s.start_flag:
        music, sound_effects = start.take_sound()
        pygame.mixer.music.set_volume(music)
        s.screens(s.screen_number)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s.action(event.pos)
            if pygame.mouse.get_focused() and event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if pygame.mouse.get_focused():
                mouse_cursor = True
            else:
                mouse_cursor = False
        if mouse_cursor:
            mouse((x, y))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.mixer.music.stop()


pygame.mouse.set_visible(False)
start_screen()
pygame.mouse.set_visible(True)


def Run():
    pygame.init()
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((450, 600))
    pygame.display.set_caption('MY GAME')
    sc_collor = 117, 187, 253
    player = Player(screen)
    birds = Group()
    stats = Stats()
    sc = Scores(screen, stats)
    FPS = 10
    clock = pygame.time.Clock()
    control.create_army(screen, birds)

    while control.run_flag:
        control.events(player)
        player.update_player()
        control.update(sc_collor, screen, stats, sc, player, birds)
        control.update_birds(stats, screen, player, birds)
        stats.score += 1
        sc.image_score()
        sc.image_highscore()
        sc.show_score()
        clock.tick(FPS)


Run()


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('GAME_OVER')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    image1 = pygame.image.load('data/gameover3.jpg')
    screen.blit(image1, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
