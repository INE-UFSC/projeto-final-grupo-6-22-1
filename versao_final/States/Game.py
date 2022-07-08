import pygame as pg
from States.State import State
from Sprites.Player import Player


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

class Game(State):
    def __init__(self):
        State.__init__(self)

        self.player_sprite_group = pg.sprite.GroupSingle()
        self.attack_sprite_group = pg.sprite.Group()
        self.player_sprite_group.add(Player(start_pos=(200, 200)))

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
        for attack_colission in pg.sprite.spritecollide(self.player_sprite_group.sprite, self.attack_sprite_group, True, pg.sprite.collide_mask):
            self.player_sprite_group.sprite.damage_taken(damage = attack_colission.damage)

            if self.player_sprite_group.sprite.health <= 0:
                self.next = "game_over"
                self.done = True

        #colisao player_sprite_group parede


        #colisao player_sprite_group inimigo


        # colisao inimigo ataque

        #colisao player_sprite_group porta

    def handle_keys(self, keys):
        super().handle_keys(keys)

        #movimento player_sprite_group
        if keys[pg.K_w]:
            self.player_sprite_group.sprite.rect.move_ip((0, -3))
        
        elif keys[pg.K_s]:
            self.player_sprite_group.sprite.rect.move_ip((0, 3))
        
        elif keys[pg.K_a]:
            self.player_sprite_group.sprite.rect.move_ip((-3, 0))
        
        elif keys[pg.K_d]:
            self.player_sprite_group.sprite.rect.move_ip((3, 0))

        #ataque player_sprite_group
        if pg.mouse.get_pressed()[0] and not self.player_sprite_group.sprite.in_cooldown:
            mouse_pos = pg.mouse.get_pos()
            player_pos = self.player_sprite_group.sprite.rect.center
            difference_pos = (player_pos[0] - mouse_pos[0], player_pos[1] - mouse_pos[1])

            if difference_pos[1] > 0 and difference_pos[1] > abs(difference_pos[0]):
                self.attack_sprite_group.add(self.player_sprite_group.sprite.attack('up'))
            
            elif difference_pos[1] < 0 and abs(difference_pos[1]) > abs(difference_pos[0]):
                self.attack_sprite_group.add(self.player_sprite_group.sprite.attack('down'))
            
            elif difference_pos[0] > 0 and difference_pos[0] > abs(difference_pos[1]):
                self.attack_sprite_group.add(self.player_sprite_group.sprite.attack('left'))
            
            elif difference_pos[0] < 0 and abs(difference_pos[0]) > abs(difference_pos[1]):
                self.attack_sprite_group.add(self.player_sprite_group.sprite.attack('right'))

    def update(self, screen):
        self.attack_sprite_group.update()
        self.player_sprite_group.update()
        self.draw(screen)

    def draw(self, screen):

        self.current_room.draw_background(screen)

        pg.draw.rect(screen, (99, 23, 23), pg.Rect(0, 0, 1280, 180)) #HUD

        self.attack_sprite_group.draw(screen)

        self.player_sprite_group.draw(screen)
