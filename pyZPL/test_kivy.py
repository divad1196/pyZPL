import kivy
from kivy import uix
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.splitter import Splitter
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.actionbar import ActionBar, ActionDropDown, ActionGroup, ActionButton, ActionView, ActionItem, ActionPrevious
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Line, Color, ClearColor

WHITE = (1, 1, 1, 1)

import numpy

def substract(t1, t2):
    return tuple(numpy.substract(t1, t2))

class Canvas(Widget):
    # https://stackoverflow.com/questions/59825759/how-to-rotate-two-rectangle-widgets-independently-on-single-screen-in-kivy
    def __init__(self, bcolor=WHITE, **kwargs):
        # if "pos_hint" not in kwargs:
        #     kwargs["pos_hint"] = {'top': 1}
        print(kwargs)
        super(Canvas, self).__init__(**kwargs)
        if len(bcolor) == 3:
            bcolor += (1, )
        self.bcolor = bcolor
        self.clear()

    def clear(self):
        self.canvas.clear()
        with self.canvas:
            Color(rgba=self.bcolor)
            Rectangle(pos=self.pos, size=self.size)

    def line(self, x1, y1, x2, y2):
        with self.canvas:
            Line(points=[x1, y1, x2, y2])

    def rectangle(self, x, y, width, height, rgba=None):
        with self.canvas:
            if rgba:
                Color(rgba=rgba)
            Rectangle(pos=(x, y), size=(width, height))

def get_button_layout(**kwargs):
        splitter = Splitter(**kwargs)

        button_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))

        scroll = ScrollView()
        scroll.add_widget(button_layout)
        
        splitter.add_widget(scroll)

        return splitter, button_layout


class TestApp(App):
    def build(self):
        _layout = BoxLayout(orientation='vertical')

        self._set_menubar(_layout)


        main_layout = BoxLayout(orientation='horizontal')
        _layout.add_widget(main_layout)
        self.main_layout = main_layout

        canvas = Canvas(size=(500, 500))
        self.canvas = canvas
        main_layout.add_widget(canvas)

        self._set_button_layout()
        # label = Label(text="ZPL")
        return _layout

    def _set_menubar2(self, parent_widget):
        menu = ActionBar()
        parent_widget.add_widget(menu)
        self.menu = menu

        previous_button = ActionButton(text="Previous")
        action_view = ActionView(action_previous=previous_button)
        menu.add_widget(action_view)
        add_buttons = ActionDropDown()
        action_view.add_widget(add_buttons)

        self._set_add_buttons(add_buttons)

    def _set_menubar(self, parent_widget):
        menu = BoxLayout(orientation='horizontal', size_hint_max_y=50)
        parent_widget.add_widget(menu)
        self.menu = menu

        add_buttons = DropDown()
        dropdown_button = Button(text='Add', size_hint_max_x=100)
        dropdown_button.bind(on_release=add_buttons.open)
        # add_buttons.bind(on_select=lambda instance, x: setattr(dropdown_button, 'text', x))

        menu.add_widget(dropdown_button)

        self._set_add_buttons(add_buttons)

        for b in add_buttons.children[0].children:
            print(b.text)

    def _set_add_buttons(self, parent_widget):
        def add(text, on_press):
            btn = Button(text=text, size_hint_y=None, height=44)
            btn.bind(on_press=on_press)
            parent_widget.add_widget(btn)

        add(
            "Box",
            lambda instance: self.new_box(),
        )
        add(
            "Hline",
            lambda instance: self.new_hline(),
        )
        add(
            "Vline",
            lambda instance: self.new_vline(),
        )


    def _set_button_layout(self):
        parent_layout, button_layout = get_button_layout(sizable_from = 'left')
        self.button_layout = button_layout
        self.main_layout.add_widget(parent_layout)


    def _add_button_to_layout(self, text, on_press):
        button = Button(
            text=text,
            size_hint_max_y=100
        )
        button.bind(
            on_press=on_press
        )
        self.button_layout.add_widget(button)


    def new_box(self):
        self._add_button_to_layout(
            "new Box",
            lambda instance: print(instance),
        )
    
    def new_hline(self):
        self._add_button_to_layout(
            "new Hline",
            lambda instance: print(instance),
        )

    def new_vline(self):
        self._add_button_to_layout(
            "new Vline",
            lambda instance: print(instance),
        )

if __name__ == '__main__':
    TestApp().run()