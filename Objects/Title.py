# Title.py

from GameFrame import RoomObject
import pygame

class Title(RoomObject):
    """
    object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Title.png")
        self.set_image(image, 800, 350)

        self.handle_key_events = True

    def key_pressed(self, key):
        """
        if space pressed, game starts
        """
        if key[pygame.K_SPACE]:
            self.room.running = False   