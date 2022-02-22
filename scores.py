import pygame.font
from stats import Stats



class Scores:
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stat = Stats()
        self.stats = stats
        self.text_cl = 0, 0, 0
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_highscore()
        self.image_life()

    def image_score(self):
        self.score_im = self.font.render(str(self.stats.score), True, self.text_cl, (117, 187, 253))
        self.score_rect = self.score_im.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20
        self.score_im = self.font.render(str(self.stats.score), True, self.text_cl, (117, 187, 253))
        self.score_rect = self.score_im.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_highscore(self):
        self.highscore_im = self.font.render(str(self.stats.high_score), True, self.text_cl, (117, 187, 253))
        self.highscore_rect = self.score_im.get_rect()
        self.highscore_rect.right = self.screen_rect.right - 40
        self.highscore_rect.top = 20
        self.highscore_im = self.font.render(str(self.stats.high_score), True, self.text_cl, (117, 187, 253))
        self.highscore_rect = self.score_im.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = 20

    def image_life(self):
        self.scorelife_im = self.font.render(str(self.stats.life), True, self.text_cl, (117, 187, 253))
        self.scorelife_rect = self.score_im.get_rect()
        self.scorelife_rect.left = self.screen_rect.left + 40
        self.scorelife_rect.top = 20
        self.scorelife_im = self.font.render(str(self.stats.life), True, self.text_cl, (117, 187, 253))
        self.scorelife_rect = self.score_im.get_rect()
        self.scorelife_rect.left = self.screen_rect.left + 40
        self.scorelife_rect.top = 20

    def show_score(self):
        self.image_life()
        self.screen.blit(self.highscore_im, self.highscore_rect)
        self.screen.blit(self.score_im, self.score_rect)
        self.screen.blit(self.scorelife_im, self.scorelife_rect)


