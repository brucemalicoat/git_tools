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

class   Notebook(tkinter.ttk.Notebook):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Notebook
        inherits from:                  tkinter.ttk.Notebook
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat - no Jira ticket #
        description:                    extend the functionality of tkinter.ttk.Notebook
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

