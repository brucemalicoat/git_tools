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

class   Datawindow(pandastable.Table):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Datawindow
        inherits from:                  pandastable.Table
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat 
        description:                    extend the functionality of pandastable.Table to provide GUI functionality for xlsx, 
                                        ML projects, and git tools. We are also going to include a lot of static functions in here
                                        related to working with dataframes, table data, importing/exporting, xlsx, etc.
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

                arg_dataframe = kargs.get("dataframe")
                if( kargs.get("fgcolor")                 == None): kargs["fgcolor"]               = "black"
                if( kargs.get("bgcolor")                 == None): kargs["bgcolor"]               = "white"
                if( kargs.get("showtoolbar")             == None): kargs["showtoolbar"]           = True
                if( kargs.get("showstatusbar")           == None): kargs["showstatusbar"]         = True
                if( kargs.get("enable_menus")            == None): kargs["enable_menus"]          = True

                super().__init__(*args,**kargs)

                # df is the variable pandastables uses to store its datastore
                # -----------------------------------------------------------
                self.model.df = arg_dataframe

                # assume we are in a frame, and the frame is dedicated to this Table
                # ------------------------------------------------------------------
                self.grid(column=0,row=0,sticky='NSEW')
                self.grid_rowconfigure(0, weight=1)
                self.grid_columnconfigure(0, weight=1)
                self.redraw()
                self.show()

        def     set_cell_background_color( self, x, y, color : str = "white" ):
                 # -----------------------------------------------------------------------------------------------------------      
                # function:     set_cell_background_color
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  this method of setting cell background color is specific to pandastable
                # -----------------------------------------------------------------------------------------------------------      
                # print( str(self.rowcolors.shape[0]) + " x " + str(self.rowcolors.shape[1]) )
                # print( 'set x=' + str(x) + ',  y=' + str(y) + ' to ' + color )
                self.rowcolors.iloc[y,x]=webcolors.name_to_hex(color)

        def     setDF( self, arg_new_dataframe : pandas.DataFrame ):
                 # -----------------------------------------------------------------------------------------------------------      
                # function:     setDF
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  update the data in this datawindow
                # -----------------------------------------------------------------------------------------------------------      
                self.model.df = arg_new_dataframe


                # initialize the row colors for all rows to force pandastable to populate/use the rowcolors dataframe, which
                # you can use subsequent to class instantiation to set the bg color for any cell via iloc
                # ----------------------------------------------------------------------------------------------------------
                self.redrawDF()

        def     redrawDF( self ):
                 # -----------------------------------------------------------------------------------------------------------      
                # function:     redrawDF
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  update the data in this datawindow, including row color array
                # -----------------------------------------------------------------------------------------------------------      
                
                # initialize the row colors for all rows to force pandastable to populate/use the rowcolors dataframe, which
                # you can use subsequent to class instantiation to set the bg color for any cell via iloc
                # ----------------------------------------------------------------------------------------------------------
                if      ( self.model.df.shape[0] != self.rowcolors.shape[0] ) or \
                        ( self.model.df.shape[1] != self.rowcolors.shape[1] ) :

                                
                        self.rowcolors = self.model.df
                        self.rowcolors=self.rowcolors.astype('object')

                        list_of_rows = []
                        for index in range(self.model.df.shape[0]):
                                list_of_rows.append(index)

                        self.setRowColors(list_of_rows,webcolors.name_to_hex('white'),'all')
                        # print(self.rowcolors)

                self.update()
                self.redraw()
                self.autoResizeColumns()

        @staticmethod
        def     round(              arg_dataframe:pandas.DataFrame,
                                    arg_precision:int=2)->pandas.DataFrame:
                # -----------------------------------------------------------------------------------------------------------      
                # function:     round (STATIC)
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  because this class is sort of geared around using Decimal instead of float, and you can't
                #               just use df.round() to affect Decimal cells, this function will apply arg_precision
                #               level of rounding to every cell that is Decimal type.
                # -----------------------------------------------------------------------------------------------------------      
                for     row_index   in range(arg_dataframe.shape[0]):
                        for     column_index   in   range(arg_dataframe.shape[1]):
                                if( isinstance(arg_dataframe.iloc[row_index,column_index],Decimal) ):
                                            arg_dataframe.iloc[row_index,column_index] = round(arg_dataframe.iloc[row_index,column_index],arg_precision)
                return(arg_dataframe)

        @staticmethod
        def     convert_to_decimal( arg_dataframe:pandas.DataFrame
                                  )->pandas.DataFrame:

                # -----------------------------------------------------------------------------------------------------------      
                # function:     convert_to_decimal (STATIC)
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat   
                # description:  because of rounding issues inherent in float values, convert all float values to Decimal. 
                #               This is more geared for anything modeling / using financial data with currencies than
                #               abstract calculations in float.
                #               A lot of ways you will import data (excel/csv/some db types) will end up with float.
                # -----------------------------------------------------------------------------------------------------------      
                for     row_index   in range(arg_dataframe.shape[0]):
                        if( isinstance(arg_dataframe.iloc[row_index,0],float) ):
                                arg_dataframe.iloc[row_index].apply(Decimal)
                return( arg_dataframe )

        @staticmethod
        def     random_filled(      arg_rows:int,
                                    arg_cols:int
                                  )->pandas.DataFrame:
                # -----------------------------------------------------------------------------------------------------------      
                # function:     random_filled (STATIC)
                # -----------------------------------------------------------------------------------------------------------      
                # created:      2026-01-20 Bruce Malicoat  
                # description:  create a random arg_rows x arg_cols dataframe with Decimal data types with random values
                #               between 0 and 100 via numpy library.
                # -----------------------------------------------------------------------------------------------------------      
                list_of_columns = []
                for     column_index in range(1,arg_cols+1):
                        list_of_columns.append( openpyxl.utils.get_column_letter( column_index ) )
                filled_dataframe = pandas.DataFrame(data=numpy.random.uniform(0,100,size=(arg_rows,arg_cols)),columns=list_of_columns)
                filled_dataframe = Datawindow.convert_to_decimal(filled_dataframe)
                filled_dataframe = Datawindow.round( filled_dataframe,2)
                return(filled_dataframe)


    