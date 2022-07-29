import pygame as pg
from get_image import get_image
from States.AbstractState import AbstractState
from Sprites.Player import Player
from Rooms.RoomController import RoomController

class GameState(AbstractState):
    def __init__(self):
        super().__init__()

        self.player_sprite_group = pg.sprite.GroupSingle()
        self.attack_sprite_group = pg.sprite.Group()




        self.room_entities_sprite_group = pg.sprite.Group()
        self.enemies_sprite_group = pg.sprite.Group()
        self.objects_sprite_group = pg.sprite.Group()
        self.walls_sprite_group = pg.sprite.Group()
        self.door_sprite_group = pg.sprite.Group()

        self.start_time = 0

        self.room_controller = RoomController()

    def cleanup(self):
        for sprite in self.room_entities_sprite_group:
            sprite.kill()

        self.player_sprite_group.sprite.kill()

        if self.next == "win":
            return pg.time.get_ticks() - self.start_time
        else:
            return -1

    def startup(self):
        self.player_sprite_group.add(Player(start_pos=(500, 500)))
        self.start_time = pg.time.get_ticks()
        self.end_time = -1
        self.change_room(0)

    def handle_events(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.quit = True

        if event.type == pg.USEREVENT+1:
            if event.__dict__["enemy_name"] == "Strahd":
                self.next = "win"
                self.done = True

    def handle_collisions(self):
        for attack_colission in pg.sprite.spritecollide(self.player_sprite_group.sprite, self.attack_sprite_group, False, pg.sprite.collide_mask):
            if attack_colission.damages_player:
                self.player_sprite_group.sprite.damage_taken(damage = attack_colission.damage)

            if self.player_sprite_group.sprite.health <= 0:
                self.next = "game_over"
                self.done = True

        #colisão com paredes jogador
        if pg.sprite.spritecollide(self.player_sprite_group.sprite, self.walls_sprite_group, False, lambda sprite1, sprite2: sprite1.hitbox.colliderect(sprite2.rect)):
            self.player_sprite_group.sprite.move_back()

        #Tentativa de colisão do jogador com objetos
        if pg.sprite.spritecollide(self.player_sprite_group.sprite, self.objects_sprite_group, False, lambda sprite1, sprite2: sprite1.hitbox.colliderect(sprite2.rect)):
            self.player_sprite_group.sprite.move_back()    
            
        #colisão inimigos
        for enemy in self.enemies_sprite_group:
            if enemy.name == "Bat": # colisão morcego com parede
                for wall in pg.sprite.spritecollide(enemy, self.walls_sprite_group, False):
                    enemy.change_direction(wall.rect)
                    
        #colisao player_sprite_group inimigo
        for enemy_colission in pg.sprite.spritecollide(self.player_sprite_group.sprite, self.enemies_sprite_group, False, lambda sprite1, sprite2: sprite1.hitbox.colliderect(sprite2.rect)):
            self.player_sprite_group.sprite.damage_taken(damage = enemy_colission.damage)

            if self.player_sprite_group.sprite.health <= 0:
                self.next = "game_over"
                self.done = True

        # colisao inimigo ataque
        for attack in self.attack_sprite_group:
            for enemy in pg.sprite.spritecollide(attack, self.enemies_sprite_group, False, pg.sprite.collide_mask):
                enemy.damage_taken(damage = attack.damage)
                #attack.hit()




        #colisao player_sprite_group porta

    def handle_keys(self, keys):
        super().handle_keys(keys)

        if keys[pg.K_1]:
            self.change_room(0)

        if keys[pg.K_2]:
            self.change_room(1)

        if keys[pg.K_3]:
            self.change_room(2)

        if keys[pg.K_4]:
            self.change_room(3)
        
        if keys[pg.K_5]:
            self.change_room(4)

        if keys[pg.K_6]:
            self.change_room(5)

        if keys[pg.K_7]:
            self.change_room(6)

        if keys[pg.K_8]:
            self.change_room(7)

        if keys[pg.K_9]:
            self.change_room(8)

        if keys[pg.K_0]:
            self.change_room(9)
 
        
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
        

        #interação com objetos
        if keys[pg.K_SPACE]:
            if self.room_controller.current_room.cleared:
                for objeto in self.objects_sprite_group:
                    distancia = ((self.player_sprite_group.sprite.hitbox.centerx - objeto.rect.centerx)**2 + (self.player_sprite_group.sprite.hitbox.centery - objeto.rect.centery)**2)**0.5
                    if distancia < 100:
                        mudar_sala = objeto.interaction(self.player_sprite_group.sprite)
                        if mudar_sala:
                            self.change_room(mudar_sala)


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

        if self.room_controller.current_room.cleared == True:
            for sprite in self.enemies_sprite_group:
                sprite.kill()
        # Altera posicao do jogador
        self.player_sprite_group.sprite.hitbox.center = (500, 500)

    def update(self, screen):
        self.attack_sprite_group.update()
        self.player_sprite_group.update()
        self.room_entities_sprite_group.update()
        
        # Controle de movimento do jogador
        self.player_sprite_group.sprite.last_pos = self.player_sprite_group.sprite.hitbox.center
        self.player_sprite_group.sprite.hitbox.move_ip(self.player_sprite_group.sprite.change_x, self.player_sprite_group.sprite.change_y)
        self.player_sprite_group.sprite.change_x = 0
        self.player_sprite_group.sprite.change_y = 0

        for enemy in self.enemies_sprite_group:
            movement = enemy.ai_move(self.player_sprite_group.sprite.hitbox.center)
            enemy.rect.move_ip(movement[0], movement[1])

        if not self.enemies_sprite_group:
            self.room_controller.current_room.cleared = True

        self.draw(screen)

    def draw(self, screen):

        self.room_controller.draw(screen)

        for sprite in self.walls_sprite_group: #debug para ver as paredes
            pg.draw.rect(screen, (255, 255, 255), sprite.rect)

        self.objects_sprite_group.draw(screen)

        self.attack_sprite_group.draw(screen)

        self.enemies_sprite_group.draw(screen)

        self.player_sprite_group.draw(screen)


        # hud
        pg.draw.rect(screen, (99, 23, 23), pg.Rect(0, 0, 1280, 180))

        img = get_image("art", "coracao.png")
        img = pg.transform.smoothscale(img, (280, 295))
        screen.blit(img, (1000, -70))
        screen.blit(pg.font.Font(pg.font.get_default_font(), 60).render(str(self.player_sprite_group.sprite.health), 1, (0, 0, 0)), (1130, 60))
