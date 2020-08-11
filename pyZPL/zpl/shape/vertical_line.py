

class VLine():
    def __init__(self, length, x=0, y=0, border=1):
        self.length = length
        self.x = x
        self.y = y
        self.border = border
    def __str__(self):
        return "^FO" + str(self.x) + "," + str(self.y) \
            + "^GB1,"+ str(self.length) + "," + str(self.border) + "^FS"