#Function: Home page
#Input: Choosing a particular calculator
#Output: The calculator  


from tkinter import*

from pathlib import Path


from functools import partial

window = Tk() 

window.title("homepage")
window.geometry('600x570')
window.config(bg= "#114B5F")
folder = Path.cwd()
window.iconbitmap(str(folder) + "/projecticon.ico")
window.grid_rowconfigure(6, minsize = 25)
window.grid_columnconfigure(0, minsize = 95)
window.grid_rowconfigure(0, minsize = 140)
window.grid_rowconfigure(8, minsize = 25)
window.grid_rowconfigure(10, minsize = 25)

def openFile(file):
    folder = Path.cwd()
    window.destroy()
    exec(open(str(folder)+"/"+file).read(), globals())





titleLabel = Label(window, text = "CALCUCALOAD", font = ("Verdana", 35, "bold"), fg = "#FFB366", bg = "#F45B69")
titleLabel.grid(column = 1, row = 5)


standardBtn = Button(window, text = "Standard Calculator", font = ("Helvetica", 12, "bold"), fg = "#ffffff", bg = "#F45B69", width = 20, command = partial(openFile, "standardCalculator.py"))
standardBtn.grid(column = 1, row = 7)

programmingBtn = Button(window, text = "Programming Calculator", font = ("Helvetica", 12, "bold"), fg = "#ffffff", bg = "#F45B69", width = 20, command = partial(openFile, "SACGUI.py"))
programmingBtn.grid(column = 1, row = 9)

scientificBtn = Button(window, text = "Scientific Calculator", font = ("Helvetica", 12, "bold"), fg = "#ffffff", bg = "#F45B69", width = 20, command = partial(openFile, "SACGUI.ScientificCalculator.py"))
scientificBtn.grid(column = 1, row = 11)




window.mainloop()