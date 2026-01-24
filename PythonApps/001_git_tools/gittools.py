import  os
os.chdir("c:/git/github/git_tools/PythonApps/001_git_tools")
#region imports
import sys
import tkinter
import pandastable
sys.path.append('../..')
from    PythonClasses.Datawindow      import  Datawindow
from    PythonClasses.Frame           import  Frame
from    PythonClasses.Window          import  Window
from    PythonClasses.Notebook        import  Notebook
#endregion imports

w_main = Window(title="gittools v1.0.0")

# main window properties
# ----------------------
w_main.StandardWindow1( tabcount = 2, framecount = 2, tabnames=['Configuration','Data'] )
w_main.ivar_datatable.set_cell_background_color(x=3,y=3,color="red")

w_main.mainloop()
