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

class   Label(tkinter.Label):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Label
        inherits from:                  tkinter.Label
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
        ivar_font = None

        # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(       self,
                                *args,
                                **kargs):

                super().__init__(*args,**kargs)
                self.setfont( "Courier New", 8, "normal" )
                self.configure( justify = "left" )
                self.configure( anchor = "nw" )
                self.configure( bg=webcolors.name_to_hex("white") )

        def     loadfile(       self,
                                arg_filename : str ):

                with open( arg_filename ,"r" ) as input_file:
                        text_data = input_file.read()

                self.config(text=text_data)

        def     setfont(        self,
                                arg_font_family : str,
                                arg_font_size   : int,
                                arg_font_style  : str
                        ):
                self.ivar_font = tkinter.font.Font( family = arg_font_family, size= arg_font_size, weight = arg_font_style )
                self.configure(font=self.ivar_font)
                
        def     set_cell_background_color(      self,
                                                color : str = "white" ):
                 # -----------------------------------------------------------------------------------------------------------      
                # function:     set_label_background_color
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  this method of setting cell background color is specific to pandastable
                # -----------------------------------------------------------------------------------------------------------      
               self.configure("bg",webcolors.name_to_hex(color))

        def     set_cell_background_color(      self,
                                                red     : int = 255,
                                                green   : int = 255,
                                                blue    : int = 255
                                        ):
                 # -----------------------------------------------------------------------------------------------------------      
                # function:     set_label_background_color
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  this method of setting cell background color is specific to pandastable
                # -----------------------------------------------------------------------------------------------------------      
                rgbtuple = (red,green,blue)
                rgbhex = str(webcolors.rgb_to_hex(rgbtuple))
                self.configure(bg=rgbhex)