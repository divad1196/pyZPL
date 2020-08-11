
class Box():
    def __init__(self, length, height, x=0, y=0, border=1):
        self.length = length
        self.height = height
        self.x = x
        self.y = y
        self.border = border
    
    def __str__(self):
        return "^FO" + str(self.x) + "," + str(self.y) \
            + "^GB" + str(self.length) + "," + str(self.height) + "," + str(self.border) + "^FS"