import pygame as pg
from States import States
from Player import Player


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
