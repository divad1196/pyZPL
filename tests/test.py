from pyZPL import ZPL 

zpl = ZPL(78,49,6)
text = zpl.Text(300,x=100,fontsize=20)
ligne1 = text.newLine("salut")
text.fontsize = 12
ligne = text.newLine("ca va?")
text.fontsize = 40
ligne1 = text.newLine("Test")