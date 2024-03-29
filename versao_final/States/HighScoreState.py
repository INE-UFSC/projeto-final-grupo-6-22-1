import pygame as pg
from States.AbstractState import AbstractState
from get_image import get_image


class HighScoreState(AbstractState):
    def __init__(self, menu_font, score_controller):
        AbstractState.__init__(self)
        self.__score_controller = score_controller

        self.__background = get_image('telas', 'TelaHighScore.png')
        self.__background = pg.transform.smoothscale(self.__background, (1280, 700))       
        self.__rect_menu = pg.Rect(60, 560, 500, 125)
        #self.text_menu = menu_font.render('Retornar ao menu', True, (0, 0, 0))


    def startup(self):
        self.__scores = list(self.__score_controller.get_all().values())
        print(self.__scores)
        self.__top_five = []
        self.__scores.sort()
        for i in range(5):
            self.__top_five.append(pg.font.Font(pg.font.get_default_font(), 40).render(str(self.__scores[i]), True, (77, 0, 18)))

    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.__rect_menu.collidepoint(mouse_pos):
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
        screen.blit(self.__background, dest=(0,0))
        #pg.draw.rect(screen, (255, 255, 255), self.__rect_menu)
    
        #screen.blit(self.text_menu, dest=(550, 370))

        for i in range(5):
            screen.blit(self.__top_five[i], dest=(570, 335 + 40*i))
