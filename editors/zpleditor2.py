#!/usr/bin/python3
import zpl
import gtk

class Window(gtk.Window):

    def __init__(self):
        super(Window, self).__init__()
        self.set_default_size(600,600)
        self.set_title("ZPL Editor")
        label = gtk.Label("Hello World")
        self.add(label)
        self.show_all()


win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
gtk.main()