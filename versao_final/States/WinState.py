import pygame as pg
from Score.ScoreController import ScoreController
from Score.ScoreDAO import ScoreDAO
from States.AbstractState import AbstractState
from get_image import get_image


class WinState(AbstractState):
    def __init__(self, menu_font, score_controller):
        AbstractState.__init__(self)
        self.score_controller = score_controller
        self.ScoreController = ScoreController()

        self.background = get_image('telas', 'TelaVitoria.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))       
        self.score = menu_font.render("0", True, (77, 0, 18))
        self.rect_menu = pg.Rect(60, 560, 500, 125)
        #self.text_menu = menu_font.render('Retornar ao menu', True, (0, 0, 0))


    def startup(self):
        self.score = pg.font.Font(pg.font.get_default_font(), 40).render(str(self.score_controller.get_last_score()), True, (77, 0, 18))

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
        #screen.fill((00, 255, 00))
        screen.blit(self.background, dest=(0,0))
        #pg.draw.rect(screen, (255, 255, 255), self.rect_menu)
    
        #screen.blit(self.text_menu, dest=(550, 370))

        screen.blit(self.score, dest=(570, 335))
