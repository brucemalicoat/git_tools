#region imports
import tkinter
import tkinter.ttk
import sys
import pandastable
import pandas
import numpy
import tksheet
from   decimal import Decimal
import decimal
import webcolors
import openpyxl.utils
sys.path.append('../..')
from    PythonClasses.Datawindow      import  Datawindow
from    PythonClasses.Frame           import  Frame
from    PythonClasses.Notebook        import  Notebook
#endregion imports

class   Window(tkinter.Tk):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Window
        inherits from:                  tkinter.Tk
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat 
        description:                    extend the functionality of tkinter.Tk
        ---------------------------------------------------------------------------------------------------------------------------
        modified:
        description:
        ---------------------------------------------------------------------------------------------------------------------------
        """

        # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(   self,
                            *args,
                            **kargs):

                super().__init__(*args,**kargs)

                # some defaults. override after class object created if you want/need
                self.configure(background="white")
                self.state('zoomed')
                self.minsize(800, 600)
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(0, weight=1)

        def     StandardWindow1(    self,
                                ):
                # -----------------------------------------------------------------------------------------------------------      
                # function:     StandardWindow1 
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  set up a "standard" 2 frame 1 datawindow window with notebook in frame 1
                # -----------------------------------------------------------------------------------------------------------      
                self.x=1
                self.frame_1 = Frame(self, bg="white")
                self.frame_1.grid(row=0,column=0,sticky="NSEW")
                self.frame_1.grid_rowconfigure(0, weight=1)
                self.frame_1.grid_columnconfigure(0, weight=1)

                # self.frame_2 = Frame(master=self, bg="white")
                # self.frame_2.grid(row=0,column=1,sticky="NSEW")

                # Tools and Filters tabs
                self.frame_1.notebook_1 = Notebook(self.frame_1)
                self.frame_1.notebook_1.grid(column=0,row=0,sticky='NSEW')
                self.frame_1.notebook_1.grid_rowconfigure(0, weight=1)
                self.frame_1.notebook_1.grid_columnconfigure(0, weight=1)

                self.frame_1.notebook_1.frame_1 = Frame(master=self.frame_1.notebook_1, bg="lightblue")
                self.frame_1.notebook_1.frame_1.grid(column=0,row=0,sticky='NSEW')
                self.frame_1.notebook_1.frame_1.grid_rowconfigure(0, weight=1)
                self.frame_1.notebook_1.frame_1.grid_columnconfigure(0, weight=1)               # self.notebook_1.tab_2 = Frame(master=self.notebook_1, bg="lightgreen")

                self.frame_1.notebook_1.add(self.frame_1.notebook_1.frame_1, text='Tab 1')

                self.frame_1.notebook_1.frame_2 = Frame(master=self.frame_1.notebook_1, bg="lightblue")
                self.frame_1.notebook_1.frame_2.grid(column=1,row=0,sticky='NSEW')
                self.frame_1.notebook_1.frame_2.grid_rowconfigure(0, weight=1)
                self.frame_1.notebook_1.frame_2.grid_columnconfigure(0, weight=1)               # self.notebook_1.tab_2 = Frame(master=self.notebook_1, bg="lightgreen")

                self.frame_1.notebook_1.add(self.frame_1.notebook_1.frame_2, text='Tab 2')

                # self.notebook_1.radiobutton_var = tkinter.StringVar(value="None")
                # for tool in ["1", "2","3","4"]:
                #                 tkinter.Radiobutton(
                #                         self.notebook_1.tab_1,
                #                         text=tool,
                #                         variable=self.notebook_1.radiobutton_var,
                #                         value=tool,
                #                         bg="lightblue",
                #                 ).pack(anchor="w", padx=1, pady=1,side="top",expand=True)

                self.frame_1.notebook_1.frame_1.image_git2   = tkinter.PhotoImage(file="git.png")#.zoom(8,8).subsample(2,2)
                self.frame_1.notebook_1.frame_1.image_label  = tkinter.Label(self.frame_1.notebook_1.frame_1, image=self.frame_1.notebook_1.frame_1.image_git2, anchor="n")
                self.frame_1.notebook_1.frame_1.image_label.grid(column=0,row=0,sticky='NSEW')
                self.frame_1.notebook_1.frame_1.image_label.grid_rowconfigure(0, weight=1)
                self.frame_1.notebook_1.frame_1.image_label.grid_columnconfigure(0, weight=1)



                # pandastable
                # -----------
                self.frame_1.notebook_1.frame_2.dw_1 = Datawindow(      parent=self.frame_1.notebook_1.frame_2,
                                                                        dataframe=Datawindow.random_filled(75,50)
                                                                )
                self.frame_1.notebook_1.frame_2.dw_1.rowcolors.iloc[3,7]=webcolors.name_to_hex('red')
