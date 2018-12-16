#!/usr/bin/python3
from zpl import *
from tkinter import *
from pathlib import Path


#Define how to draw ZPL-Objects
def drawZPL(self,canvas):
    canvas.delete("all")
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
#------------------------
#usefull functions
def listboxRename(app,index,text):
    app.objects.delete(index)
    app.objects.insert(index,text)
def editObj(obj,app,attr,value,spinbox):
    print(value)
    tmp = value
    if tmp < 0:
        tmp = 0
        spinbox.delete(0,END)
        spinbox.insert(0,str(0))
    setattr(obj,attr,tmp)
    app.draw()

def numBox(obj,frame,app,attr):
    parent = frame
    canvas = app.canvas
    if hasattr(obj,attr):
        label = Label(parent,text=attr)
        label.pack()
        # label.grid(row=parent.grid_size()[0],column=0)
        tmp = Spinbox(parent, from_=0,to=1000,wrap=True,
                command=lambda:editObj(obj,app,attr,int(tmp.get()),tmp))
        tmp.delete(0,END)
        tmp.insert(0,str(getattr(obj,attr)))
        tmp.bind("<Return>",lambda event: editObj(obj,app,attr,int(event.widget.get()),tmp))
        # tmp.grid(row=parent.grid_size()[0],column=1)
        tmp.pack()
        return tmp
    else:
        print("attribut " + str(attr) + " does not exist")

def labelFrame(app,index):
    text = app.objects.get(index)
    parent = app.editor
    label = Entry(parent)
    label.delete(0,END)
    label.insert(0,text)
    l = LabelFrame(parent, labelwidget=label)
    label.bind("<Return>",lambda event: listboxRename(app,index,event.widget.get()))
    parent.add(l)
    return l


def defaultLabelFrame(app):
    parent = app.editor
    l = LabelFrame(parent, text="Empty")
    parent.add(l)
    Label(l, text="the selected object doesn't have editor").pack()
    return l

#-------------------------------------------------------------------------
#objects editors

def editZPL(self,app):
    index = 0
    parent = app.editor
    l = labelFrame(app,index)
    parent.add(l)
    Label(l, text="Editer le zpl").pack()

    width = numBox(self,l,app,"width")
    height = numBox(self,l,app,"height")
    dpmm = numBox(self,l,app,"dpmm")
    
    return l

ZPL.edit = editZPL

def editHline(self,app,index):
    parent = app.editor
    l = labelFrame(app,index)
    parent.add(l)
    Label(l, text="Editer la HLine").pack()

    length = numBox(self,l,app,"length")
    x = numBox(self,l,app,"x")
    y = numBox(self,l,app,"y")
    border = numBox(self,l,app,"border")
    
    return l

HLine.edit = editHline

def editVline(self,app,index):
    parent = app.editor
    l = labelFrame(app,index)
    parent.add(l)
    Label(l, text="Editer la VLine").pack()

    length = numBox(self,l,app,"length")
    x = numBox(self,l,app,"x")
    y = numBox(self,l,app,"y")
    border = numBox(self,l,app,"border")
    
    return l

VLine.edit = editVline

def editBox(self,app,index):
    parent = app.editor
    l = labelFrame(app,index)
    parent.add(l)
    Label(l, text="Editer la Box").pack()

    length = numBox(self,l,app,"length")
    height = numBox(self,l,app,"height")
    x = numBox(self,l,app,"x")
    y = numBox(self,l,app,"y")
    border = numBox(self,l,app,"border")
    
    return l

Box.edit = editBox

class App():
    def __init__(self):
        self.win = Tk(className=" ZPL Editor ")
        self.zpl = ZPL(78,49,6)
        self.active_index = 0

        #Menus
        self.main_menu = Menu(self.win)
        self.menu1 = Menu(self.main_menu, tearoff=0)
        self.menu1.add_command(label="Print", command=lambda: self.printZPL())
        self.main_menu.add_cascade(label="Fichier", menu=self.menu1)
       
        self.win.config(menu=self.main_menu)
        #main panel to keep every
        self.panel = PanedWindow(self.win, orient=HORIZONTAL)
        self.panel.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

        #Define the 3 most importants parts: buttons, canvas, editor
        self.actions = PanedWindow(self.panel, orient=VERTICAL)
        self.panel.add(self.actions)

        self.canvas = Canvas(self.panel,width=400,height=400, background='yellow')
        self.panel.add(self.canvas)

        self.editor = PanedWindow(self.panel, orient=HORIZONTAL)
        self.panel.add(self.editor)
        self.objects = Listbox(self.editor)
        self.editor.add(self.objects)
        self.objects.bind('<<ListboxSelect>>',lambda evt: app.edit_active_object(evt))
        self.objects.insert(END,"ZPL")
        self.panel.add(self.editor)
        self.labelframe = self.zpl.edit(self)
        #===========================================================================================
        #Create Buttons
        self.actions.add(Button(self.actions,text='new Horizontal Line', command=lambda: self.createHLine()))
        self.actions.add(Button(self.actions,text='new Vertical Line', command=lambda: self.createVLine()))
        self.actions.add(Button(self.actions,text='new Box', command=lambda: self.createBox()))
        self.actions.add(Label(self.actions))

    def edit_active_object(self,evt):
        w = evt.widget
        select = w.curselection()
        index = int(select[0]) if select else self.active_index
        if  index != self.active_index:
            self.labelframe.destroy()
            self.active_index = index
            if index == 0:
                self.labelframe = self.zpl.edit(self)
            else:
                curent_object = self.zpl._childs[index-1]
                if hasattr(curent_object,'edit'):
                    self.labelframe = curent_object.edit(self,index)
                else:
                    self.labelframe = defaultLabelFrame(self)

    def createHLine(self):
        tmp = self.zpl.HLine(length=200,x=50,y=50,border=2)
        app.objects.insert(END,"HLine")
        # Button(self.win,text='HLine', command=lambda: print('test')))
        self.zpl.draw(self.canvas)
    def createVLine(self):
        self.zpl.VLine(length=200,x=50,y=50,border=2)
        app.objects.insert(END,"VLine")
        self.zpl.draw(self.canvas)
    def createBox(self):
        self.zpl.Box(length=100,height=100,x=50,y=50,border=2)
        app.objects.insert(END,"Box")
        self.zpl.draw(self.canvas)
    def printZPL(self):
        filename = self.objects.get(0) + ".zpl"
        with open(str(Path.home()) + "/" + filename, 'x') as f:
            f.write(str(self.zpl))

    def draw(self):
        self.zpl.draw(self.canvas)
    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    app = App()
    app.draw()
    app.run()




# txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")