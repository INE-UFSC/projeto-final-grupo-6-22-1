from abc import ABC, abstractmethod

class AbstractState(ABC):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None
    
    @abstractmethod
    def handle_events(self, events):
        pass
    
    @abstractmethod
    def handle_collisions(self):
        pass
    
    @abstractmethod
    def handle_keys(self, keys):
        pass
    
    @abstractmethod
    def update(self, screen):
        pass
