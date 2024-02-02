# WelcomeScreen

from GameFrame import Level
from Objects.Title import Title

class WelcomeScreen(Level):
    """
    initial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        ## background image
        self.set_background_image("background.png")

        ## add title
        self.add_room_object(Title(self, 240, 200))