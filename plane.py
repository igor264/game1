import pygame


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('data/plane_f.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.anim = 0
        self.move_d = False
        self.move_a = False
        self.move_w = False
        self.move_s = False
        self.images_f = ['data/plane_f.png']
        self.images_b = ['data/plane_f.png']
        self.images_r = ['data/plane_r.png']
        self.images_l = ['data/plane_l.png']

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        if self.move_d and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
            self.image = pygame.image.load(self.images_r[0])
        elif self.move_a and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 5
            self.image = pygame.image.load(self.images_l[0])
        elif self.move_w and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 5
            self.image = pygame.image.load(self.images_b[0])
        elif self.move_s and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 5
            self.image = pygame.image.load(self.images_f[0])

    def plane(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
