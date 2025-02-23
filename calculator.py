from tkinter import *
from tkinter import messagebox

cal = Tk()                     
cal.geometry("312x394")         
cal.resizable(0, 0)             
cal.title("Calculator")


def about():
    messagebox.showinfo('About'," \n Created by Shahmir Riddo \n \n  Github :\n  https://github.com/shahmir-riddo")

def click_button(item):                                          
    global expression
    inputText.set(inputText.get()+(str(item)))

def clear_button():                                               
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clear_all():                                                 
    inputText.set("")

def equal_button():
    result = ""
    try:
        result = eval(inputText.get())                            
        inputText.set(result)
    except:
        result = "_ERROR_"
        inputText.set(result)

# Coded by Shahmir Riddo
menubar = Menu(cal,bg="black",fg="grey")

filemenu = Menu(menubar, tearoff=0,bg="black",fg="white")
filemenu.add_command(label="Cut", accelerator="Ctrl+X" )
filemenu.add_command(label="Copy",accelerator="Ctrl+C" )
filemenu.add_command(label="Paste",accelerator="Ctrl+V")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=cal.quit)

menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0,bg="black",fg="white")
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

cal.config(bg="grey",menu=menubar)  


expression = ""
inputText = StringVar()                     


inputFrame = Frame(cal, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="crimson", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=("Lucida", 17), textvariable=inputText, width=50,fg="white", bg="black", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=14)


button_frame = Frame(cal, width=312, height=272.5, bg="white")
button_frame.pack()

clearall = Button(button_frame, text = "C", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: clear_all()).grid(row = 1, column = 0, padx = 1, pady = 1)
l_bracket= Button(button_frame, text = "(", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("(")).grid(row = 1, column = 1, padx = 1, pady = 1)
r_bracket = Button(button_frame, text = ")", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(")")).grid(row = 1, column = 2, padx = 1, pady = 1)
clear = Button(button_frame, text = "Remove", fg = "white", width = 10, height = 3, bd = 0, bg = "grey1",border=0,borderwidth=0, cursor = "hand2", command = lambda: clear_button()).grid(row = 1, column = 3, padx = 1, pady = 1)


power = Button(button_frame, text = "^", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("**")).grid(row = 2, column = 0, padx = 1, pady = 1)
pie = Button(button_frame, text = "π", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(3.1415)).grid(row = 2, column = 1, padx = 1, pady = 1)
exp  = Button(button_frame, text = "e", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(2.7182)).grid(row = 2, column = 2, padx = 1, pady = 1)
divide_= Button(button_frame, text = "/", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("/")).grid(row = 2, column = 3, padx = 1, pady = 1)


seven = Button(button_frame, text = "7", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight = Button(button_frame, text = "8", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(button_frame, text = "9", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
multiply = Button(button_frame, text = "x", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("*")).grid(row = 3, column = 3, padx = 1, pady = 1)


four = Button(button_frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(button_frame, text = "5", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(5)).grid(row = 4, column = 1, padx = 1, pady = 1)
six = Button(button_frame, text = "6", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(6)).grid(row = 4, column = 2, padx = 1, pady = 1)
minus = Button(button_frame, text = "-", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("-")).grid(row = 4, column = 3, padx = 1, pady = 1)


one = Button(button_frame, text = "1", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(1)).grid(row = 5, column = 0, padx = 1, pady = 1)
two = Button(button_frame, text = "2", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(2)).grid(row = 5, column = 1, padx = 1, pady = 1)
three = Button(button_frame, text = "3", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(3)).grid(row = 5, column = 2, padx = 1, pady = 1)
plus = Button(button_frame, text = "+", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button("+")).grid(row = 5, column = 3, padx = 0, pady = 0)


point = Button(button_frame, text = ".", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: click_button(".")).grid(row = 6, column = 0, padx = 1, pady = 1)
zero = Button(button_frame, text = "0", fg = "white", width = 10, height = 3, bd = 0, bg = "LightSkyBlue4", cursor = "hand2", command = lambda: click_button(0)).grid(row = 6, column = 1, padx = 1, pady = 1)
equals = Button(button_frame, text = "=", fg = "lightgreen", width = 21, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: equal_button()).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)
 
cal.mainloop()                      