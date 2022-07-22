import pygame as pg
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Zombie import Zombie
from Sprites.Objects.Wardrobe import Wardrobe
from Sprites.Objects.Door import Door
from Sprites.Objects.Piano import Piano

class Room1(AbstractRoom):
    def __init__(self):
        super().__init__()
        self.rect_mudarSala = pg.Rect(60, 100, 300, 287) #apagar isso também
        self.background = get_image('Telas', 'Tela.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))
        
    def draw_background(self, screen):
        #screen.fill((255, 255, 255))
        
        screen.blit(self.background, dest=(0, 0))

    def draw_art(self, screen):
        pass
    
    def load(self, entry_point):
        self.entities['enemies'].append(Zombie((700, 500)))
        self.entities['objects'].append(Wardrobe((800, 310)))
        self.entities['objects'].append(Piano((520, 329)))
        self.entities['objects'].append(Door((300, 287), 1))
        return self.entities

    def start_walls(self):
        pass


        #tentativa de fazer uma maneira de mudar de tela

    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.rect_mudarSala.collidepoint(mouse_pos):
                self.next = 'room2'
                self.done = True



    def draw(self, screen):
        self.draw_background(screen)
        pg.draw.rect(screen, (255, 255, 255), self.rect_mudarSala)

