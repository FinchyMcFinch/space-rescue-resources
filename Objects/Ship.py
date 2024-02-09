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

    def key_pressed(self, key):
        """
        vertical movement
        """
        if key[pygame.K_w]:
            self.y_speed -= self.movement_speed
        
        elif key[pygame.K_s]:
            self.y_speed += self.movement_speed

    def step(self):
        """
        game tick
        """
        self.keep_in_room()
        if not self.check_key(pygame.K_w) and self.y_speed < 0:


    def check_key(self, key_id):
        """
        check if given key is pressed
        """
        flag = False
        for event in pygame.event.get:
            if event.type == pygame.KEYDOWN:
                if event.key == key_id:
                    flag = True
        if flag:
            return True
        return False

    def keep_in_room(self):
        """
        check for collision with border
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height