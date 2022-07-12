from Rooms.Room1 import Room1
from Rooms.Room2 import Room2

class RoomController():
    def __init__(self):
        self.rooms = [Room1(), Room2()]
        self.current_room = self.rooms[0]

    def draw(self, screen):
        self.current_room.draw_background(screen)
        self.current_room.draw_art(screen)

    def change_room(self, room_index):
        self.current_room.unload()
        self.current_room = self.rooms[room_index]

        return self.current_room.load((1,1))
        #self.room_entities.add(self.current_room.start_walls())
        
    