import pygame


music, sound_effects = 1, 1
screen = 0


def get_screen(s):
    global screen
    screen = s


def take_sound():
    return music, sound_effects


class StartScreenButtons:
    def __init__(self):
        self.options = [100, 345, 199, 241]
        self.start = [100, 355, 99, 141]
        self.credits = [100, 430, 299, 341]
        self.back_button = [49, 171, 499, 541]
        self.music_button_m = [100, 150, 113, 137]
        self.music_button_p = [440, 485, 113, 137]
        self.sound_button_m = [100, 150, 173, 197]
        self.sound_button_p = [580, 650, 173, 197]
        self.screen_number = 0
        self.start_flag = True

    def screens(self, screen_number=0):
        if screen_number == 0:
            image = pygame.image.load('data/321.png')
            screen.blit(image, (0, 0))
            f1 = pygame.font.Font(None, 75)
            text1 = f1.render('START', True,
                              (0, 0, 0))
            text2 = f1.render('OPTIONS', True,
                              (0, 0, 0))
            text3 = f1.render('CREDITS', True,
                              (0, 0, 0))
            screen.blit(text1, (100, 100))
            screen.blit(text2, (100, 200))
            screen.blit(text3, (100, 300))

        elif screen_number == 1:
            image = pygame.image.load('data/321.png')
            screen.blit(image, (0, 0))
            sound = pygame.font.Font(None, 75)
            button = pygame.font.Font(None, 75)
            back_button1 = button.render('Back', True,
                              (0, 0, 0))
            screen.blit(back_button1, (50, 500))
            music_button = sound.render(f'< Music:{int(music * 100)}%', True,
                                        (0, 0, 0))
            music_button1 = sound.render(f'>', True,
                                         (0, 0, 0))
            sound_button = sound.render(f'< Music effects:{int(sound_effects * 100)}% >', True,
                                        (0, 0, 0))
            screen.blit(music_button, (100, 95))
            screen.blit(music_button1, (450, 95))
            screen.blit(sound_button, (100, 160))

        elif screen_number == 2:
            image = pygame.image.load('data/321.png')
            screen.blit(image, (0, 0))
            intro_text = ["Разработчики:",
                          "  Shaev Igor",
                          "Художники:",
                          "  Shaev Igor"]
            font = pygame.font.Font(None, 30)
            text_coord = 50
            for line in intro_text:
                string_rendered = font.render(line, 1, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)

    def action(self, mouse_pos):
        global music
        global sound_effects
        if self.screen_number == 0:
            if self.options[0] < mouse_pos[0] < self.options[1] and \
                    self.options[2] < mouse_pos[1] < self.options[3]:
                self.screen_number = 1
            elif self.start[0] < mouse_pos[0] < self.start[1] and \
                    self.start[2] < mouse_pos[1] < self.start[3]:
                self.start_flag = False
            elif self.credits[0] < mouse_pos[0] < self.credits[1] and \
                    self.credits[2] < mouse_pos[1] < self.credits[3]:
                self.screen_number = 2
        elif self.screen_number == 1:
            if self.back_button[0] < mouse_pos[0] < self.back_button[1] and \
                    self.back_button[2] < mouse_pos[1] < self.back_button[3]:
                self.screen_number = 0
            elif self.music_button_m[0] < mouse_pos[0] < self.music_button_m[1] and \
                    self.music_button_m[2] < mouse_pos[1] < self.music_button_m[3]:
                if music > 0:
                    music = (int(music * 100) - 5) / 100
            elif self.music_button_p[0] < mouse_pos[0] < self.music_button_p[1] and \
                    self.music_button_p[2] < mouse_pos[1] < self.music_button_p[3]:
                if music < 1:
                    music = (int(music * 100) + 5) / 100
            elif self.sound_button_m[0] < mouse_pos[0] < self.sound_button_m[1] and \
                    self.sound_button_m[2] < mouse_pos[1] < self.sound_button_m[3]:
                if sound_effects > 0:
                    sound_effects = (int(sound_effects * 100) - 5) / 100
            elif self.sound_button_p[0] < mouse_pos[0] < self.sound_button_p[1] and \
                    self.sound_button_p[2] < mouse_pos[1] < self.sound_button_p[3]:
                if sound_effects < 1:
                    sound_effects = (int(sound_effects * 100) + 5) / 100
        elif self.screen_number == 2:
            self.screen_number = 0