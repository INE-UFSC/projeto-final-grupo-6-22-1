from Score.ScoreDAO import ScoreDAO

class ScoreController():
    def __init__(self):
        self.scoreDAO = ScoreDAO('score.pkl')
        if self.scoreDAO.get_all():
            self.counter = max(self.scoreDAO.get_all().keys()) + 1
        else:
            self.counter = 0

    def add_score(self, score):
        self.scoreDAO.add(self.counter, score)
        self.counter += 1

    def get_last_score(self):
        return self.scoreDAO.get(self.counter - 1)

    def get_all(self):
        return self.scoreDAO.get_all()
    
