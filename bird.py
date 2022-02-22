import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Bird, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('data/dragon_2.png')
        self.images = ['data/dragon_2.png', 'data/dragon_3.png', 'data/dragon_4.png']
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.f = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 3
        self.rect.y = self.y
        if self.f == 0:
            self.image = pygame.image.load(self.images[0])
            self.f += 1
        elif self.f == 1:
            self.image = pygame.image.load(self.images[0])
            self.f += 1
        elif self.f == 2:
            self.image = pygame.image.load(self.images[0])
            self.f += 1
        elif self.f == 3:
            self.image = pygame.image.load(self.images[1])
            self.f += 1
        elif self.f == 4:
            self.image = pygame.image.load(self.images[1])
            self.f += 1
        elif self.f == 5:
            self.image = pygame.image.load(self.images[1])
            self.f += 1
        elif self.f == 6:
            self.image = pygame.image.load(self.images[2])
            self.f += 1
        elif self.f == 7:
            self.image = pygame.image.load(self.images[2])
            self.f += 1
        elif self.f == 8:
            self.image = pygame.image.load(self.images[2])
            self.f += 1
        elif self.f == 9:
            self.image = pygame.image.load(self.images[1])
            self.f += 1
        elif self.f == 10:
            self.image = pygame.image.load(self.images[1])
            self.f += 1
        elif self.f == 11:
            self.image = pygame.image.load(self.images[1])
            self.f = 0
