#!/usr/bin/python3

from .shape import Box, VLine, HLine
from .text import Text
from .defaults import DEFAULTFONTSIZE

"""Provide high-level zpl-writing library"""

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