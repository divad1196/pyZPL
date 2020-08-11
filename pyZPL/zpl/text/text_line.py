from ..defaults import DEFAULTFONTSIZE


class TextLine():
    def __init__(
        self,
        text,
        width,
        x=0,
        y=0,
        h=DEFAULTFONTSIZE,
        w=DEFAULTFONTSIZE,
        align="L"
    ):
        """ x and y: origin position
            h and w: height and width of characters
            width: width of the text field
            align: L(left), C(center), R(right), J(justified)"""

        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.text = text
        self.width = width
        self.align = align

    def __str__(self):
        return "^CF0," + str(self.h) + "," + str(self.w) + "\n" \
            + "^FB" + str(self.width) + ",1,0," + self.align + ",0" "\n" \
            + "^FO" + str(self.x) + "," + str(self.y) + "\n" \
            + "^FD" + self.text + "^FS" + "\n"