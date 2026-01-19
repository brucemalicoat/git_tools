import tkinter
import tkinter.ttk
import sys

tkroot = tkinter.Tk()

# main window properties
tkroot.title("gittools v1.0.0")
tkroot.configure(background="black")
tkroot.minsize(200, 200)
tkroot.maxsize(500, 500)
tkroot.geometry("300x300+50+50")

# # labels
# tkinter.Label(tkroot, text="Nothing will work unless you do.").pack()
# tkinter.Label(tkroot, text="- Maya Angelou").pack()

# # image
# image_git   = tkinter.PhotoImage(file="git.png").zoom(4,4).subsample(2,2)
# image_label = tkinter.Label(tkroot, image=image_git, anchor="s")
# image_label.pack(expand=True)

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

combobox_1 = tkinter.ttk.Combobox(tkroot, values=["One", "Two", "Three"],textvariable=combobox_1_var)
combobox_1.set("One")
combobox_1.config(state="normal")
combobox_1.bind("<<ComboboxSelected>>", combobox_1_selection_changed)
combobox_1_var.trace_add("write", combobox_1_itemchanged)
combobox_1.pack(padx=5, pady=5, fill="x",anchor="center")


tkroot.mainloop()
