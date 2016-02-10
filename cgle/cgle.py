#!/usr/bin/python
from Tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import os,pickle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
#from PIL import Image, ImageTk

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
    g.solve['tpixels']=float(g.solve['tpixels'])-1
    if not os.path.exists(g.solve['currentfolder']+'/'+g.solve['subfolder']):#making the subfolder, if it doesn't exist
        os.makedirs(g.solve['currentfolder']+'/'+g.solve['subfolder'])
    if g.solve['1d2d']=='0':
        makegif()
    elif g.solve['1d2d']=='1':
        make1D()


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

    #photo = PhotoImage(file="equation.png")
    #label=Label(image=photo)
    #label.image = photo
    #label.pack()
    photo = PhotoImage(file = 'equation.png')
    label1 = Label(root, image=photo)
    label1.image = photo
    label1.grid(row = ROW, column = COL, columnspan = 4)
    
    ROW+=1

    modes_dim = [('2D .GIF','0'),('1D .png','1')]
    guiradio('1d2d', modes_dim, root, ROW, COL)
    COL+=2
    modes_absreal = [('Absolute Value','0'),('Real Part','1')]
    guiradio('absreal', modes_absreal, root, ROW, COL)
    ROW+=1
    COL-=2
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
    ROW+=1
    guinum('tpixels', 'Approx. T Pixels', root, ROW, COL)
    COL+=2
    guinum('xpixels','Approx. X Pixels',root,ROW,COL)
    ROW+=1
    COL-=2
    modes_trialfunction = [('Noise','0'),('Sech-Pulse','1'),('Generalised Gaussian','2')]
    guiradio('trialfunction', modes_trialfunction, root, ROW, COL)
    ROW+=1
    guinum('par1', 'Amplitude', root, ROW, COL)
    COL+=2
    guinum('par2', 'Width', root, ROW, COL)
    COL-=2
    ROW+=1
    guinum('par3', 'Maxima Position', root, ROW, COL)
    COL+=2
    guinum('par4', 'Phase Shift', root, ROW, COL)
    COL-=2
    ROW+=1
    guinum('par5', 'Linear Phase Coefficient', root, ROW, COL)
    COL+=2
    guinum('par6', 'Chirp Parameter', root, ROW, COL)
    COL-=2
    ROW+=1
    guinum('par7', 'Super Gaussian Width Scaling', root, ROW, COL)


    
    ROW+=2
    Button(root, text='Go!', command=getgui, font = "Times 16 bold").grid(row=ROW, column = COL, pady=2)
    ROW+=1




    root.mainloop()




