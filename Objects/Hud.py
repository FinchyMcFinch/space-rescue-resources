# Hud.Py

from GameFrame import TextObject, Globals, RoomObject

class Score(TextObject):
    """
    the current score
    """
    def __init__(self, room, x, y, text=None):
        TextObject.__init__(self, room, x, y, text)

        self.size = 60
        self.font = "Arial Black"
        self.colour = (255, 255, 255)
        self.bold = False
        self.update_text()

    def update_score(self, change):
        """
        update and redraw
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()

class Lives(RoomObject):
    """
    number of lives
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.lives_icon = []
        for i in range(6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{i}.png"))
        self.update_image()

    def update_image(self):
        """
        updates number of lives shown
        """
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)