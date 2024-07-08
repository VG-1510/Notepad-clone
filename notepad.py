from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor


def newfile():
    if len(textbox.get(1.0, END)) > 0:
        wantTosave = messagebox.askyesnocancel(
            title="Notepad", message="Do You want to Save the file")
        if wantTosave == True:
            save()
        elif wantTosave == False:
            textbox.delete(1.0, END)
        else:
            pass
        print(wantTosave)


def save():
    filedialog.asksaveasfile(title="Save As", defaultextension='.txt, .pdf')
    pass


def openFile():
    file = filedialog.askopenfile(title="open", defaultextension='.txt, .pdf')
    textbox.insert(1.0, file.read())
    # print(file.name.split('/')[-1].split('.')[0])
    win.title(file.name.split('/')[-1].split('.')[0])
    file.close()
    pass


def exit():
    win.destroy()


def undo():
    # textbox.edit_undo()
    textbox.event_generate("<<Undo>>")


# def cut():

    # textbox.clipboard_clear()
    # q = textbox.selection_get()
    # textbox.clipboard_append(q)
    # qindex = textbox.search(q, 0.0, END)
    # qlen = len(q)
    # qend=0
    # textbox.delete(qindex, qend)
    # print(qindex, float(qindex)+qlen)

def Cut():
    textbox.event_generate("<<Cut>>")


def copy():
    # q = textbox.selection_get()
    # extbox.clipboard_append(q)
    textbox.event_generate("<<Copy>>")


def paste():
    textbox.event_generate("<<Paste>>")


def abtus():
    messagebox.showinfo(title="About Us", message="created by vaibhav")

def font():
    color = askcolor()
    # print(color)

win = Tk()
win.geometry('1000x1000')
win.title("notepad clone")
fileTab = Menubutton(win, text='File')
filemenu = Menu(fileTab, tearoff=0)
fileTab['menu'] = filemenu
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="open", command=openFile)
filemenu.add_command(label="save", command=save)
filemenu.add_command(label="Exit", command=exit)
fileTab.grid(row="0", column="0")

EditTab = Menubutton(win, text='Edit')
Editmenu = Menu(EditTab, tearoff=0)
EditTab['menu'] = Editmenu
Editmenu.add_command(label="Undo   ctrl+z", command=undo)
Editmenu.add_command(label="Cut    ctrl+x", command=Cut)
Editmenu.add_command(label="Copy   ctrl+c", command=copy)
Editmenu.add_command(label="Paste  ctrl+v", command=paste)
EditTab.grid(row="0", column="2")


FormatTab = Menubutton(win, text='Format')
Formatmenu = Menu(FormatTab, tearoff=0)
FormatTab['menu'] = Formatmenu
Formatmenu.add_command(label="Font", command=font)
FormatTab.grid(row="0", column="3")

ViewTab = Menubutton(win, text='View')
Viewmenu = Menu(ViewTab, tearoff=0)
ViewTab['menu'] = Viewmenu
Viewmenu.add_command(label="Zoom", command=newfile)
Viewmenu.add_command(label="Status Bar", command=newfile)
ViewTab.grid(row="0", column="4")

HelpTab = Menubutton(win, text='Help')
Helpmenu = Menu(HelpTab, tearoff=0)
HelpTab['menu'] = Helpmenu
Helpmenu.add_command(label="Send feedback", command=newfile)
Helpmenu.add_command(label="About Notepad", command=abtus)
HelpTab.grid(row="0", column="5")
textbox = Text(win, height=500, width=500, undo=True)
textbox.place(x="0", y="20")
win.mainloop()
