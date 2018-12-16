#!/usr/bin/python3
import zpl
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ZPL Editor")
        self.dc = self.window.cairo_create()

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()