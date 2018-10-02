import sys
import pygame
from ball import Ball
from time import sleep

def check_events(ai_settings, screen, stats, play_button, paddle1, paddle2, balls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, paddle1, paddle2, balls, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle1, paddle2)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle1, paddle2)


def check_play_button(ai_settings, screen, stats, play_button, paddle1, paddle2, balls, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        pygame.mouse.set_visible(False)
        balls.empty()
        create_ball(ai_settings, screen, balls)


def check_keydown_events(event, paddle1, paddle2):
    #player 1
    if event.key == pygame.K_DOWN:
        paddle1.moving_down = True
    elif event.key == pygame.K_s:
        paddle2.moving_down = True

    #player 2
    elif event.key == pygame.K_UP:
        paddle1.moving_up = True
    elif event.key == pygame.K_w:
        paddle2.moving_up = True


def check_keyup_events(event, paddle1, paddle2):
    #player 1
    if event.key == pygame.K_UP:
        paddle1.moving_up = False
    elif event.key == pygame.K_w:
        paddle2.moving_up = False

    #player 2
    elif event.key == pygame.K_DOWN:
        paddle1.moving_down = False
    elif event.key == pygame.K_s:
        paddle2.moving_down = False


def start_ball_movement(event, ball):
    if event.key == pygame.K_SPACE:
        ball.moving_x = True
        ball.moving_y = True


def create_ball(ai_settings, screen, balls):
    sleep(1)
    balls.empty()
    ball = Ball(ai_settings, screen)
    balls.add(ball)


def check_ball_edges(ai_settings, screen, stats, sb, balls, paddle1, paddle2):
    # respond appropriately if a ball has reached an edge
    for ball in balls.sprites():
        if ball.check_edges_x(paddle1, paddle2):
            change_ball_direction_x(ai_settings, balls)
        elif ball.check_edges_y():
            change_ball_direction_y(ai_settings, balls)
        elif ball.check_point_1():
            ball_score_1(ai_settings, stats, sb, screen, paddle1, paddle2, balls)
        elif ball.check_point_2():
            ball_score_2(ai_settings, stats, sb, screen, paddle1, paddle2, balls)
            break


def change_ball_direction_x(ai_settings, balls):
    ai_settings.ball_direction_x *= -1


def change_ball_direction_y(ai_settings, balls):
    ai_settings.ball_direction_y *= -1


def ball_score_1(ai_settings, stats, sb, screen, paddle1, paddle2, balls):
    balls.empty()
    stats.score1 += ai_settings.ball_point
    sb.prep_score()
    if stats.score1 >= 10:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    create_ball(ai_settings, screen, balls)     #add paddle1 and paddle2?


def ball_score_2(ai_settings, stats, sb, screen, paddle1, paddle2, balls):
    balls.empty()
    stats.score2 += ai_settings.ball_point
    sb.prep_score()
    if stats.score2 >= 10:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    create_ball(ai_settings, screen, balls)     #add paddle1 and paddle2?



def update_balls(ai_settings, stats, screen, sb, paddle1, paddle2, balls):
    #check if the ball is at an edge and update its position
    check_ball_edges(ai_settings, screen, stats, sb, balls, paddle1, paddle2)
    balls.update()

    #look for paddle-ball collisions
    if pygame.sprite.spritecollideany(paddle1, balls):
        change_ball_direction_x(ai_settings, balls)
    if pygame.sprite.spritecollideany(paddle2, balls):
        change_ball_direction_x(ai_settings, balls)



def update_screen(ai_settings, screen, stats, sb, paddle1, paddle2, balls, play_button):
    screen.fill(ai_settings.bg_color)
    paddle1.blitme()
    paddle2.blitme()
    balls.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()