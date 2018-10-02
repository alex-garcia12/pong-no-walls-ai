import pygame
from paddle1 import Paddle1
from paddle2 import Paddle2
from settings import Settings
from startup import Startup
from scoreboard import Scoreboard
from game_stats import GameStats
from pygame.sprite import Group
import game_functions as gf



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong")
    play_button = Startup(ai_settings, screen, "Play")

    balls = Group()
    paddle1 = Paddle1(ai_settings, screen)
    paddle2 = Paddle2(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_ball(ai_settings, screen, balls)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, paddle1, paddle2, balls)
        if stats.game_active:
            paddle1.update()
            paddle2.update()
            gf.update_balls(ai_settings, stats, screen, sb, paddle1, paddle2, balls)
        gf.update_screen(ai_settings, screen, stats, sb, paddle1, paddle2, balls, play_button)  #need sb?

run_game()