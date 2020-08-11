from ..defaults import DEFAULTFONTSIZE
from .text_line import TextLine

class _Text():
    def __init__(self,width,x=0,y=0,border=False,interline=0,fontsize=DEFAULTFONTSIZE,align="L"):
        """ x and y: origin position
            h and w: height and width of characters
            width: width of the text field
            align: L(left), C(center), R(right), J(justified)"""

        self.x = x
        self.y = y
        self.border = border
        self.width = width
        self.interline = interline
        self.fontsize = fontsize
        self.align = align
        self._childs = []

    def __str__(self):
        text = ""
        for child in self._childs:
            text = text + str(child)
        return text

    def _addChild(self, child):
        self._childs.append(child)
        return child
    
    def newLine(self,text,h=False,w=False,align=False):
        """Add a new line to the text"""
        font_height = h
        font_width = w
        if font_height == False:
            font_height = self.fontsize
        if font_width == False:
            font_width = self.fontsize
        text_align = align
        if text_align == False:
            text_align = self.align
        width = self.width
        x = self.x
        if len(self._childs) == 0:   
            y = self.y
        else:
            last_child = self._childs[-1]
            y = last_child.y + last_child.h
        tmp = TextLine(
            text,
            width,
            x,
            y,
            font_height,
            font_width,
            text_align,
        )
        return self._addChild(tmp)

    def read(self):
        """Show the text content"""
        for child in self._childs:
            print(child.text)