from ..defaults import DEFAULTFONTSIZE


class NText():
    """N stand for Native, it implements the native text field of zpl """
    def __init__(
        self,
        text,
        width,
        x=0,
        y=0,
        h=DEFAULTFONTSIZE,
        w=DEFAULTFONTSIZE,
        align="L",
        max_line=1,
        interline=0,
        indent=0
    ):#,border=False
        """ x and y: origin position (up-left corner)
            h and w: height and width of characters
            max_line: maximum lines authorized, used to handle text exceeding
            interline: from -9999 to 9999
            align: L(left), C(center), R(right), J(justified)"""

        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.text = text
        self.width = width
        self.align = align
        self.max = max_line
        self.interline = interline
        self.indent = indent

    def __str__(self):
        return "^CF0," + str(self.h) + "," + str(self.w) + "\n" \
            + "^FB" + str(self.width) + "," + str(self.max) +"," + str(self.interline) + "," + self.align + "," + str(self.indent) + "\n" \
            + "^FO" + str(self.x) + "," + str(self.y) + "\n" \
            + "^FD" + self.text + "^FS" + "\n"