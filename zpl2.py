#!/usr/bin/python3

"""Provide zpl-writing library with minimal abstraction
    
    Note: All numeric values have to be integer
    
    exemple of use:
        #recommanded to keep the values in px of the ticket for relative positionning
            height = height_mm * dpmm
            width = width_mm *dpmm

            #By using a string variable to keep everything
                zpl = Start() #to keep all the zpl in one variable, to keep the logique of using functions
                zpl += newText("mon texte",100)
                zpl += newText("mon texte",100,x=width/2,y=height/2)
                zpl += End()

            #By using a list of string
                zpl = [START]
                zpl.append(newText("mon texte",100))
                zpl += [newText("BlaBLalblalblablalbla",200)]

                #a better way would be to write everything at initialization
                zpl = [
                    START,
                    newText("mon texte",100),
                    newText("BlaBLalblalblablalbla",200,x=200,y=200),
                ]

                #and finaly

                printZPL(zpl)
                #or
                getZPL(zpl)
                

    """

START = "^XA"
END = "^XZ"


def Start():
    return START + "\n"

def End():
    return END

def Fontsize(h=15,w=15):
    "Change de fontsize for the next texts"
    return ','.join(["^CF0",str(h),str(w)])

def newBox(length,height,x=0,y=0,border=1):
    return "^FO"+str(x) + "," + str(y) + "^GB" + str(length) + "," + str(height) + "," + str(border) + "^FS"

def newVLine(length,x=0,y=0,border=1):
    return newBox(length,height=1,x=x,y=y,border=1)

def newHLine(height,x=0,y=0,border=1):
    return newBox(length=1,height=height,x=x,y=y,border=1)

def newText(text,width,x=0,y=0,align="L",max_line=1,interline=0,indent=0):
    return "^FO" + str(x) + "," + str(y) + "\n" \
        + "^FB" + str(width) + "," + str(max_line) +"," + str(interline) + "," + align + "," + str(indent) + "\n" \
        + "^FD" + text + "^FS" + "\n"

def getZPL(zpl_list):
    """Takes a list of string corresponding to many zpl code and return them as a unique code string"""
    return "".join(zpl_list)

def printZPL(zpl_list):
    """Takes a list of string corresponding to many zpl code and print them as a unique code string"""
    print("\n".join(zpl_list))