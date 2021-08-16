from tkinter import *

firstNum = None
# setting the mainframe
root = Tk()
root.geometry("300x389")
inpFrame = Frame(root, width=400, height=50, bg="grey")
inpFrame.pack(side=TOP)
btnFrame = Frame(root, bg="white")
btnFrame.pack()

#setting the entry
inpBar = Entry(inpFrame)
inpBar.grid(row=0, column=0)


# function for addition button
def addBtn():
    num1 = inpBar.get()
    global firstNum
    firstNum = int(num1)
    inpBar.delete(0, END)

# function for equal button
def eqlButn():
    global firstNum
    num2 = inpBar.get()
    inpBar.delete(0, END)
    inpBar.insert(0, firstNum + int(num2))

# function add numbers to entry
def numberBtn(num):
    current = inpBar.get()
    inpBar.delete(0, END)
    inpBar.insert(0, str(current)+str(num))
    

#first row buttons
button0 = Button(btnFrame, text="0", bg="grey", fg="black", command=lambda: numberBtn(0), pady=30, padx=27)
button1 = Button(btnFrame, text="1", bg="grey", fg="black", command=lambda: numberBtn(1), pady=30, padx=27)
button2 = Button(btnFrame, text="2", bg="grey", fg="black", command=lambda: numberBtn(2), pady=30, padx=27)

#second row buttons
button3 = Button(btnFrame, text="3", bg="grey", fg="black", command=lambda: numberBtn(3), pady=30, padx=27)
button4 = Button(btnFrame, text="4", bg="grey", fg="black", command=lambda: numberBtn(4), pady=30, padx=27)
button5 = Button(btnFrame, text="5", bg="grey", fg="black", command=lambda: numberBtn(5), pady=30, padx=27)

#third row buttons
button6 = Button(btnFrame, text="6", bg="grey", fg="black", command=lambda: numberBtn(6), pady=30, padx=27)
button7 = Button(btnFrame, text="7", bg="grey", fg="black", command=lambda: numberBtn(7), pady=30, padx=27)
button8 = Button(btnFrame, text="8", bg="grey", fg="black", command=lambda: numberBtn(8), pady=30, padx=27)

#forth row buttons
button9 = Button(btnFrame, text="9", bg="grey", fg="black", command=lambda: numberBtn(9), pady=30, padx=27)
buttonAdd = Button(btnFrame, text="+", bg="grey", fg="black", command=addBtn, pady=30, padx=27)
buttonEql = Button(btnFrame, text="=", bg="grey", fg="black", command=eqlButn, pady=30, padx=27)


#Row 1
button0.grid(row=1, column=0)
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
#Row 2
button3.grid(row=2, column=0)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
#Row 3
button6.grid(row=3, column=0)
button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
#Row4
button9.grid(row=4, column=0)
buttonAdd.grid(row=4, column=1)
buttonEql.grid(row=4, column=2)

root.mainloop()
