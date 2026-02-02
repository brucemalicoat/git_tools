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
from    PythonClasses.Window          import  Window
from    PythonClasses.Notebook        import  Notebook
from    PythonClasses.Label           import  Label
from    PythonClasses.Config          import  Config
from    PythonClasses.Git             import  Git
#endregion imports

class   Application():
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Application
        inherits from:                  None
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat 
        description:                    framework for GUI application
        ---------------------------------------------------------------------------------------------------------------------------
        modified:
        description:
        ---------------------------------------------------------------------------------------------------------------------------
        """
        ivar_title      : str           = "Application"
        ivar_Config     : Config        = None
        ivar_Git        : Git           = None


       # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(       self,
                                arg_title : str):

                        self.ivar_title = arg_title

                        self.w_main = Window(title=self.ivar_title)


        def     run(            self ):
                        self.w_main.mainloop()