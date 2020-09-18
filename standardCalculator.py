#Function: Standard Calculator 
#Input: Numbers and functions
#Output: Results 


from tkinter import*

from functools import partial

from math import*

from pathlib import Path

window = Tk() 

window.title("Standard Calculator")
window.geometry('800x750')
window.config(bg= "#114B5F")
folder = Path.cwd()
window.iconbitmap(str(folder) + "/projecticon.ico")
titleLable = Label(window, text = "Standard Calculator", font=("Consolas", 24, "bold", "italic"), fg = "#ffffff", bg= "#114B5F")
titleLable.grid(column = 1, row= 1, columnspan = 10, sticky = W)

mainEntryText = ""






mainEntry = Entry(window, width=33, font=("Consolas", 23), bg = "#ffffff")
mainEntry.grid(column = 0, row = 2, ipady = 20, columnspan = 20)
mainEntry.config(state = "readonly")

secondaryEntry = Entry(window, width=33, font=("Consolas", 23), bg = "#ffffff", justify = "right")
secondaryEntry.grid(column = 0, row = 3, ipady = 20, columnspan = 20)


def insertIntoMainEntry(character):
    global mainEntryText
    mainEntryText = mainEntryText + character
    mainEntry.config(state = "normal")
    mainEntry.delete(0, END)
    mainEntry.insert(0, mainEntryText)
    mainEntry.config(state = "readonly")

def clear():
    global mainEntryText
    mainEntry.config(state = "normal")
    secondaryEntry.delete(0, END)
    mainEntry.delete(0, END)
    mainEntryText = ""
    mainEntry.config(state = "readonly")

def backSpace():
    global mainEntryText
    mainEntry.config(state = "normal")
    mainEntryText = mainEntryText[:-1]
    mainEntry.delete(0, END)
    mainEntry.insert(0, mainEntryText)
    mainEntry.config(state = "readonly")

def displayResult():
    secondaryEntryText = mainEntryText.replace(u"\u00D7", "*").replace(u"\u00F7", "/").replace("%", "/100")
    print(mainEntryText)
    print(secondaryEntryText)
    secondaryEntry.delete(0, END)
    try:
        secondaryEntry.insert(0, eval(secondaryEntryText))
    except SyntaxError: 
        secondaryEntry.insert(0, "Error")
    print(eval(secondaryEntryText))


window.grid_rowconfigure(5, minsize = 90)
window.grid_rowconfigure(6, minsize = 90)
window.grid_rowconfigure(7, minsize = 90)
window.grid_rowconfigure(8, minsize = 90)

window.grid_columnconfigure(1, minsize = 150)
window.grid_columnconfigure(2, minsize = 150)
window.grid_columnconfigure(3, minsize = 150)
window.grid_columnconfigure(4, minsize = 150)
window.grid_columnconfigure(5, minsize = 150)


but1 = Button(window, text = "1", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "1")).grid(column = 1, row = 5)
but2 = Button(window, text = "2", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "2")).grid(column = 2, row = 5)
but3 = Button(window, text = "3", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "3")).grid(column = 3, row = 5)

but4 = Button(window, text = "4", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "4")).grid(column = 1, row = 6)
but5 = Button(window, text = "5", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "5")).grid(column = 2, row = 6)
but6= Button(window, text = "6", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "6")).grid(column = 3, row = 6)
but7 = Button(window, text = "7", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "7")).grid(column = 1, row = 7)
but8 = Button(window, text = "8", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "8")).grid(column = 2, row = 7)
but9 = Button(window, text = "9", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "9")).grid(column = 3, row = 7)
but0 = Button(window, text = "0", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "0")).grid(column = 2, row = 8)
dotBut = Button(window, text = ".", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, ".")).grid(column = 1, row = 8)
equalBut = Button(window, text = "=", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 12, command = displayResult).grid(column = 4, row = 8, columnspan = 2)

addBut = Button(window, text = "+", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "+")).grid(column = 4, row = 6)
subBut =  Button(window, text = "-", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "-")).grid(column = 5, row = 6)
divideBut=  Button(window, text = u"\u00F7", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, u"\u00F7")).grid(column = 4, row = 7)
multipleBut= Button(window, text = u"\u00D7", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, u"\u00D7")).grid(column = 5, row = 7)
cBut = Button(window, text = "C", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = clear).grid(column = 5, row = 5)
delBut = Button(window, text = "DEL", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = backSpace).grid(column = 4, row = 5)


negBut =  Button(window, text = "%", font=("Helvetica", 26, "bold"), fg = "#000000", bg = "#E6E6E6", height = 1, width = 5, command = partial(insertIntoMainEntry, "%")).grid(column = 3, row = 8)



def openFile(file):
    folder = Path.cwd()
    window.destroy()
    exec(open(str(folder)+"/"+file).read(), globals())

homepageBtn = Button(window, text = "Homepage", font = ("Helvetica", 12, "bold"), fg = "#ffffff", bg = "#F45B69", width = 15, command = partial(openFile, "homepage.py"))
homepageBtn.grid(column = 1, row = 0, columnspan = 2, sticky = W)


programmingBtn = Button(window, text = "Programming", font = ("Helvetica", 12, "bold"), fg = "#ffffff", bg = "#F45B69", width = 15, command = partial(openFile, "SACGUI.py"))
programmingBtn.grid(column = 3, row = 0, columnspan = 2, sticky = W)

scientificBtn = Button(window, text = "Scientific", font = ("Helvetica", 12, "bold"), fg = "#ffffff", bg = "#F45B69", width = 15, command = partial(openFile, "SACGUI.ScientificCalculator.py"))
scientificBtn.grid(column = 4, row = 0, columnspan = 2, sticky = E)


window.mainloop()