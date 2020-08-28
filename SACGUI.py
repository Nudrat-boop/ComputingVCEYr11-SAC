from tkinter import*

from functools import partial

window = Tk() 

window.title("Programming Calculator")
window.geometry('1000x600')
window.config(bg= "#114B5F")



titleLable = Label(window, text = "Programming Calculator", font=("Consolas", 13, "bold","italic"), fg = "#ffffff", bg= "#114B5F")
titleLable.grid(column = 0, row= 2, columnspan = 10, sticky = W)
 
sum = 0

canvas3 = Canvas(window, width = 200, height = 100, bg = "#114B5F", borderwidth = 0, highlightthickness = 0)
canvas3.grid(row = 11, column = 10, columnspan = 4, rowspan = 5)

canvas2 = Canvas(window, width = 200, height = 100, bg = "#114B5F", borderwidth = 0, highlightthickness = 0)
canvas2.grid(row = 11, column = 5, columnspan = 4, rowspan = 5)

canvas4 = Canvas(window, width = 200, height = 100, bg = "#114B5F", borderwidth = 0, highlightthickness = 0)
canvas4.grid(row = 11, column = 15, columnspan = 4, rowspan = 5)

canvas1 = Canvas(window, width = 200, height = 100, bg = "#114B5F", borderwidth = 0, highlightthickness = 0)
canvas1.grid(row = 11, column = 0, columnspan = 4, rowspan = 5)

window.grid_rowconfigure(10, minsize = 20)

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

rectangle3 = round_rectangle(canvas3, 0, 0, 200, 100, radius=20, fill="#999999")

rectangle2 = round_rectangle(canvas2, 0, 0, 200, 100, radius=20, fill="#999999")

rectangle4 = round_rectangle(canvas4, 0, 0, 200, 100, radius=20, fill="#999999")

rectangle1 = round_rectangle(canvas1, 0, 0, 200, 100, radius=20, fill="#999999")


mainEntry = Entry(window, width=100, font=("Consolas", 14), bg = "#4432a8")
mainEntry.insert(0, str(sum))
mainEntry.config(state = "readonly")
mainEntry.grid(column = 0, row = 4, ipady = 20, columnspan = 20)
 
def updateMainEntry(event, lbl):
    mainEntry.config(state = "normal")
    mainEntry.delete(0, END)
    mainEntry.insert(0, lbl["text"])
    mainEntry.config(state = "readonly")

def highlight(event, thisField):
    thisField.config(bg = "#E6E6E6", fg = "#000000")

def stopHighlight(event, thisField):
    thisField.config(bg= "#114B5F", fg = "#ffffff")

hexTitle = Label(window, text = "HEX |", font=("Consolas", 12, "bold"), bg= "#114B5F", fg = "#ffffff")
hexTitle.grid(sticky = W, column = 0, columnspan = 2, row = 6)


hexValue = Label(window, text = "0", bg= "#114B5F", fg = "#ffffff", font=("Consolas", 12, "bold"))
hexValue.grid(column = 1, row = 6, sticky = W, columnspan = 10)
hexValue.bind("<Button-1>", partial(updateMainEntry, lbl = hexValue))
hexValue.bind("<Enter>", partial(highlight, thisField = hexValue))
hexValue.bind("<Leave>", partial(stopHighlight, thisField = hexValue))

hexTitle.bind("<Button-1>", partial(updateMainEntry, lbl = hexValue))
hexTitle.bind("<Enter>", partial(highlight, thisField = hexValue))
hexTitle.bind("<Leave>", partial(stopHighlight, thisField = hexValue))

decTitle= Label(window, text = "DEC |", font=("Consolas", 12, "bold"), bg= "#114B5F", fg = "#ffffff")
decTitle.grid(sticky = W, column = 0, columnspan = 2,  row = 7)

decValue = Label(window, text = "0", bg= "#114B5F", fg = "#ffffff", font=("Consolas", 12, "bold"))
decValue.grid(column = 1, row = 7, sticky = W, columnspan = 10)
decValue.bind("<Button-1>", partial(updateMainEntry, lbl = decValue))
decValue.bind("<Enter>", partial(highlight, thisField = decValue))
decValue.bind("<Leave>", partial(stopHighlight, thisField = decValue))

decTitle.bind("<Button-1>", partial(updateMainEntry, lbl = decValue))
decTitle.bind("<Enter>", partial(highlight, thisField = decValue))
decTitle.bind("<Leave>", partial(stopHighlight, thisField = decValue))

octTitle = Label(window, text = "OCT |", font=("Consolas", 12, "bold"), bg= "#114B5F", fg = "#ffffff")
octTitle.grid(sticky = W, column = 0, columnspan = 2,  row = 8)


octValue = Label(window, text = "0", bg= "#114B5F", fg = "#ffffff", font=("Consolas", 12, "bold"))
octValue.grid(column = 1, row = 8, sticky = W, columnspan = 10)
octValue.bind("<Button-1>", partial(updateMainEntry, lbl = octValue))
octValue.bind("<Enter>", partial(highlight, thisField = octValue))
octValue.bind("<Leave>", partial(stopHighlight, thisField = octValue))

octTitle.bind("<Button-1>", partial(updateMainEntry, lbl = octValue))
octTitle.bind("<Enter>", partial(highlight, thisField = octValue))
octTitle.bind("<Leave>", partial(stopHighlight, thisField = octValue))

binTitle = Label(window, text = "BIN |", font=("Consolas", 12, "bold"), bg= "#114B5F", fg = "#ffffff")
binTitle.grid(sticky = W, column = 0, columnspan = 2,  row = 9)

binValue = Label(window, text = "0", bg= "#114B5F", fg = "#ffffff", font=("Consolas", 12, "bold"))
binValue.grid(column = 1, row = 9, sticky = W, columnspan = 10)
binValue.bind("<Button-1>", partial(updateMainEntry, lbl = binValue))
binValue.bind("<Enter>", partial(highlight, thisField = binValue))
binValue.bind("<Leave>", partial(stopHighlight, thisField = binValue))

binTitle.bind("<Button-1>", partial(updateMainEntry, lbl = binValue))
binTitle.bind("<Enter>", partial(highlight, thisField = binValue))
binTitle.bind("<Leave>", partial(stopHighlight, thisField = binValue))


def swapDigit(theButton):
    if(theButton["text"] == "0"): 
        theButton.config(text = "1")
    elif(theButton["text"] == "1"):
        theButton.config(text = "0")


def valueChange(index, theButton):
    global sum
    if (theButton["text"] == "0"):
        sum = sum - pow(2, index)
    elif(theButton["text"] == "1"):
        sum = sum + pow(2, index)
    mainEntry.config(state = "normal")
    mainEntry.delete(0, END)
    mainEntry.insert(0, str(sum))
    mainEntry.config(state = "readonly")
    decValue["text"] = str(sum)
    binValue["text"] = str(decimalToBinary(sum))
    hexValue["text"] = str(decimaltoHex(sum))
    octValue["text"] = str(decimaltoOct(sum))
    print(sum)

def swapAndValueChange(theButton, index):
    swapDigit(theButton)
    valueChange(index, theButton)

def decimalToBinary(number):
    return bin(number).replace("0b","")

def decimaltoHex(number):
    return hex(number).replace("0x", "")

def decimaltoOct(number):
    return oct(number).replace("0o", "")





    




bit0 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit0.config(command = partial(swapAndValueChange, bit0, 0))
bit0.grid(column = 18, row= 11)

bit1 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit1.config(command = partial(swapAndValueChange, bit1, 1))
bit1.grid(column = 17, row = 11)

bit2= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit2.config(command = partial(swapAndValueChange, bit2, 2))
bit2.grid(column = 16, row = 11)

bit3= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit3.config(command = partial(swapAndValueChange, bit3, 3))
bit3.grid(column = 15, row = 11)





bit4= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit4.config(command = partial(swapAndValueChange, bit4, 4))
bit4.grid(column = 13, row= 11)

bit5 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit5.config(command = partial(swapAndValueChange, bit5, 5))
bit5.grid(column = 12, row = 11)

bit6= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit6.config(command = partial(swapAndValueChange, bit6, 6))
bit6.grid(column = 11, row = 11)

bit7= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit7.config(command = partial(swapAndValueChange, bit7, 7))
bit7.grid(column = 10, row = 11)

bit8 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit8.config(command = partial(swapAndValueChange, bit8, 8))
bit8.grid(column = 8, row= 11)

bit9 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit9.config(command = partial(swapAndValueChange, bit9, 9))
bit9.grid(column = 7, row = 11)

bit10= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit10.config(command = partial(swapAndValueChange, bit10, 10))
bit10.grid(column = 6, row = 11)

bit11= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit11.config(command = partial(swapAndValueChange, bit11, 11))
bit11.grid(column = 5, row = 11)

bit12 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit12.config(command = partial(swapAndValueChange, bit12, 12))
bit12.grid(column = 3, row= 11)

bit13 = Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit13.config(command = partial(swapAndValueChange, bit13, 13))
bit13.grid(column = 2, row = 11)

bit14= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit14.config(command = partial(swapAndValueChange, bit14, 14))
bit14.grid(column = 1, row = 11)

bit15= Button(window, text = "0", bg = "#66656e", fg = "#ffffff")
bit15.config(command = partial(swapAndValueChange, bit15, 15))
bit15.grid(column = 0, row = 11)
 
lbl1= Label(window, text = "0", font=("Consolas", 10 , "italic"), bg = "#66656e", fg = "#ffffff")
lbl1.grid(column = 18, row = 12)

lbl2 = Label(window, text = "4", font=("Consolas", 10,"italic"), bg = "#66656e", fg = "#ffffff")
lbl2.grid(column = 13, row= 12)

lbl3= Label(window, text = "8", font=("Consolas", 10, "italic"), bg = "#66656e", fg = "#ffffff")
lbl3.grid(column = 8, row = 12)

lbl4 = Label(window, text = "12", font=("Consolas", 10, "italic"), bg = "#66656e", fg = "#ffffff")
lbl4.grid(column = 3, row = 12)







window.mainloop()


