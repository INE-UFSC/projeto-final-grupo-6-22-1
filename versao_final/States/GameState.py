import pygame as pg
from States.AbstractState import AbstractState
from Sprites.Player import Player
from Rooms.RoomController import RoomController

class GameState(AbstractState):
    def __init__(self):
        super().__init__()

        self.player_sprite_group = pg.sprite.GroupSingle()
        self.attack_sprite_group = pg.sprite.Group()

        self.player_sprite_group.add(Player(start_pos=(200, 200)))

        self.room_entities_sprite_group = pg.sprite.Group()
        self.enemies_sprite_group = pg.sprite.Group()
        self.objects_sprite_group = pg.sprite.Group()
        self.walls_sprite_group = pg.sprite.Group()


        self.room_controller = RoomController()


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

        if keys[pg.K_LEFT]:
            self.change_room(0)

        if keys[pg.K_RIGHT]:
            self.change_room(1)
        
        if keys[pg.K_UP]:
            print(self.room_entities_sprite_group.sprites())

        if keys[pg.K_DOWN]:
            self.room_entities_sprite_group.empty()

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

    def change_room(self, room_index):
        self.room_entities_sprite_group.empty()
        entities = self.room_controller.change_room(room_index)
        for entity_group in entities.values():
            self.room_entities_sprite_group.add(entity_group)

    def update(self, screen):
        self.attack_sprite_group.update()
        self.player_sprite_group.update()
        self.room_entities_sprite_group.update()
        self.draw(screen)

    def draw(self, screen):

        self.room_controller.draw(screen)

        pg.draw.rect(screen, (99, 23, 23), pg.Rect(0, 0, 1280, 180)) #HUD

        self.attack_sprite_group.draw(screen)

        self.player_sprite_group.draw(screen)

        self.room_entities_sprite_group.draw(screen)
