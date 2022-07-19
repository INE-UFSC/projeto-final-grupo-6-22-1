import pygame as pg
from States.AbstractState import AbstractState
from get_image import get_image



class GameOverState(AbstractState):
    def __init__(self, menu_font):
        super().__init__()
        self.background = get_image('Telas', 'TelaGameOver.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))
        self.rect_tentatNovamente = pg.Rect(310, 320, 648, 80)
        #self.text_tentarNovamente = menu_font.render('Tentar Novamente', True, (0, 0, 0)) 
        self.rect_menu = pg.Rect(490, 423, 230, 80)
        #self.text_menu = menu_font.render('Menu', True, (0, 0, 0))
        #self.text_gameOver = menu_font.render('GAME OVER', True, (0, 0, 0))


    def startup(self):
        pass

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
        screen.blit(self.background, dest=(0, 0))
        #screen.fill((88, 79, 77))

        #pg.draw.rect(screen, (255, 255, 255), self.rect_tentatNovamente)
    
        #screen.blit(self.text_menu, dest=(550, 370))

        #screen.blit(self.text_gameOver, dest=(500, 125))
