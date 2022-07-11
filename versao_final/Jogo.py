import pygame as pg
import sys

from States.GameState import GameState
from States.MenuState import MenuState
from States.GameOverState import GameOverState

TAMANHO_TELA = (1280, 720)


pg.init()

menu_font = pg.font.Font(pg.font.get_default_font(), 90)

class Control:
    def __init__(self):
        self.done = False
        self.fps = 60
        self.screen = pg.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        # Função que troca de estado atual para proximo estado
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        #self.state.cleanup() # talvez usar
        self.state = self.state_dict[self.state_name]
        #self.state.startup() # talvez usar
        self.state.previous = previous

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state() # Troca de estado
        
        self.state.handle_collisions()
        self.state.update(self.screen)
        
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.handle_events(event)
    
    def get_keys(self):
        keys = pg.key.get_pressed()
        self.state.handle_keys(keys)
            
    def main_game_loop(self):
        while not self.done:
            self.clock.tick(self.fps)
            self.event_loop()
            self.get_keys()
            self.update()
            pg.display.update()

   
jogo = Control()
state_dict = {
    'menu': MenuState(menu_font),
    'game': GameState(),
    'game_over': GameOverState(menu_font),
    #win
}
jogo.setup_states(state_dict, 'game_over')
jogo.main_game_loop()

pg.quit()
sys.exit()
