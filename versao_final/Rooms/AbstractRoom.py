from abc import ABC, abstractmethod

class AbstractRoom(ABC):
    def __init__(self):
        self.visited = False
    
    @abstractmethod
    def draw_background(self, screen):
        pass

    @abstractmethod
    def draw_art(self, screen):
        pass
    
    @abstractmethod
    def load(self, entry_point):
        pass

    @abstractmethod
    def unload(self):
        pass

    @abstractmethod
    def start_walls(self):
        pass
