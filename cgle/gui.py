
def run_file():
   global test_file
   filename=test_file.get()
   if filename:
      execfile(root_folder+"/"+filename,globals())
   else:
      execfile(root_folder+"/test.py",globals())
def open_debug():
   global debug_window,master
   global test_file,test_code
   debug_window = Toplevel(master)
   debug_window.title("Debug Window")
   new_frame = Frame(debug_window)
   ROW = 0
   COL = 0

   #Button(debug_window, text='Run test.py', command=run_file, font = "Times 16 bold").grid(row=ROW, column = COL,sticky=W, pady=2)
   #ROW+=1



###########THE GUI STARTS HERE#####################

if __name__ == "__main__":

   master = Tk()
   master.title("Monte Carlo Small Angle Scattering ({0})".format(version))
   root = Frame(master)



   ROW = 0
   COL = 0
   Label(master, text = "Model Type", font = "Times 16 bold").grid(row = ROW, column = COL, sticky = W)
   ROW+=1
   tick('Qz',"Small Angle Approx.", master, ROW, COL)
   COL+=1
   tick("symmetric", "Radial Symmetry", master,ROW,COL)
   COL-=1



   ROW+=1
   
   Label(master, text = "Monte Carlo Model: ").grid(row = ROW, column = COL, sticky = W)
   g.dictionary_in['shape'] = StringVar(master)
   g.dictionary_in['shape'].set(g.MC_num_and_name[g.dictionary['shape']][0])
   OptionMenu(master, g.dictionary_in['shape'], *g.MC_num_and_name[:,0]).grid(row = ROW, column = COL+1)

   
   ROW+=1
   Label(master, text = "Analytic Model: ").grid(row = ROW, column = COL, sticky = W)
   g.dictionary_in['analytic'] = StringVar(master)
   g.dictionary_in['analytic'].set(Analytic_options[g.dictionary['analytic']][0])
   OptionMenu(master, g.dictionary_in['analytic'], *Analytic_options[:,0]).grid(row = ROW, column = COL+1)


   ROW+=1
   Label(master, text = "Model Parameters", font = "Times 16 bold").grid(row = ROW, column = COL, sticky = W)
   COL+=1
   parameter_help = Button(master, text='Update Parameters', font = "Times 12 bold")
   parameter_help.bind("<Button-1>", rename_parameters)
   parameter_help.grid(row=ROW, column = COL, pady=2)   
   COL-=1
   ROW+=1
   parameter_start_row=ROW
   enter_num('radius_1', "Radius 1 (nm)", master, ROW, COL)
   ROW+=1
   enter_num('radius_2', "Radius 2 (nm)", master, ROW, COL)
   ROW+=1
   enter_num('z_dim', "Length (nm)", master, ROW, COL)
   ROW+=1
   enter_num('rho_1', 'Rho 1', master, ROW, COL)
   ROW+=1
   enter_num('rho_2', 'Rho 2', master, ROW, COL)
   ROW+=1

   enter_num('num', 'Number', master, ROW, COL)
   ROW+=1
   enter_num('length_2', 'Length 2 (nm)', master, ROW, COL)
   ROW+=1
   
   Label(master, text = "Rotation Parameters", font = "Times 16 bold").grid(row = ROW, column = COL, sticky = W)
   ROW+=1
   MODES_angle = [('Degrees', '1'),('Radians','0'),]
   radio('degrees', MODES_angle, master, ROW, COL)
   ROW+=1
   enter_num('x_theta', 'x rotation', master, ROW, COL)
   ROW+=1
   enter_num('y_theta', 'y rotation', master, ROW, COL)
   ROW+=1
   enter_num('z_theta', 'z rotation', master, ROW, COL)
   

   COL+=2
   ROW=0
   Label(master, text="Output Options", font = "Times 16 bold").grid(row= ROW, column=COL, sticky = W)
   COL+=1
   tick('save_img', 'Save Images?', master, ROW, COL)
   ROW+=1
   COL-=1

   enter_str('title', 'Plot Title', master, ROW, COL)
   ROW+=1
   enter_str('save_name', 'File Name', master, ROW, COL)
   ROW+=1
   enter_str('subfolder', 'Subfolder', master, ROW, COL)
   ROW+=1

   HEIGHT = 3
   WIDTH = 50
   enter_text("comments", "Description (optional):", WIDTH, HEIGHT, ROW, COL, 2)
   ROW+=3
   
   enter_num('num_plots', "Number of Plots to Average", master, ROW, COL)
   ROW+=1


   enter_num('pixels', "Number of Pixels (x y)", master, ROW, COL)
   ROW+=1
   enter_num('ave_dist', "Approximate Number of Points", master, ROW, COL)
   ROW+=1

   tick('bound', "Upper / Lower Bounds?", master, ROW, COL)

   ROW+=1
   enter_num('minimum', "Minimum (ie. 3e-7)", master, ROW, COL)
   ROW+=1
   enter_num('maximum', "Maximum", master, ROW, COL)
   ROW+=1
   

   COL+=2
   ROW=0
   
   Button(master, text='Real Space', command=plot_points, font = "Times 16 bold").grid(row=ROW, column = COL, sticky=W, pady=2)
   ROW+=1
   

   int_button = Button(master, text="Calculate Intensity", command = calc_int, font = "Times 16 bold")
   int_button.grid(row=ROW, column = COL,sticky=W, pady=2)
   ROW+=1
   
   Button(master, text='Replot Intensity', command=view_intensity, font = "Times 16 bold").grid(row=ROW, column = COL, sticky=W, pady=2)
   

   ROW+=2
   Label(master, text="Pop-Up Windows:", font = "Times 16 bold").grid(row= ROW, column=COL, sticky = W)
   ROW+=1

   Button(master, text='Ring Options', command=ring_options, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)   
   ROW+=1

   Button(master,text='Inter-Particle Scattering', command=interparticle_options, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)

   ROW+=1
   
   Button(master, text='Detector Options', command=detector_parameters, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)   
   ROW+=1
   
   Button(master, text='Sequence Options', command=sequence_parameters, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)   
   ROW+=1


   Button(master, text='Fitting Options', command=select_fit_parameters, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)
   ROW+=1

   Button(master, text='Output Options', command=output_options, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)   
   ROW+=1


   if g.debug:
      ROW+=1
      Button(master, text='Debug Window', command=open_debug, font = "Times 14 bold").grid(row=ROW, column = COL, sticky=W, pady=2)   
      ROW+=1


   rename_parameters(0)
   root.mainloop()
   




