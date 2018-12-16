#!/usr/bin/python3
from zpl import *
from tkinter import * 


#Define how to draw ZPL-Objects
def drawZPL(self,canvas):
    canvas.create_rectangle(0,0,self.width * self.dpmm,self.height * self.dpmm,outline='green')
    for child in self._childs:
        if hasattr(child,'draw'):
            child.draw(canvas)

def drawHLine(self,canvas):
    canvas.create_line(self.x,self.y,self.x + self.length,self.y,width=self.border,activefill='red')

def drawVLine(self,canvas):
    canvas.create_line(self.x,self.y,self.x, self.length + self.y,width=self.border,activefill='red')

def drawBox(self,canvas):
    canvas.create_rectangle(self.x, self.y, self.x + self.length, self.y + self.height,width=self.border,activeoutline='red')

ZPL.draw = drawZPL
HLine.draw = drawHLine
VLine.draw = drawVLine
Box.draw = drawBox


#Define the Edit Menu
def defaultLabelFrame(parent):
    l = LabelFrame(parent, text="Empty")
    parent.add(l)
    Label(l, text="the selected object doesn't have editor").pack()
    return l

def editZPL(self,parent):
    l = LabelFrame(parent, text="ZPL")
    parent.add(l)
    Label(l, text="Editer le zpl").pack()
    return l

ZPL.edit = editZPL




class App():
    def __init__(self):
        self.win = Tk(className=" ZPL Editor ")
        self.zpl = ZPL(78,49,6)
       
        #main panel to keep every
        self.panel = PanedWindow(self.win, orient=HORIZONTAL)
        self.panel.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

        #Define the 3 most importants parts: buttons, canvas, editor
        self.actions = PanedWindow(self.panel, orient=VERTICAL)
        self.panel.add(self.actions)

        self.canvas = Canvas(self.panel,width=400,height=400, background='yellow')
        self.panel.add(self.canvas)

        self.editing = PanedWindow(self.panel, orient=HORIZONTAL)
        self.panel.add(self.editing)
        self.objects = Listbox(self.editing)
        self.editing.add(self.objects)
        self.objects.bind('<<ListboxSelect>>',lambda evt: self.edit_active_object(evt))
        self.objects.insert(END,"ZPL")
        self.editor = PanedWindow(self.editing, orient=VERTICAL)
        self.panel.add(self.editing)
        self.labelframe = self.zpl.edit(self.editing)

        # scrollbar = Scrollbar(self.panel)
        # scrollbar.pack(side=RIGHT, fill=Y)
        # self.objects = Listbox(self.panel, yscrollcommand=scrollbar.set)
        # self.panel.add(self.objects)
        # scrollbar.config(command=self.objects.yview)
        #===========================================================================================
        #Create Buttons
        self.actions.add(Button(self.actions,text='new Horizontal Line', command=lambda: self.createHLine()))
        self.actions.add(Button(self.actions,text='new Vertical Line', command=lambda: self.createVLine()))
        self.actions.add(Button(self.actions,text='new Box', command=lambda: self.createBox()))
        self.actions.add(Label(self.actions))

    def edit_active_object(self,evt):
        self.labelframe.destroy()
        del self.labelframe
        w = evt.widget
        index = int(w.curselection()[0])
        if index == 0:
            # print("show zpl editor")
            self.labelframe = self.zpl.edit(self.editing)
        else:
            curent_object = self.zpl._childs[index-1]
            # print("show object")
            if hasattr(curent_object,'edit'):
                self.labelframe = curent_object.edit(self.editing)
            else:
                self.labelframe = defaultLabelFrame(self.editing)

    def createHLine(self):
        tmp = self.zpl.HLine(length=200,x=50,y=50,border=2)
        app.objects.insert(END,"HLine")
        # self.editor.add(Button(self.editor,text='HLine', command=lambda: print('test')))
        self.zpl.draw(self.canvas)
    def createVLine(self):
        self.zpl.VLine(length=200,x=50,y=50,border=2)
        app.objects.insert(END,"VLine")
        self.zpl.draw(self.canvas)
    def createBox(self):
        self.zpl.Box(length=100,height=100,x=50,y=50,border=2)
        app.objects.insert(END,"Box")
        self.zpl.draw(self.canvas)
    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()




# txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")