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

tkroot = tkinter.Tk()

# main window properties
tkroot.title("gittools v1.0.0")
tkroot.configure(background="white")
tkroot.state('zoomed')
# tkroot.minsize(200, 200)
# tkroot.maxsize(500, 500)
# tkroot.geometry("300x300+50+50")
tkroot.grid_rowconfigure(2, weight=1)
tkroot.grid_columnconfigure(1, weight=1)

# frame
frame_1 = tkinter.Frame(tkroot, bg="white")
#frame_1.pack(padx=1, pady=1,   side="left",        fill="none",expand=False)
frame_1.grid(row=0,column=0,sticky="NSEW")

frame_2 = tkinter.Frame(tkroot, bg="white")
#frame_2.pack(padx=1, pady=1,    side='left',        fill="none",expand=False)
frame_2.grid(row=0,column=1,sticky="NSEW")

frame_3 = tkinter.Frame(tkroot, bg="white")
#frame_3.pack(padx=1, pady=1,    side='left',        fill="none",expand=False)
frame_3.grid(row=1,column=1,sticky='NSEW')

frame_4 = tkinter.Frame(tkroot, bg="white")
#frame_4.pack(padx=1, pady=1,    side='left',        fill="none",expand=False)
frame_4.grid(row=2,column=1,sticky='NSEW')


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
def round_to_2(arg_value,arg_precision=2):
    if isinstance(arg_value,Decimal):
            return round(arg_value,arg_precision)
    else:
            return arg_value 

df = pandas.DataFrame([[Decimal("1.9998"),Decimal("2.90028374019283740223412352349128360491238")],[Decimal("3.2938419283470192834"),Decimal("4.2938470192374388333")]],columns=['column1','column2'])
df=df.map(round_to_2,arg_precision=15)
print(df)


# treeview
treeview_1 = tkinter.ttk.Treeview(frame_2)
#treeview_1.pack(fill='both',expand=True)
treeview_1.grid(column=0,row=0,sticky='NSEW')
treeview_1["columns"]=list(df)
treeview_1["show"] = "headings"

for columns in df.columns:
        treeview_1.heading(columns,text=columns)
        treeview_1.column(columns,width=100)

for index, row in df.iterrows():
        treeview_1.insert("","end",values=list(row))

# pandastable
def pt_clicked(self, index): # index is a QModelIndex
    print(f"Cell ({index.row()}, {index.column()}) clicked!")

pt_1 = pandastable.Table(frame_3, dataframe=df, showtoolbar=True, showstatusbar=True)
pt_1.grid(column=0,row=0,sticky='NSEW')
pt_1.clear_styles()
list_of_rows = []
for index, column in df.iterrows():
        list_of_rows.append(index)
pt_1.setRowColors(list_of_rows,webcolors.name_to_hex('white'),'all')
pt_1.rowcolors.iloc[1,:]=webcolors.name_to_hex('red')
print(pt_1.rowcolors)
print(type(pt_1.rowcolors))
pt_1.redraw()
pt_1.show()


# tksheet
# https://stackoverflow.com/questions/70001624/build-a-fixed-size-data-table-with-tkinter-tksheet-in-python-bug-in-sheet-d
sheet_1 = tksheet.Sheet(frame_4,data=[[]])
# sheet_1.headers(list(df.columns))
sheet_1.grid(column=0,row=0,sticky='NSEW')
sheet_1.set_options(expand_sheet_if_paste_too_big=False)
sheet_1.enable_bindings(            # enable table behavior
                                   "single_select",
                                    "select_all",
                                    "column_select",
                                    "row_select",
                                    "drag_select",
                                    "arrowkeys",
                                    "column_width_resize",
                                    "double_click_column_resize",
                                    "row_height_resize",
                                    "double_click_row_resize",
                                    "right_click_popup_menu",
                                    "rc_select",  # rc = right click
                                    "copy",
                                    "cut",
                                    "paste",
                                    "delete",
                                    "undo",
                                    "edit_cell"
                                    )

# sheet_1.extra_bindings("end_edit_cell",      func=f_cell_edited)
# sheet_1.extra_bindings("end_paste",          func=f_cells_pasted)

sheet_1.delete_column(0)
sheet_1.delete_row(0)

for index,column_name in enumerate(list(df.columns)):
        sheet_1.set_header_data(column_name,index)
for index, row in df.iterrows():
        sheet_1.insert_row(list(row))

sheet_1.redraw()

tkroot.mainloop()
