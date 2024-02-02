# Title.py

from GameFrame import RoomObject

class Title(RoomObject):
    """
    object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("Title.png")
        self.set_image(image, 800, 350)