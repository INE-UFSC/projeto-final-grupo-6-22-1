from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Enemy import Enemy

class Room1(AbstractRoom):
    def __init__(self):
        super().__init__()

    def draw_background(self, screen):
        screen.fill((255, 255, 255))

    def draw_art(self, screen):
        pass
    
    def load(self, entry_point):
        self.entities['enemies'].append(Enemy((500, 500)))
        return self.entities

    def start_walls(self):
        pass

