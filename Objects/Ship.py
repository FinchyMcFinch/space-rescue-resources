# Ship.py

from GameFrame import RoomObject, Globals
import pygame

class Ship(RoomObject):
    """
    player avatar
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Ship.png")
        self.set_image(image, 100, 100)

        self.handle_key_events = True

        self.movement_speed = 2
        self.move_key = 0
        # 1 = w
        # 2 = s

    def key_pressed(self, key):
        """
        vertical movement
        """
        if key[pygame.K_w]:
            self.y_speed -= self.movement_speed
            self.move_key = 1
        
        elif key[pygame.K_s]:
            self.y_speed += self.movement_speed
            self.move_key = 2

    def step(self):
        """
        game tick
        """
        self.decelerate()
        self.keep_in_room()
    
    def decelerate(self):
        """
        decelerate ship passively
        """
        if self.move_key == 0:
            if self.y_speed < 0:
                self.y_speed += self.movement_speed
            elif self.y_speed > 0:
                self.y_speed -= self.movement_speed
        self.move_key = 0

    def keep_in_room(self):
        """
        check for collision with border
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height