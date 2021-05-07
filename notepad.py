from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser


root = Tk()
root.geometry("1200x685")
root.title("Text Editor")
root.iconbitmap("C:/WINDOWS/system32/notepad.exe")

#set varibale for open file name
global open_save_name
open_save_name = False
global green
green = "#00FF40"
global selected
selected = False

#newfile function
def newFile(e):
    global open_save_name
    open_save_name = False
    my_text.delete(1.0, END)
    root.title("Text Editor-New")
    status_bar.config(text="New File        ")
#open file function
def openFile(e):
    my_text.delete(1.0, END)

    text_file = filedialog.askopenfilename(initialdir="C:/Users/jwald/OneDrive/Documents", title="Open File", filetypes=(("Text files", "*txt"), ("HTML files", "*.html"), ("Python files", "*.py"), ("All Files", "*.*")))
    if text_file:
        global open_save_name
        open_save_name = text_file

    name = text_file
    status_bar.config(text=f"{name}        ")
    name = name.replace("C:/Users/jwald/OneDrive/Documents/", "")
    root.title(f"{name} - Text Editor")

    #open file
    text_file = open(text_file, "r")
    stuff = text_file.read()
    #add content to text widget
    my_text.insert(END, stuff)
    text_file.close()
#save as
def saveAsFile(e):
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File As", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f"Saved: {name}        ")
        name = name.replace("C:/Users/jwald/OneDrive/Documents/", "")
        root.title(f"{name} - Text Editor")

        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()
#save file
def saveFile(e):
    global open_save_name
    if open_save_name:
        status_bar.config(text=f"Saved: {open_save_name}        ")
        text_file = open(open_save_name, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()
    else:
        saveAsFile()
#cut text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")

            root.clipboard_clear()
            root.clipboard_append(selected)

def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
def bolded():
    # create font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    current_tags = my_text.tag_names("sel.first")
    #config tag
    my_text.tag_configure("bold", font=bold_font)
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")
def italic():
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")
    current_tags = my_text.tag_names("sel.first")
    #config tag
    my_text.tag_configure("italic", font=italic_font)
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")
def txt_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        color_font = font.Font(my_text, my_text.cget("font"))
        current_tags = my_text.tag_names("sel.first")
        my_text.tag_configure("colored", font=color_font, foreground=my_color)
        if "colored"  in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)
def all_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color, insertbackground=my_color)
def pick():
    my_color = colorchooser.askcolor()[1]
    my_text.config(fg=my_color)
def select_all(e):
    my_text.tag_add('sel', '1.0', 'end')
def clr_all(e):
    my_text.delete(1.0, END)
def nmo():
    bg_color = "#000000"
    text_bg = "#373737"
    text_color = "#ffffff"
    #set color
    status_bar.config(text="Night Mode         ")
    root.config(bg=bg_color)
    my_text.config(bg=text_bg, fg=text_color)
    status_bar.config(bg=bg_color, fg=text_color)
    tool_bar.config(bg=bg_color)
    boldbtn.config(bg=text_bg, fg="white")
    italicbtn.config(bg=text_bg, fg="white")
    redobtn.config(bg=text_bg, fg="white")
    undobtn.config(bg=text_bg, fg="white")
    #menu colors
    fileMenu.config(bg=bg_color, fg=text_color)
    editMenu.config(bg=bg_color, fg=text_color)
    colorMenu.config(bg=bg_color, fg=text_color)
    options.config(bg=bg_color, fg=text_color)
def nmoff():
    bg_color = "SystemButtonFace"
    text_bg = "SystemButtonFace"
    text_color = "black"
    #set color
    root.config(bg=bg_color)
    my_text.config(bg="White", fg=text_color)
    status_bar.config(bg=bg_color, fg=text_color)
    #toolbar
    tool_bar.config(bg=bg_color)
    boldbtn.config(bg=text_bg, fg=text_color)
    italicbtn.config(bg=text_bg, fg=text_color)
    redobtn.config(bg=text_bg, fg=text_color)
    undobtn.config(bg=text_bg, fg=text_color)
    #menu colors
    fileMenu.config(bg=bg_color, fg=text_color)
    editMenu.config(bg=bg_color, fg=text_color)
    colorMenu.config(bg=bg_color, fg=text_color)
    options.config(bg=bg_color, fg=text_color)
def hacker():
    root.config(bg="black")
    my_text.config(bg="black", fg=green, insertbackground=green, selectforeground="black", selectbackground=green)
    status_bar.config(bg="black", fg=green, text="Hacker Mode        ")
    tool_bar.config(bg="black")
    undobtn.config(bg="black", fg=green)
    redobtn.config(bg="black", fg=green)
    boldbtn.config(bg="black", fg=green)
    italicbtn.config(bg="black", fg=green)
    fileMenu.config(bg="black", fg=green)
    editMenu.config(bg="black", fg=green)
    colorMenu.config(bg="black", fg=green)
    options.config(bg="black", fg=green)
def hackeroff():
    root.config(bg="white")
    my_text.config(bg="white", fg="black")
    status_bar.config(bg="white", fg="black", text="Ready        ")
    tool_bar.config(bg="white")
    undobtn.config(bg="white", fg="black")
    redobtn.config(bg="white", fg="black")
    boldbtn.config(bg="white", fg="black")
    italicbtn.config(bg="white", fg="black")
    fileMenu.config(bg="white", fg="black")
    editMenu.config(bg="white", fg="black")
    colorMenu.config(bg="white", fg="black")
    options.config(bg="white", fg="black")
tool_bar = Frame(root)
tool_bar.pack(fill=X)

my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#horiontal scroll
horiz = Scrollbar(my_frame, orient="horizontal")
horiz.pack(side=BOTTOM, fill=X)

my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectforeground="green", selectbackground="black", undo=True, yscrollcommand=text_scroll.set, xscrollcommand=horiz.set, wrap="none")
my_text.pack()

text_scroll.config(command=my_text.yview)
horiz.config(command=my_text.xview)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)
# file menu
fileMenu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile, accelerator="ctrl+n")
fileMenu.add_command(label="Open", command=openFile, accelerator="ctrl+o")
fileMenu.add_command(label="Save", command=saveFile, accelerator="ctrl+s")
fileMenu.add_command(label="Save As", command=saveAsFile, accelerator="ctrl+shift+s")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit, accelerator="ctrl+w")
#edit menu
editMenu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="ctrl+x")
editMenu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="ctrl+c")
editMenu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="ctrl+v")
editMenu.add_separator()
editMenu.add_command(label="Undo", command=my_text.edit_undo, accelerator="ctrl+z")
editMenu.add_command(label="Redo", command=my_text.edit_redo, accelerator="ctrl+y")
editMenu.add_separator()
editMenu.add_command(label="Select All", command=lambda:select_all(False), accelerator="ctrl+a")
editMenu.add_command(label="Clear All", command=lambda:clr_all(False), accelerator="ctrl+q")
#options menu
options = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options)
options.add_command(label="Night Mode On", command=nmo)
options.add_command(label="Night Mode Off", command=nmoff)
options.add_command(label="Hacker Mode on", command=hacker)
options.add_command(label="Hacker Mode off", command=hackeroff)
#color menu
colorMenu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=colorMenu)
colorMenu.add_command(label="Change Selected Text", command=txt_color)
colorMenu.add_command(label="Change All Text", command=all_color)
colorMenu.add_command(label="Change Background", command=bg_color)
colorMenu.add_command(label="Custom Text Color", command=pick)
#add status bar
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)
root.bind('<Control-Q>', clr_all)
root.bind('<Control-q>', clr_all)
root.bind('<Control-S>', saveAsFile)
root.bind('<Control-s>', saveFile)
root.bind('<Control-o>', openFile)
root.bind('<Control-n>', newFile)
boldbtn = Button(tool_bar, text="Bold", border=1, command=bolded)
boldbtn.grid(row=0, column=0, sticky=W, padx=5)
italicbtn = Button(tool_bar, text="Italics", border=1,  command=italic)
italicbtn.grid(row=0, column=1, sticky=W, padx=5)
undobtn = Button(tool_bar, text="Undo", border=1,  command=my_text.edit_undo)
undobtn.grid(row=0, column=2, sticky=W, padx=5)
redobtn = Button(tool_bar, text="Redo", border=1, command=my_text.edit_redo)
redobtn.grid(row=0, column=3, sticky=W, padx=5)

root.mainloop()