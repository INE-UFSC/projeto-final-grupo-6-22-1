import pygame as pg
import sys
import os

TAMANHO_TELA = (1280, 720)

TAMANHO_PERSONAGEM = (28, 78)


pg.init()

menu_font = pg.font.Font(pg.font.get_default_font(), 90)

# Pré-carregamento de imagens
image_cache = {}

def get_image(folder, key):
    """
    Retorna imagem do cache, se não está carregada, carrega
    """
    if not key in image_cache:
        image_cache[key] = pg.image.load(os.path.join("images", folder, key)).convert_alpha()

    return image_cache[key]

class Player(pg.sprite.Sprite):
    """
    Classe do jogador
    """

    def __init__(self, start_pos = (0, 0)):
        """
        Spawna um jogador na coordenada x,y
        """
        # Inicialização
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.smoothscale(get_image("player", "quadrado.png"), TAMANHO_PERSONAGEM)

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        # Coordenadas iniciais
        self.rect.centerx, self.rect.centery = start_pos

        self.health = 300

        self.in_cooldown = False
        self.last_shot_time = 0

    def update(self):
        """
        Atualiza a sprite
        """
        if pg.time.get_ticks() - self.last_shot_time >= 800: #cooldown especifico arma
            self.in_cooldown = False

    def attack(self, direct):
        """
        Ataca na direção informada e retorna ataque
        """
        attk = Attack(attacker_pos=self.rect.center, direction=direct, format='triangular', damage=1,damages_player=False, time_spawned=300)
        self.in_cooldown = True
        self.last_shot_time = pg.time.get_ticks()
        return attk

    def damage_taken(self, damage):
        """
        Recebe dano
        """
        self.health = self.health - damage
        print(self.health)

class Attack(pg.sprite.Sprite):
    def __init__(self, attacker_pos, direction, format, damage, damages_player, time_spawned):
        # Inicialização
        pg.sprite.Sprite.__init__(self)

        if direction == 'up':
            angle = 180
            attack_pos = (attacker_pos[0], attacker_pos[1]-80)
        
        elif direction == 'down':
            angle = 0
            attack_pos = (attacker_pos[0], attacker_pos[1]+80)

        elif direction == 'left':
            angle = 270
            attack_pos = (attacker_pos[0]-60, attacker_pos[1])

        elif direction == 'right':
            angle = 90
            attack_pos = (attacker_pos[0]+60, attacker_pos[1])


        if format=='vertical_pipe':
            self.image = pg.transform.smoothscale(get_image("attacks", "quadrado.png"), (40, 80))

        elif format=='triangular':
            self.image = pg.transform.smoothscale(get_image("attacks", "triangulo.png"), (300, 140))


        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = attack_pos
        
        self.mask = pg.mask.from_surface(self.image)

        self.damages_player = damages_player
        self.damage = damage

        self.time_spawned = time_spawned
        self.time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.time >= self.time_spawned:
            self.kill()
        
class Room(object):
    def __init__(self):
        self.visited = False
    
    def draw_background(self, screen):
        """
        Pinta a sala de branco caso não informado background
        """
        screen.fill((255, 255, 255))

    def draw_art(self):
        pass

    def load(self, entry_point):
        """
        Carrega a sala, entry point indica de que direção o player veio
        """


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
        self.state.cleanup() # talvez usar
        self.state = self.state_dict[self.state_name]
        self.state.startup() # talvez usar
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
             
class States():
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

    def cleanup(self):
        pass

    def startup(self):
        pass
    
    def handle_events(self, events):
        pass

    def handle_collisions(self):
        pass

    def handle_keys(self, keys):
        if keys[pg.K_ESCAPE]:
            self.quit = True

    def update(self, screen):
        pass
                 
class Menu(States):
    def __init__(self):
        States.__init__(self)

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
        
         
class Game(States):
    def __init__(self):
        States.__init__(self)

        self.jogador = pg.sprite.GroupSingle()
        self.attacks = pg.sprite.Group()
        self.jogador.add(Player(start_pos=(200, 200)))

        self.current_room = Room()

    # def cleanup(self):

    # def startup(self):

    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.quit = True

    def handle_collisions(self):
        for attack_colission in pg.sprite.spritecollide(self.jogador.sprite, self.attacks, True, pg.sprite.collide_mask):
            self.jogador.sprite.damage_taken(damage = attack_colission.damage)

            if self.jogador.sprite.health <= 0:
                self.next = "game_over"
                self.done = True

        #colisao jogador parede


        #colisao jogador inimigo


        # colisao inimigo ataque

        #colisao jogador porta

    def handle_keys(self, keys):
        super().handle_keys(keys)

        #movimento jogador
        if keys[pg.K_w]:
            self.jogador.sprite.rect.move_ip((0, -3))
        
        elif keys[pg.K_s]:
            self.jogador.sprite.rect.move_ip((0, 3))
        
        elif keys[pg.K_a]:
            self.jogador.sprite.rect.move_ip((-3, 0))
        
        elif keys[pg.K_d]:
            self.jogador.sprite.rect.move_ip((3, 0))

        #ataque jogador
        if pg.mouse.get_pressed()[0] and not self.jogador.sprite.in_cooldown:
            mouse_pos = pg.mouse.get_pos()
            player_pos = self.jogador.sprite.rect.center
            difference_pos = (player_pos[0] - mouse_pos[0], player_pos[1] - mouse_pos[1])

            if difference_pos[1] > 0 and difference_pos[1] > abs(difference_pos[0]):
                self.attacks.add(self.jogador.sprite.attack('up'))
            
            elif difference_pos[1] < 0 and abs(difference_pos[1]) > abs(difference_pos[0]):
                self.attacks.add(self.jogador.sprite.attack('down'))
            
            elif difference_pos[0] > 0 and difference_pos[0] > abs(difference_pos[1]):
                self.attacks.add(self.jogador.sprite.attack('left'))
            
            elif difference_pos[0] < 0 and abs(difference_pos[0]) > abs(difference_pos[1]):
                self.attacks.add(self.jogador.sprite.attack('right'))

    def update(self, screen):
        self.attacks.update()
        self.jogador.update()
        self.draw(screen)

    def draw(self, screen):

        self.current_room.draw_background(screen)

        pg.draw.rect(screen, (99, 23, 23), pg.Rect(0, 0, 1280, 180)) #HUD

        self.attacks.draw(screen)

        self.jogador.draw(screen)
    


   
jogo = Control()
state_dict = {
    'menu': Menu(),
    'game': Game(),
    #win
    #game_over
}
jogo.setup_states(state_dict, 'menu')
jogo.main_game_loop()

pg.quit()
sys.exit()
