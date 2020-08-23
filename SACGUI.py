from tkinter import*

from functools import partial

window = Tk() 

window.title("Programming Calculator")

window.geometry('1000x600')



titleLable = Label(window, text = "Programming Calculator", font=("Consolas", 13, "bold","italic"))
titleLable.grid(column = 0, row= 2, columnspan = 10, sticky = W)
 
sum = 0

mainEntry = Entry(window, width=100)
mainEntry.insert(0, str(sum))
mainEntry.grid(column = 0, row = 4, ipady = 20, columnspan = 20)
 


hexTitle = Label(window, text = "HEX  |", font=("Consolas", 9))
hexTitle.grid(column = 0, row = 6)

hexValue = Label(window, text = "0")
hexValue.grid(column = 1, row = 6, sticky = W)

decTitle= Label(window, text = "DEC  |", font=("Consolas", 9))
decTitle.grid(column = 0, row = 7)

decValue = Label(window, text = "0")
decValue.grid(column = 1, row = 7, sticky = W)

octTitle = Label(window, text = "OCT  |", font=("Consolas", 9))
octTitle.grid(column = 0, row = 8)

octValue = Label(window, text = "0")
octValue.grid(column = 1, row = 8, sticky = W)

binTitle = Label(window, text = "BIN  |", font=("Consolas", 9))
binTitle.grid(column = 0, row = 9)

binValue = Label(window, text = "0")
binValue.grid(column = 1, row = 9, sticky = W)



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
    mainEntry.delete(0, END)
    mainEntry.insert(0, str(sum))
    print(sum)

def swapAndValueChange(theButton, index):
    swapDigit(theButton)
    valueChange(index, theButton)




    




bit0 = Button(window, text = "0")
bit0.config(command = partial(swapAndValueChange, bit0, 0))
bit0.grid(column = 18, row= 11)

bit1 = Button(window, text = "0")
bit1.config(command = partial(swapAndValueChange, bit1, 1))
bit1.grid(column = 17, row = 11)

bit2= Button(window, text = "0")
bit2.config(command = partial(swapAndValueChange, bit2, 2))
bit2.grid(column = 16, row = 11)

bit3= Button(window, text = "0")
bit3.config(command = partial(swapAndValueChange, bit3, 3))
bit3.grid(column = 15, row = 11)





bit4= Button(window, text = "0")
bit4.config(command = partial(swapAndValueChange, bit4, 4))
bit4.grid(column = 13, row= 11)

bit5 = Button(window, text = "0")
bit5.config(command = partial(swapAndValueChange, bit5, 5))
bit5.grid(column = 12, row = 11)

bit6= Button(window, text = "0")
bit6.config(command = partial(swapAndValueChange, bit6, 6))
bit6.grid(column = 11, row = 11)

bit7= Button(window, text = "0")
bit7.config(command = partial(swapAndValueChange, bit7, 7))
bit7.grid(column = 10, row = 11)

bit8 = Button(window, text = "0")
bit8.config(command = partial(swapAndValueChange, bit8, 8))
bit8.grid(column = 8, row= 11)

bit9 = Button(window, text = "0")
bit9.config(command = partial(swapAndValueChange, bit9, 9))
bit9.grid(column = 7, row = 11)

bit10= Button(window, text = "0")
bit10.config(command = partial(swapAndValueChange, bit10, 10))
bit10.grid(column = 6, row = 11)

bit11= Button(window, text = "0")
bit11.config(command = partial(swapAndValueChange, bit11, 11))
bit11.grid(column = 5, row = 11)

bit12 = Button(window, text = "0")
bit12.config(command = partial(swapAndValueChange, bit12, 12))
bit12.grid(column = 3, row= 11)

bit13 = Button(window, text = "0")
bit13.config(command = partial(swapAndValueChange, bit13, 13))
bit13.grid(column = 2, row = 11)

bit14= Button(window, text = "0")
bit14.config(command = partial(swapAndValueChange, bit14, 14))
bit14.grid(column = 1, row = 11)

bit15= Button(window, text = "0")
bit15.config(command = partial(swapAndValueChange, bit15, 15))
bit15.grid(column = 0, row = 11)
 
lbl1= Label(window, text = "0", font=("Consolas", 10 , "italic"))
lbl1.grid(column = 18, row = 12)

lbl2 = Label(window, text = "4", font=("Consolas", 10,"italic"))
lbl2.grid(column = 13, row= 12)

lbl3= Label(window, text = "8", font=("Consolas", 10, "italic"))
lbl3.grid(column = 8, row = 12)

lbl4 = Label(window, text = "12", font=("Consolas", 10, "italic"))
lbl4.grid(column = 3, row = 12)





window.mainloop()


