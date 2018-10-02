import pygame

class Paddle2():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start paddles in appropriate places
        self.rect.centerx = self.screen_rect.right - 55
        self.rect.centery = self.ai_settings.screen_height / 2
        self.center = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

        #player 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.paddle_speed

        self.rect.centery = self.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)



