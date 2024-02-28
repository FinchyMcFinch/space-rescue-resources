# Ship.py

from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

class Ship(RoomObject):
    """
    player avatar
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.set_image(self.load_image("Ship.png"), 100, 100)

        self.handle_key_events = True

        self.movement_speed = (2 * 30)/Globals.FRAMES_PER_SECOND ## numbers in brackets are desired speed at given fps
        self.move_key = 0
        # 1 = w
        # 2 = s
        self.bounciness = -0.4

        self.can_shoot = True
        self.shoot_cooldown = 10

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
             
        elif key[pygame.K_SPACE]:
            self.shoot_laser()

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
        if self.y_speed > -self.movement_speed and self.y_speed < self.movement_speed:
            self.y_speed = 0
            return
        if self.move_key == 0 and self.y_speed != 0:
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
            self.y_speed *= self.bounciness
        elif self.y + self.height > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= self.bounciness
    
    def shoot_laser(self):
        """
        pew pew
        """
        if self.can_shoot:
            new_laser = Laser(self.room,
                              self.x + self.width,
                              self.y + self.height/2)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(self.shoot_cooldown, self.reset_shot)

    def reset_shot(self):
        self.can_shoot = True