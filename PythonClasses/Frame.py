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
#endregion imports

class   Frame(tkinter.Frame):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Frame
        inherits from:                  tkinter.frame
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat - no Jira ticket #
        description:                    extend the functionality of tkinter frame class to provide GUI functionality for xlsx, 
                                        ML projects, and git tools
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

