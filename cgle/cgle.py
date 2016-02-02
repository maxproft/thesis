#!/usr/bin/python
from Tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import os,pickle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


import glob as g
currentfolder = os.getcwd()


try:
    d = pickle.load(open(currentfolder+"/defaults", 'rb'))
    for x in g.dic:
      if x not in d: 
         d[x]=g.dic[x]
    d['currentfolder']=currentfolder
    g.dic = d
except:
    print("Couldn't Load Variables.")
    with open(currentfolder+"/defaults", 'wb') as f:
       pickle.dump(g.dic, f)
    g.dic['currentfolder']=currentfolder

g.gui = {x:g.dic[x] for x in g.dic}#This is for gui inputs
g.solve = {x:g.dic[x] for x in g.dic}#This includes everything, such as A=a1+a2*1j


execfile(currentfolder+"/solve.py",globals())


def getgui():
    for x in g.dic:
        try:
            g.dic[x] = g.gui[x].get()
        except:
            None
    with open(currentfolder+"/defaults", 'wb') as f:
       pickle.dump(g.dic, f)
    g.solve = g.dic
    g.solve['A']=float(g.dic['a1'])+1j*float(g.dic['a2'])
    g.solve['B']=float(g.dic['b1'])+1j*float(g.dic['b2'])
    g.solve['C']=float(g.dic['c1'])+1j*float(g.dic['c2'])
    g.solve['D']=float(g.dic['d1'])+1j*float(g.dic['d2'])
    if not os.path.exists(g.solve['currentfolder']+'/'+g.solve['subfolder']):#making the subfolder, if it doesn't exist
        os.makedirs(g.solve['currentfolder']+'/'+g.solve['subfolder'])
    makegif()


#GUI Input Functions
def guinum(varname, label, window, ROW, COL):
    Label(window, text=label).grid(row= ROW, column=COL, columnspan=1, sticky = E)
    temp = StringVar()
    g.gui[varname] = Entry(window, textvariable = temp)
    temp.set(g.dic[varname])
    g.gui[varname].grid(row= ROW, column = COL+1)

def guistr(varname, label, window, ROW, COL):
    Label(window, text=label).grid(row= ROW, column=COL, sticky = E)
    g.gui[varname] = Entry(window)
    g.gui[varname].insert(0, g.dic[varname])
    g.gui[varname].grid(row= ROW, column = COL + 1)

def guiradio(varname, MODES, window, ROW, COL):
   g.gui[varname] = StringVar()
   g.gui[varname].set(g.dic[varname])
   for name, mode in MODES:
      g.gui[varname+mode] = Radiobutton(window, text=name, variable=g.gui[varname], value=mode)
      g.gui[varname+mode].grid(row=ROW, column = COL, sticky = W)
      COL+=1
#MODE should be entered like: [('2D .GIF','0'),('1D .png','1')]


#The GUI
if __name__ == "__main__":

    root = Tk()
    root.title("Complex Ginsberg-Landau Equation")


    ROW=0
    COL=0
    modes_dim = [('2D .GIF','0'),('1D .png','1')]
    guiradio('1d2d', modes_dim, root, ROW, COL)
    ROW+=1
    guinum('a1',"A=",root,ROW,COL)
    COL+=2
    guinum('a2',"+i",root,ROW,COL)
    COL-=2
    ROW+=1
    guinum('b1',"B=",root,ROW,COL)
    COL+=2
    guinum('b2',"+i",root,ROW,COL)
    COL-=2
    ROW+=1
    guinum('c1',"C=",root,ROW,COL)
    COL+=2
    guinum('c2',"+i",root,ROW,COL)
    COL-=2
    ROW+=1
    guinum('d1',"D=",root,ROW,COL)
    COL+=2
    guinum('d2',"+i",root,ROW,COL)
    COL-=2
    ROW+=1
    guinum('ttotal','Total Time',root,ROW,COL)
    COL+=2
    guinum('tstep','Time Step Size',root,ROW,COL)
    COL-=2
    ROW+=1
    guinum('xtotal','X Range',root,ROW,COL)
    COL+=2
    guinum('xstep','X Resolution',root,ROW,COL)
    COL-=2
    ROW+=1
    guistr('subfolder', 'Subfolder', root, ROW, COL)
    COL+=2
    guinum('giflen', 'Num Frames in .GIF', root, ROW, COL)
    COL-=2
    ROW+=1
    modes_absreal = [('Absolute Value','0'),('Real Part','1')]
    guiradio('absreal', modes_absreal, root, ROW, COL)




    
    ROW+=2
    Button(root, text='Button', command=getgui, font = "Times 16 bold").grid(row=ROW, column = COL, sticky=W, pady=2)
    ROW+=1
    
    root.mainloop()














