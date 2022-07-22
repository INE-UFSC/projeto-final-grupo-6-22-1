from Rooms.Room1 import Room1
from Rooms.Room2 import Room2
from Rooms.Room3 import Room3
from Rooms.Room4 import Room4
from Rooms.Room5 import Room5
from Rooms.Room6 import Room6
from Rooms.Room7 import Room7
from Rooms.Room8 import Room8
from Rooms.Room9 import Room9


class RoomController():
    def __init__(self):
        self.rooms = [Room1(), Room2(), Room3(), Room4(), Room5(), Room6(), Room7(), Room8(), Room9()]
        self.current_room = self.rooms[0]

    def draw(self, screen):
        self.current_room.draw_background(screen)
        self.current_room.draw_art(screen)

    def change_room(self, room_index):
        self.current_room.unload()
        self.current_room = self.rooms[room_index]

        return self.current_room.load((1,1))
        #self.room_entities.add(self.current_room.start_walls())
        
    