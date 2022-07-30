import pygame as pg
from Sprites.Entity import Entity

class Attack(Entity):
    def __init__(self, start_pos, direction, damage, damages_player, time_spawned, image_folder="attacks", image_name="chicote.png", image_size=(100, 100),):
        # Inicialização
        super().__init__(start_pos, image_folder, image_name, image_size)

        if direction == 'up':
            angle = 180
            attack_pos = (start_pos[0], start_pos[1]-80)
        
        elif direction == 'down':
            angle = 0
            attack_pos = (start_pos[0], start_pos[1]+80)

        elif direction == 'left':
            angle = 270
            attack_pos = (start_pos[0]-60, start_pos[1])

        elif direction == 'right':
            angle = 90
            attack_pos = (start_pos[0]+60, start_pos[1])

        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = attack_pos
        
        self.mask = pg.mask.from_surface(self.image)

        self.damages_player = damages_player
        self.damage = damage

        self.time_spawned = time_spawned
        self.start_time = pg.time.get_ticks()

    def update(self):
        if pg.start_time.get_ticks() - self.time >= self.time_spawned:
            self.kill()

    def hit(self):
        self.kill()
