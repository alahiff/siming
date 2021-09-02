from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

def doStuff():
    folder = folderPath.get()
    print("Doing stuff with folder", folder)

def clearStuff():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    variable.set(workflows[0])
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')

gui = Tk()
gui.geometry("800x400")
gui.title("Simulation Ingestor")

entry1l = Label(gui, text="Name", justify=LEFT, anchor="w")
entry1l.grid(row=0, column=0, sticky=W)
entry1 = Entry(gui)
entry1.grid(row=0, column=1)


gui = Tk()
gui.geometry("800x400")
gui.title("Simulation Ingestor")

entry1l = Label(gui, text="Name", justify=LEFT, anchor="w")
entry1l.grid(row=0, column=0, sticky=W)
entry1 = Entry(gui)
entry1.grid(row=0, column=1)


gui = Tk()
gui.geometry("800x400")
gui.title("Simulation Ingestor")

entry1l = Label(gui, text="Name", justify=LEFT, anchor="w")
entry1l.grid(row=0, column=0, sticky=W)
entry1 = Entry(gui)
entry1.grid(row=0, column=1)

workflows = ["Application 1", "Application 2", "Application 3"]
variable = StringVar(gui)
variable.set(workflows[0])

entry3l = Label(gui, text="Workflow name", justify=LEFT, anchor="w")
entry3l.grid(row=1, column=0, sticky=W)
entry3 = OptionMenu(gui, variable, *workflows)
entry3.grid(row=1, column=1)

entry2l = Label(gui, text="Configuration", justify=LEFT, anchor="w")
entry2l.grid(row=2, column=0, sticky=W)
entry2 = Entry(gui)
entry2.grid(row=2, column=1)

entry4l = Label(gui, text="Study ID", justify=LEFT, anchor="w")
entry4l.grid(row=3, column=0, sticky=W)
entry4 = Entry(gui)
entry4.grid(row=3, column=1)

entry5l = Label(gui, text="Study URL", justify=LEFT, anchor="w")
entry5l.grid(row=4, column=0, sticky=W)
entry5 = Entry(gui)
entry5.grid(row=4, column=1)

folderPath = StringVar()
a = Label(gui, text="Directory name", justify=LEFT, anchor="w")
a.grid(row=5, column = 0, sticky=W)
E = Entry(gui, textvariable=folderPath)
E.grid(row=5, column=1)
btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
btnFind.grid(row=5,column=2)

c = ttk.Button(gui, text="Ingest", command=doStuff)
c.grid(row=8,column=0)

d = ttk.Button(gui, text="Clear", command=clearStuff)
d.grid(row=8,column=1)


gui.mainloop()
