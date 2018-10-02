import pygame.ftfont

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score_str1 = str(self.stats.score1)
        score_str2 = str(self.stats.score2)
        self.score_image1 = self.font.render(score_str1, True, self.text_color, self.ai_settings.bg_color)
        self.score_image2 = self.font.render(score_str2, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect1 = self.score_image1.get_rect()
        self.score_rect2 = self.score_image2.get_rect()
        self.score_rect1.right = (self.ai_settings.screen_width / 2) + 30
        self.score_rect2.right = (self.ai_settings.screen_width / 2) - 30
        self.score_rect1.top = 20
        self.score_rect2.top = 20

    def show_score(self):
        self.screen.blit(self.score_image1, self.score_rect1)
        self.screen.blit(self.score_image2, self.score_rect2)
