import tkinter
import tkinter.ttk
import sys
import pandastable
import pandas
import numpy

tkroot = tkinter.Tk()

# main window properties
tkroot.title("gittools v1.0.0")
tkroot.configure(background="yellow")
tkroot.state('zoomed')
# tkroot.minsize(200, 200)
# tkroot.maxsize(500, 500)
# tkroot.geometry("300x300+50+50")
tkroot.grid_rowconfigure(0, weight=1)
tkroot.grid_columnconfigure(1, weight=1)

# frame
frame_1 = tkinter.Frame(tkroot, bg="white")
#frame_1.pack(padx=1, pady=1,   side="left",        fill="none",expand=False)
frame_1.grid(row=0,column=0,sticky="NSEW")
frame_2 = tkinter.Frame(tkroot, bg="green")
#frame_2.pack(padx=1, pady=1,    side='left',        fill="none",expand=False)
frame_2.grid(row=0,column=1,sticky="NSEW")

# Tools and Filters tabs
notebook_1 = tkinter.ttk.Notebook(frame_1)
#notebook_1.pack(expand=True, fill="both")
notebook_1.grid(column=0,row=0,sticky='NW')

tab_1 = tkinter.Frame(notebook_1, bg="lightblue")
tab_2 = tkinter.Frame(notebook_1, bg="lightgreen")

notebook_1.add(tab_1, text="Tab   1")
notebook_1.add(tab_2, text="Tab   2")


# # labels
# tkinter.Label(tkroot, text="Nothing will work unless you do.").pack()
# tkinter.Label(tkroot, text="- Maya Angelou").pack()

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

# # button
# def button_on_click():
#     sys.exit(0)

# button_exit = tkinter.Button(
#                                 tkroot,
#                                 text="Exit",
#                                 command=button_on_click,
#                             )
# button_exit.pack(padx=5, pady=5,anchor="e")

# # checkbox 
# checkbox_1_var = tkinter.IntVar()

# def checkbox_toggle():
#     checked = "Checked" if checkbox_1_var.get() else "Unchecked"
#     checkbox_1.config(text=f"{checked}")

# checkbox_1 = tkinter.Checkbutton(tkroot, text="Checked", variable=checkbox_1_var,anchor="sw")
# checkbox_1.select()
# checkbox_1.config(command=checkbox_toggle)
# checkbox_1.pack(padx=5, pady=10)

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



# # image
# image_git   = tkinter.PhotoImage(file="git.png")#.zoom(4,4).subsample(2,2)
# image_label = tkinter.Label(frame_2, image=image_git, anchor="s")
# image_label.pack(expand=True)


df = pandas.DataFrame([['1','2'],['A','B']],columns=['column1','column2'])

pt = pandastable.Table(frame_2, dataframe=df, showtoolbar=True, showstatusbar=True)
pt.show()


tkroot.mainloop()
