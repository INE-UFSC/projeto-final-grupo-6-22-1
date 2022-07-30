from Score.ScoreDAO import ScoreDAO

class ScoreController():
    def __init__(self):
        self.__scoreDAO = ScoreDAO('score.pkl')
        if self.__scoreDAO.get_all():
            self.__counter = max(self.__scoreDAO.get_all().keys()) + 1
        else:
            self.__counter = 0

    def add_score(self, score):
        self.__scoreDAO.add(self.__counter, score)
        self.__counter += 1

    def get_last_score(self):
        return self.__scoreDAO.get(self.__counter - 1)

    def get_all(self):
        return self.__scoreDAO.get_all()
    
