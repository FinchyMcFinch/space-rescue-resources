# Hud.Py

from GameFrame import TextObject, Globals

class Score(TextObject):
    """
    the current score
    """
    def __init__(self, room , x:int, y:int, text=None):
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