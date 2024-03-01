# Astronaut.py

from GameFrame import RoomObject

class Astronaut(RoomObject):
    """
    no witty comment. it's just an astronaut.
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image("Astronaut.png"), 50, 49)

        ## travel direction
        speed = 5
        self.set_direction(180, speed)

        self.register_collision_object("Ship")

    def step(self):
        """
        game tick
        """
        self.outside_room()

    def outside_room(self):
        """
        prune old astronauts
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
    
    def handle_collision(self, other, other_type):
        """
        check for collisions
        """
        if other_type == "Ship":
            self.room.delete_object(self)