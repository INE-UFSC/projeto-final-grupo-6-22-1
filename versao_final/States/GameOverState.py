import pygame as pg
from States.AbstractState import AbstractState



class GameOverState(AbstractState):
    def __init__(self, menu_font):
        super().__init__()

        self.rect_tentatNovamente = pg.Rect(450, 320, 300, 25)
        self.text_tentarNovamente = menu_font.render('Tentar Novamente', True, (0, 0, 0)) 
        self.rect_menu = pg.Rect(550, 370, 300, 125)
        self.text_menu = menu_font.render('Menu', True, (0, 0, 0))
        self.text_gameOver = menu_font.render('GAME OVER', True, (0, 0, 0))


    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.rect_tentatNovamente.collidepoint(mouse_pos):
                self.next = 'game'
                self.done = True
            elif self.rect_menu.collidepoint(mouse_pos):
                self.next = 'menu'
                self.done = True

    def handle_collisions(self):
        pass

    def handle_keys(self, keys):
        pass

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        screen.fill((88, 79, 77))

        screen.blit(self.text_tentarNovamente, dest=(450, 320))
    
        screen.blit(self.text_menu, dest=(550, 370))

        screen.blit(self.text_gameOver, dest=(500, 125))