import pygame as pg
from States.State import State



class Menu(State):
    def __init__(self, menu_font):
        State.__init__(self)

        self.rect_jogar = pg.Rect(180, 430, 300, 125)
        self.text_jogar = menu_font.render('Jogar', True, (0, 0, 0))
        self.rect_sair = pg.Rect(180, 550, 300, 125)
        self.text_sair = menu_font.render('Sair', True, (0, 0, 0))

    # def cleanup(self):

    # def startup(self):

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

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((119, 221, 119))

        screen.blit(self.text_jogar, dest=(200, 450))
    
        screen.blit(self.text_sair, dest=(200, 570))
