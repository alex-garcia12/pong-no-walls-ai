class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)   #black

        #paddle settings
        self.paddle_speed = 1
        self.paddle_width = 10
        self.paddle_height = 50
        self.paddle_color = 255, 255, 255   #white

        #ball settings
        self.ball_speed = 0.5
        self.ball_direction_x = 1
        self.ball_direction_y = 1

        #scoring
        self.ball_point = 1