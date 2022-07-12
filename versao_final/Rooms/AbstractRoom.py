from abc import ABC, abstractmethod

class AbstractRoom(ABC):
    def __init__(self):
        self.visited = False
        self.entities = {'enemies': [], 'objects': [], 'walls': []}
    
    @abstractmethod
    def draw_background(self, screen):
        pass

    @abstractmethod
    def draw_art(self, screen):
        pass
    
    @abstractmethod
    def load(self, entry_point):
        pass

    def unload(self):
        self.entities['enemies'].clear()
        self.entities['objects'].clear()
        self.entities['walls'].clear()

    @abstractmethod
    def start_walls(self):
        pass
