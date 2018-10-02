import pygame

from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        #start each new ball in the center of the screen
        self.rect.x = ai_settings.screen_width / 2
        self.rect.y = ai_settings.screen_height / 2

        #store the ball's exact location
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edges_x(self, paddle1, paddle2):
        #return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect == paddle1.rect.y:
            return True
        elif self.rect == paddle2.rect.y:
            return True
        if self.rect.right > screen_rect.right:
            return False
        elif self.rect.left < 0:
            return False


    def check_edges_y(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def check_point_1(self):
        screen_rect = self.screen.get_rect()
        if self.rect.left < 0:
            return True


    def check_point_2(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True


    def revert_false(self):
        return False


    def update(self):
        #move the ball right
        self.x += (self.ai_settings.ball_speed * self.ai_settings.ball_direction_x)
        self.y -= (self.ai_settings.ball_speed * self.ai_settings.ball_direction_y)

        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)