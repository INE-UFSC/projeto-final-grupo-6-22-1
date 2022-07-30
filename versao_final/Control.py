import pygame as pg
import sys

from States.GameState import GameState
from States.MenuState import MenuState
from States.WinState import WinState
from States.GameOverState import GameOverState
from States.HighScoreState import HighScoreState

from Score.ScoreController import ScoreController


class Control:
    def __init__(self):
        self.__done = False
        self.__fps = 60
        self.__screen = pg.display.set_mode((1280, 720))
        self.__screen_rect = self.__screen.get_rect()
        self.__clock = pg.time.Clock()
        
        self.__score_controller = ScoreController()

    def init(self):
        pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.init()
        self.menu_font = pg.font.Font(pg.font.get_default_font(), 30)
        self.state_dict = {
        'menu': MenuState(self.menu_font),
        'game': GameState(),
        'game_over': GameOverState(self.menu_font),
        'win': WinState(self.menu_font, self.__score_controller),
        'high_score': HighScoreState(self.menu_font, self.__score_controller)
        }
        self.setup_states(self.state_dict, 'menu')
        self.main_game_loop()
        pg.quit()
        sys.exit()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        # Função que troca de estado atual para proximo estado
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        # Finalização do estado anterior
        
        score = self.state.cleanup()

        if score != -1:
            self.__score_controller.add_score(score)
    
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
        
    def update(self):
        if self.state.quit:
            self.__done = True
        elif self.state.done:
            self.flip_state() # Troca de estado
        
        self.state.handle_collisions()
        self.state.update(self.__screen)
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__done = True
            self.state.handle_events(event)
    
    def get_keys(self):
        keys = pg.key.get_pressed()
        self.state.handle_keys(keys)
            
    def main_game_loop(self):
        while not self.__done:
            self.__clock.tick(self.__fps
)
            self.event_loop()
            self.get_keys()
            self.update()
            pg.display.update()
