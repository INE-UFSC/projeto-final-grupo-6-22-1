import pygame as pg
from States.AbstractState import AbstractState
from get_image import get_image

class MenuState(AbstractState):
    def __init__(self, menu_font):
        super().__init__()

        self.background = get_image('Telas', 'TelaMenu.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))
        self.rect_jogar = pg.Rect(80, 475, 250, 60)
       # self.text_jogar = menu_font.render('Jogar', True, (0, 0, 0))
        self.rect_sair = pg.Rect(80, 635, 190, 60)
       # self.text_sair = menu_font.render('Sair', True, (0, 0, 0))


    def startup(self):
        pass

    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.rect_jogar.collidepoint(mouse_pos):
                self.next = 'game'
                self.done = True
            elif self.rect_sair.collidepoint(mouse_pos):
                self.quit = True
    
    def handle_collisions(self):
        pass

    def handle_keys(self, keys):
        pass

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.background, dest=(0, 0))
        #pg.draw.rect(screen, (255, 255, 255), self.rect_sair)

        #screen.blit(self.text_jogar, dest=(200, 500))
    
#        screen.blit(self.text_sair, dest=(200, 570))
