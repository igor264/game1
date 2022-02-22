class Stats():
    def __init__(self):
        self.reset_stats()
        with open('data/highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        self.life = 3
        self.score = 0