from turtle import distance
import pygame as pg
from Rooms.Room2 import Room2
from States.AbstractState import AbstractState
from Sprites.Player import Player
from Rooms.RoomController import RoomController
from Sprites.Objects.Door import Door

class GameState(AbstractState):
    def __init__(self):
        super().__init__()

        self.player_sprite_group = pg.sprite.GroupSingle()
        self.attack_sprite_group = pg.sprite.Group()

        self.player_sprite_group.add(Player(start_pos=(500, 500)))


        self.room_entities_sprite_group = pg.sprite.Group()
        self.enemies_sprite_group = pg.sprite.Group()
        self.objects_sprite_group = pg.sprite.Group()
        self.walls_sprite_group = pg.sprite.Group()
        self.door_sprite_group = pg.sprite.Group()


        


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


        #colisão da porta
        for door_colission in pg.sprite.spritecollide(self.player_sprite_group.sprite, self.door_sprite_group, True, pg.sprite.collide_mask):
            self.change_room(Room2)
            break

        #colisão com paredes jogador
        if pg.sprite.spritecollide(self.player_sprite_group.sprite, self.walls_sprite_group, False):
            self.player_sprite_group.sprite.move_back()



        #colisao player_sprite_group inimigo


        # colisao inimigo ataque

        #colisao player_sprite_group porta

    def handle_keys(self, keys):
        super().handle_keys(keys)

        if keys[pg.K_1]:
            self.change_room(0)

        if keys[pg.K_2]:
            self.change_room(1)

        if keys[pg.K_3]:
            self.change_room(2)
        
        if keys[pg.K_UP]:
            print(self.room_entities_sprite_group.sprites())

        if keys[pg.K_DOWN]:
            self.room_entities_sprite_group.empty()

        #movimento player_sprite_group
        if keys[pg.K_w]:
            # self.player_sprite_group.sprite.rect.move_ip((0, -3))
            self.player_sprite_group.sprite.change_y -= 3
        
        if keys[pg.K_s]:
            # self.player_sprite_group.sprite.rect.move_ip((0, 3))
            self.player_sprite_group.sprite.change_y += 3
        
        if keys[pg.K_a]:
            # self.player_sprite_group.sprite.rect.move_ip((-3, 0))
            self.player_sprite_group.sprite.change_x -= 3
        
        if keys[pg.K_d]:
            # self.player_sprite_group.sprite.rect.move_ip((3, 0))
            self.player_sprite_group.sprite.change_x += 3

        #ataque player_sprite_group
        if pg.mouse.get_pressed()[0] and not self.player_sprite_group.sprite.in_cooldown:
            mouse_pos = pg.mouse.get_pos()
            print(mouse_pos)
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
        # Mata as entidades da sala atual
        for sprite in self.room_entities_sprite_group:
            sprite.kill()

        # Troca de sala e recebe novas entidades
        entities = self.room_controller.change_room(room_index)

        # Adiciona entidades da sala no grupo de entidades
        for entity_group in entities.values():
            self.room_entities_sprite_group.add(entity_group)

        # Adiciona as entidades em seus grupos respectivos
        self.enemies_sprite_group.add(entities['enemies'])
        self.objects_sprite_group.add(entities['objects'])
        self.walls_sprite_group.add(entities['walls'])

    def update(self, screen):
        self.attack_sprite_group.update()
        self.player_sprite_group.update()
        self.room_entities_sprite_group.update()
        
        # Controle de movimento do jogador
        self.player_sprite_group.sprite.last_pos = self.player_sprite_group.sprite.rect.center
        self.player_sprite_group.sprite.rect.move_ip(self.player_sprite_group.sprite.change_x, self.player_sprite_group.sprite.change_y)
        self.player_sprite_group.sprite.change_x = 0
        self.player_sprite_group.sprite.change_y = 0

        # for enemy in self.enemies_sprite_group:
        #     enemy.moveAI()

        self.draw(screen)

    def draw(self, screen):

        self.room_controller.draw(screen)

        for sprite in self.walls_sprite_group: #debug para ver as paredes
            pg.draw.rect(screen, (255, 255, 255), sprite.rect)

        self.attack_sprite_group.draw(screen)

        self.player_sprite_group.draw(screen)

        self.enemies_sprite_group.draw(screen)

        self.objects_sprite_group.draw(screen)

        pg.draw.rect(screen, (99, 23, 23), pg.Rect(0, 0, 1280, 180)) #HUD


