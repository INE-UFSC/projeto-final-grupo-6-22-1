from Score.DAO import DAO

class ScoreDAO(DAO):
    def __init__(self, data_source):
        super().__init__(data_source)
    
    def add(self, chave, score):
        if isinstance(score, int):
            if score > 0:
                super().add(chave, score)
    
    def get(self, chave):
        return super().get(chave)
    
    def remove(self, chave):
        super().remove(chave)
