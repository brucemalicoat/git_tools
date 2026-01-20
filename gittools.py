#region imports
import  tkinter
import  tkinter.ttk
import  sys
import  pandastable
import  pandas
import  numpy
import  tksheet
from    decimal                 import  Decimal
import  decimal
import  webcolors
from    Classes.Datawindow      import  Datawindow
from    Classes.Frame           import  Frame
import  openpyxl.utils
import  os
#endregion imports

os.chdir("c:/git/github/git_tools")
tkroot = tkinter.Tk()

# main window properties
# ----------------------
tkroot.title("gittools v1.0.0")
tkroot.configure(background="white")
tkroot.state('zoomed')
tkroot.minsize(800, 600)
tkroot.grid_rowconfigure(0, weight=1)
tkroot.grid_columnconfigure(1, weight=1)


# frame
frame_1 = Frame(master=tkroot, bg="white")
frame_1.grid(row=0,column=0,sticky="NSEW")

frame_2 = Frame(master=tkroot, bg="white")
frame_2.grid(row=0,column=1,sticky="NSEW")



# Tools and Filters tabs
notebook_1 = tkinter.ttk.Notebook(frame_1)
notebook_1.grid(column=0,row=0,sticky='NW')

tab_1 = Frame(master=notebook_1, bg="lightblue")
tab_2 = Frame(master=notebook_1, bg="lightgreen")

notebook_1.add(tab_1, text="Tab   1")
notebook_1.add(tab_2, text="Tab   2")

radiobutton_var = tkinter.StringVar(value="None")
for tool in ["1", "2","3","4"]:
    tkinter.Radiobutton(
        tab_1,
        text=tool,
        variable=radiobutton_var,
        value=tool,
        bg="lightblue",
    ).pack(anchor="w", padx=1, pady=1,side="top",expand=True)

image_git2   = tkinter.PhotoImage(file="git.png")#.zoom(8,8).subsample(2,2)
image_label = tkinter.Label(tab_1, image=image_git2, anchor="n")
image_label.pack(side="top",expand=True)


# combobox
combobox_1_var = tkinter.StringVar()

def combobox_1_selection_changed(event):
    print(f"{event.widget.get()}")
def combobox_1_itemchanged(*args):
    print(f"{combobox_1_var.get()}")

combobox_1 = tkinter.ttk.Combobox(tab_2, values=["One", "Two", "Three"],textvariable=combobox_1_var)
combobox_1.set("One")
combobox_1.config(state="normal")
combobox_1.bind("<<ComboboxSelected>>", combobox_1_selection_changed)
combobox_1_var.trace_add("write", combobox_1_itemchanged)
combobox_1.pack(padx=5, pady=5, fill="x",anchor="n",expand=True)


# pandastable
# -----------
pt_1 = Datawindow(  parent=frame_2,
                    dataframe=Datawindow.random_filled(75,50)
                )
pt_1.rowcolors.iloc[3,7]=webcolors.name_to_hex('red')

tkroot.mainloop()
