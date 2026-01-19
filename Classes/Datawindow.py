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

class   Datawindow(pandastable.Table):

        def     __init__(   self,
                            frame,
                            arg_dataframe:pandas.DataFrame):

                super().__init__(frame,dataframe=arg_dataframe,fgcolor="black",bgcolor="white",showtoolbar=True, showstatusbar=True,rows=1,columns=1)
                self.df = arg_dataframe
                if(isinstance(self.df,pandas.DataFrame)):
                        list_of_rows = []
                        for index in range(self.df.shape[0]):
                                list_of_rows.append(index)
                        self.setRowColors(list_of_rows,webcolors.name_to_hex('white'),'all')
                self.grid(column=0,row=0,sticky='NSEW')
                self.redraw()
                self.show()


        @staticmethod
        def     round(              arg_dataframe:pandas.DataFrame,
                                    arg_precision:int=2)->pandas.DataFrame:

                for     row_index   in range(arg_dataframe.shape[0]):
                        for     column_index   in   range(arg_dataframe.shape[1]):
                                if( isinstance(arg_dataframe.iloc[row_index,column_index],Decimal) ):
                                            arg_dataframe.iloc[row_index,column_index] = round(arg_dataframe.iloc[row_index,column_index],arg_precision)
                return(arg_dataframe)

        @staticmethod
        def     convert_to_decimal( arg_dataframe:pandas.DataFrame
                                  )->pandas.DataFrame:

                for     row_index   in range(arg_dataframe.shape[0]):
                        if( isinstance(arg_dataframe.iloc[row_index,0],float) ):
                                arg_dataframe.iloc[row_index].apply(Decimal)
                return( arg_dataframe )

        @staticmethod
        def     random_filled(      arg_rows:int,
                                    arg_cols:int
                                  )->pandas.DataFrame:

                list_of_columns = []
                for     column_index in range(1,arg_cols+1):
                        list_of_columns.append( openpyxl.utils.get_column_letter( column_index ) )
                filled_dataframe = pandas.DataFrame(data=numpy.random.uniform(0,100,size=(arg_rows,arg_cols)),columns=list_of_columns)
                filled_dataframe = Datawindow.convert_to_decimal(filled_dataframe)
                filled_dataframe = Datawindow.round( filled_dataframe,2)
                return(filled_dataframe)


    