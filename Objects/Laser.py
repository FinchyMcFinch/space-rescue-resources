# Laser.py

from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    """
    small flying light
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image("Laser.png"), 33, 9)

        ## travel direction
        speed = 20
        self.set_direction(0, speed)

        self.register_collision_object("Asteroid")
        self.register_collision_object("Astronaut")

    def step(self):
        """
        game tick
        """
        self.outside_room()
    
    def outside_room(self):
        """
        prune old lasers
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        """
        only runs if the user can aim worth a damn
        """
        if other_type == "Asteroid":
            self.room.delete_object(other)
        elif other_type == "Astronaut":
            self.room.delete_object(other)