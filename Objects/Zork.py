# Zork.py

from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
import random


class Zork(RoomObject):
    """
    what did my man zork ever do to you to become the antagonist??
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image("Zork.png"), 135, 165)

        self.movement_speed = (10 * 30)/Globals.FRAMES_PER_SECOND ## numbers in brackets are desired speed at given fps
        self.y_speed = random.choice([-self.movement_speed, self.movement_speed])
        self.turnaround_chance = 0.4

        asteroid_spawn_time = 35
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)

    def keep_in_room(self):
        """
        check for collision with border
        """
        if self.y < 0:
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1

    def step(self):
        """
        game tick
        """
        self.keep_in_room()
        chance = round(random.random()*100,2)
        if chance < self.turnaround_chance:
            self.y_speed *= -1

    def spawn_asteroid(self):
        """
        randomly spawns big rock
        """
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)

        asteroid_spawn_time = random.randint(20, 250)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)