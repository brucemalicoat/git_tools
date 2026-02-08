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
from    PythonClasses.Label           import  Label
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
                self.geometry("800x600+1+1")
                self.minsize(800, 600)
                self.grid()
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(1, weight=1)

                # instance variables 
                # ------------------
                self.ivar_framecount            :       int                = 1
                self.ivar_framelist             :       list[Frame]        = []   


        def     StandardWindow1(        self,
                                        **kargs,
                                ):
                # -----------------------------------------------------------------------------------------------------------      
                # function:     StandardWindow1 
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  set up a "standard" 2 frame 1 tab window with notebook in frame[1]
                # -----------------------------------------------------------------------------------------------------------     
                self.ivar_framecount = 2
                self.ivar_tabcount           :       int                = len(kargs.get("tabnames"))
                self.ivar_tabnames           :       list[str]          = kargs.get("tabnames")
                self.ivar_datatable          :       list[Datawindow]   = None  
                self.ivar_output_label                                  = None
                self.ivar_config_label       :       list[str]          = None

                # frame one is for buttons, frame 2 is for the notebook with xx tabs to show / edit data
                # --------------------------------------------------------------------------------------
                self.ivar_framelist.append( Frame(self, bg="white",padx=0,pady=0) )
                self.ivar_framelist[0].grid(row=0,column=0,sticky="NW")
                self.ivar_framelist[0].grid_rowconfigure(0, weight=1)
                self.ivar_framelist[0].grid_columnconfigure(0, weight=1)


                if( self.ivar_framecount > 1 ):

                        # the first tab has a big info only label, and a bunch of status labels at the bottom, not a datawindow.
                        # tabs 2 through xx will have a datawindow each
                        # ------------------------------------------------------------------------------------------------------
                        self.ivar_framelist.append( Frame(self, bg="white",width=900, height=700,padx=0,pady=0) )
                        self.ivar_framelist[1].grid(row=0,column=1,sticky="NSEW")
                        self.ivar_framelist[1].grid_rowconfigure(0, weight=1)
                        self.ivar_framelist[1].grid_columnconfigure(0, weight=1)

                        if( self.ivar_tabcount > 0):


                                # Tools and Filters tabs
                                self.ivar_framelist[1].ivar_notebooklist : list[ Notebook ] = []
                                self.ivar_framelist[1].ivar_notebooklist.append( Notebook(self.ivar_framelist[1]) )
                                self.ivar_framelist[1].ivar_notebooklist[0].grid(column=0,row=0,sticky='NSEW')
                                self.ivar_framelist[1].ivar_notebooklist[0].grid_rowconfigure(0, weight=1)
                                self.ivar_framelist[1].ivar_notebooklist[0].grid_columnconfigure(0, weight=1)

                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist : list[Frame] = []
                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist.append( Frame(master=self.ivar_framelist[1].ivar_notebooklist[0], bg="Light Grey",padx=4,pady=4) )
                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[0].grid(column=0,row=0,sticky='NSEW')
                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[0].grid_rowconfigure(0, weight=1)
                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[0].grid_columnconfigure(0, weight=1)               # self.notebook_1.tab_2 = Frame(master=self.notebook_1, bg="lightgreen")

                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_notebooks : list[Notebook] = []
                                self.ivar_framelist[1].ivar_notebooklist[0].ivar_notebooks.append( self.ivar_framelist[1].ivar_notebooklist[0].add(self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[0], text=self.ivar_tabnames[0] ) )

                                self.ivar_output_label = Label( self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[0] ,padx=0,pady=0,text="status:")
                                self.ivar_output_label.grid(row=0,column=0,sticky="NSEW")

                                self.ivar_config_label          :       list[ Label ] = []
                                for idx in range(10) :
                                        self.ivar_config_label.append( Label( self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[0] ,padx=0,pady=0, text=str(idx)+':') )
                                        self.ivar_config_label[idx].grid(row=idx+1,column=0,sticky="NSEW")
                                        self.ivar_config_label[idx].set_background_color( red=200,green=200,blue=200)

                        if( self.ivar_tabcount > 1):


                                for lvar_index in range( 1, self.ivar_tabcount ):

                                        self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist.append( Frame(master=self.ivar_framelist[1].ivar_notebooklist[0], bg="Light Grey",padx=4,pady=4) )
                                        self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[lvar_index].grid(column=1,row=0,sticky='NSEW')
                                        # the below code causes the pandastable to come out weird looking with too large row header and column name
                                        # but you need it on the parent frame :/
                                        # ---------------------------------------------------------------------------------------------------------
                                        # self.ivar_framelist[1].notebook_1.ivar_framelist[1].grid_rowconfigure(0, weight=1)
                                        # self.ivar_framelist[1].notebook_1.ivar_framelist[1].grid_columnconfigure(0, weight=1)               # self.notebook_1.tab_2 = Frame(master=self.notebook_1, bg="lightgreen")


                                        self.ivar_framelist[1].ivar_notebooklist[0].add(self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[lvar_index], text=self.ivar_tabnames[ lvar_index ]) 
                                        self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[lvar_index].ivar_datatable = Datawindow(       parent=self.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[lvar_index],
                                                                                                                                        dataframe=pandas.DataFrame(),
                                                                                                                                        padx=0,pady=0
                                                                                                                                )




