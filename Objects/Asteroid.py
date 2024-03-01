# Asteroid.py

from GameFrame import RoomObject, Globals
import random

class Asteroid(RoomObject):
    """
    big flying rock
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        dimension = random.choice([40, 50, 60, 75])
        if random.randint(1, 100) <= 3:
            dimension = 175
            self.x -= 100
            speed = 3
        self.set_image(self.load_image("asteroid.png"), dimension, dimension)

        ## travel direction
        speed = (10*50)/self.width
        self.set_direction(random.randint(135, 225), speed)

        self.register_collision_object("Ship")

    def step(self):
        """
        game tick
        """
        self.keep_in_room()
        self.outside_room()

    def keep_in_room(self):
        """
        check for collision with border
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1

    def outside_room(self):
        """
        prune old asteroids
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        """
        check for collisions
        """
        if other_type == "Ship":
            self.room.delete_object(self)
            Globals.LIVES -= 1
            if Globals.LIVES != 0:
                self.room.lives.update_image()
            else:
                self.room.running = False