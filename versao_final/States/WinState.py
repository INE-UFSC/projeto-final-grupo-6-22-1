import pygame as pg
from States.AbstractState import AbstractState


class WinState(AbstractState):
    def __init__(self, menu_font):
        AbstractState.__init__(self)

        self.text_win = menu_font.render('VITÓRIA', True, (0, 0, 0))
        self.rect_menu = pg.Rect(550, 370, 300, 125)
        self.text_menu = menu_font.render('Retornar ao menu', True, (0, 0, 0))


    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.rect_menu.collidepoint(mouse_pos):
                self.next = 'menu'
                self.done = True

    def handle_collisions(self):
        pass

    def handle_keys(self, keys):
        pass                

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((00, 255, 00))
    
        screen.blit(self.text_menu, dest=(550, 370))

        screen.blit(self.text_win, dest=(500, 125))