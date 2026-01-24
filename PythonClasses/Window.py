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

        # instance variables 
        # ------------------
        ivar_framecount         :       int = 2
        ivar_tabcount           :       int = 2
        ivar_tabnames           =       ["Tab1","Tab2"]
        ivar_datatable          =       None  


        # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(   self,
                            *args,
                            **kargs):

                match( kargs.get("title")   ):
                        case      None | "":
                                title = "Window1"
                        case    _:
                                title = kargs.get("title")
                                kargs.pop("title")

                super().__init__(*args,**kargs)
                self.title(title)

                # some defaults. override after class object created if you want/need
                self.configure(background="white")
                #self.state('zoomed')
                self.geometry("1024x768+1+1")
                self.minsize(1024, 768)
                self.grid()
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(1, weight=1)

        def     StandardWindow1(        self,
                                        **kargs,
                                ):
                # -----------------------------------------------------------------------------------------------------------      
                # function:     StandardWindow1 
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  set up a "standard" 2 frame 1 datawindow window with notebook in frame 1
                # -----------------------------------------------------------------------------------------------------------     
                match( kargs.get("tabcount")   ):
                        case      0 | 1 | 2:
                                self.ivar_tabcount = kargs.get("tabcount")
                match( kargs.get("framecount")   ):
                        case      0 | 1 | 2:
                                self.ivar_framecount = kargs.get("framecount")
                match( kargs.get("tabnames")   ):
                        case      None :
                                pass
                        case      _:
                                self.ivar_tabnames = kargs.get("tabnames")

                if( self.ivar_framecount > 0 ):
                        self.frame_1 = Frame(self, bg="white")
                        self.frame_1.grid(row=0,column=0,sticky="NW")
                        self.frame_1.grid_rowconfigure(0, weight=1)
                        self.frame_1.grid_columnconfigure(0, weight=1)

                if( self.ivar_framecount > 1 ):
                        self.frame_2 = Frame(self, bg="white",width=900, height=700)
                        self.frame_2.grid(row=0,column=1,sticky="NSEW")
                        self.frame_2.grid_rowconfigure(0, weight=1)
                        self.frame_2.grid_columnconfigure(0, weight=1)

                        if( self.ivar_tabcount > 0):

                                # Tools and Filters tabs
                                self.frame_2.notebook_1 = Notebook(self.frame_2)
                                self.frame_2.notebook_1.grid(column=0,row=0,sticky='NSEW')
                                self.frame_2.notebook_1.grid_rowconfigure(0, weight=1)
                                self.frame_2.notebook_1.grid_columnconfigure(0, weight=1)

                                self.frame_2.notebook_1.frame_1 = Frame(master=self.frame_2.notebook_1, bg="lightblue")
                                self.frame_2.notebook_1.frame_1.grid(column=0,row=0,sticky='NSEW')
                                self.frame_2.notebook_1.frame_1.grid_rowconfigure(0, weight=1)
                                self.frame_2.notebook_1.frame_1.grid_columnconfigure(0, weight=1)               # self.notebook_1.tab_2 = Frame(master=self.notebook_1, bg="lightgreen")

                                if len( self.ivar_tabnames ) > 0:
                                        self.frame_2.notebook_1.add(self.frame_2.notebook_1.frame_1, text=self.ivar_tabnames[0] )
                                else:
                                        self.frame_2.notebook_1.add(self.frame_2.notebook_1.frame_1, text='Tab1')

                        if( self.ivar_tabcount > 1):

                                self.frame_2.notebook_1.frame_2 = Frame(master=self.frame_2.notebook_1, bg="lightblue")
                                self.frame_2.notebook_1.frame_2.grid(column=1,row=0,sticky='NSEW')
                                # the below code causes the pandastable to come out weird looking with too large row header and column name
                                # but you need it on the parent frame :/
                                # ---------------------------------------------------------------------------------------------------------
                                # self.frame_2.notebook_1.frame_2.grid_rowconfigure(0, weight=1)
                                # self.frame_2.notebook_1.frame_2.grid_columnconfigure(0, weight=1)               # self.notebook_1.tab_2 = Frame(master=self.notebook_1, bg="lightgreen")


                                if len( self.ivar_tabnames ) > 1:
                                        self.frame_2.notebook_1.add(self.frame_2.notebook_1.frame_2, text=self.ivar_tabnames[1])
                                else:
                                        self.frame_2.notebook_1.add(self.frame_2.notebook_1.frame_2, text='Tab2')

                                # pandastable
                                # -----------
                                self.ivar_datatable = Datawindow(       parent=self.frame_2.notebook_1.frame_2,
                                                                        dataframe=Datawindow.random_filled(75,50)
                                                                )




