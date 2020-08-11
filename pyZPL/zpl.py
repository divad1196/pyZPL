#!/usr/bin/python3

"""Provide high-level zpl-writing library"""

DEFAULTFONTSIZE = 15

class ZPL():
    """
        Simplify the write of zpl tickets
        (The result will not be optimized and explicits every parameters)
        Starts with ZPL class
        exemple of use:

            zpl = ZPL(78,49,6)
            text = zpl.Text(300,x=100,fontsize=20)
            ligne1 = text.newLine("salut")
            text.fontsize = 12
            ligne = text.newLine("ca va?")
            text.fontsize = 40
            ligne1 = text.newLine("Test")

            print(zpl) #return the wanted zpl code
    """
    _start = "^XA"
    _end = "^XZ"
    def __init__(self, width, height, dpmm):
        """
        width and height given in mm
        """
        self.width = width
        self.height = height
        self.dpmm = dpmm
        self._childs = []

    def __str__(self):
        text = self._start
        for child in self._childs:
            text = text + "\n" + str(child)
        text = text + "\n" + self._end
        return text

    def tostring(self):
        """Return the zpl as a string, without formating"""
        return str(self).replace("\n","")

    def w_px(self):
        """Return the width in pixels"""
        return self.width * self.dpmm

    def h_px(self):
        """Return the height in pixels"""
        return self.height * self.dpmm
    
    def _addChild(self, child):
        self._childs.append(child)
        return child

    def VLine(self, length, x=0, y=0, border=1):
        tmp = VLine(length,x,y,border)
        return self._addChild(tmp)

    def HLine(self, length, x=0, y=0, border=1):
        tmp = HLine(length,x,y,border)
        return self._addChild(tmp)

    def Box(self, length, height, x=0, y=0, border=1):
        tmp = Box(length,height,x,y,border)
        return self._addChild(tmp)

    def Text(self,
        width,
        x=0,
        y=0,
        border=False,
        interline=1,
        fontsize=DEFAULTFONTSIZE,
        align="L"
    ):
        tmp = _Text(
            width,
            x,
            y,
            border,
            interline,
            fontsize,
            align
        )
        return self._addChild(tmp)

    def NText(
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
    ):
        tmp = _NText(
            text=text,
            width=width,
            x=x,
            y=y,
            h=h,
            w=w,
            align=align,
            max_line=max_line,
            interline=interline,
            indent=indent
        )
        return self._addChild(tmp)

class _TextLine():
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


class _NText():
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
        tmp = _TextLine(text,width,x,y,font_height,font_width,text_align)
        return self._addChild(tmp)

    def read(self):
        """Show the text content"""
        for child in self._childs:
            print(child.text)

    


class VLine():
    def __init__(self, length, x=0, y=0, border=1):
        self.length = length
        self.x = x
        self.y = y
        self.border = border
    def __str__(self):
        return "^FO" + str(self.x) + "," + str(self.y) \
            + "^GB1,"+ str(self.length) + "," + str(self.border) + "^FS"
    

class HLine():
    def __init__(self, length, x=0, y=0, border=1):
        self.length = length
        self.x = x
        self.y = y
        self.border = border
    
    def __str__(self):
        return "^FO" + str(self.x) + "," + str(self.y)\
            + "^GB" + str(self.length) + ",1," + str(self.border) + "^FS"

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

class _BarCode():
    def __init__(self, text, x=0, y=0):
        self.width = 2
        self.text = text
        self.x = x
        self.y = y
    
    def __str__(self):
        return "^FO" + str(self.x) + "," + str(self.y) + "\n" \
            + "^BY"+ str(self.width) + "\n" \
            + "^FD" + self.text + "^FS"

