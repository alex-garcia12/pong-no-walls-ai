class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

        self.ten = 10

    def reset_stats(self):
        self.score1 = 0
        self.score2 = 0

