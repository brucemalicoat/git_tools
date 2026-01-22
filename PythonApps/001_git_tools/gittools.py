import  os
os.chdir("c:/git/github/git_tools/PythonApps/001_git_tools")
#region imports
import sys
sys.path.append('../..')
from    PythonClasses.Datawindow      import  Datawindow
from    PythonClasses.Frame           import  Frame
from    PythonClasses.Window          import  Window
from    PythonClasses.Notebook        import  Notebook
#endregion imports

w_main = Window()

# main window properties
# ----------------------
w_main.title("gittools v1.0.0")
w_main.StandardWindow1()

# image_git2   = tkinter.PhotoImage(file="git.png")#.zoom(8,8).subsample(2,2)
# image_label  = tkinter.Label(w_main, image=image_git2, anchor="n")
# image_label.pack(side="top",expand=True)


w_main.mainloop()
