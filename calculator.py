from tkinter import *
from tkinter import ttk
import math as m

calc_body = Tk()

calc_body.geometry("500x500")
calc_body.configure(bg="black")
calc_body.title("RO-Calc")
calc_body.resizable(0, 0)
displaybox = StringVar()
displaybox.set("")

net_result=""

def clear():
    global net_result
    net_result = ""
    displaybox.set("0")

def click(item_clicked):
    global net_result
    net_result = net_result + str(item_clicked)
    displaybox.set(net_result)
    return

def equals():
    global net_result
    try:
        total = str(eval(net_result))
        displaybox.set(total)
        #net_result = " "
    except:

        displaybox.set("ERROR !!!")
        net_result = ""

def backspace():
    content =entry_space.get()
    length = len(content)-1
    entry_space.delete(length,END)

def special(event):
    b=event.widget
    text=b['text']
    dis=entry_space.get()
    result = ""

    if text == "%":
       result = str((float(dis)*100))+" %"
       print(result,type(result))

    if text =="SQRT":
      result=str(m.sqrt(float(dis)))

    entry_space.delete(0,END)
    entry_space.insert(0,result)
    result=" "



#Display & entry settings

entry_space = Entry(calc_body, width=50,borderwidth=10, textvariable=displaybox,justify="right",relief=RIDGE, fg='white', bg='black',font=('arial', 20, 'bold'))

entry_space.place(y=10, x=20, height=80, width=450)


#function buttons
button_clear=Button(calc_body, text="C", height=2, width=10, relief=RAISED, bg="yellow",command = clear)
button_clear.place(y=100, x=20)

button_back=Button(calc_body, text="<---", height=2, width=10, relief=RAISED, bg="yellow", command = backspace)
button_back.place(y=100, x=140)

#Taking inputs from keyboard


#number buttons
button_seven=Button(calc_body, text="7", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(7))
button_seven.place(y=160, x=20)
button_eight=Button(calc_body, text="8", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(8))
button_eight.place(y=160, x=140)
button_nine=Button(calc_body, text="9", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(9))
button_nine.place(y=160, x=260)

button_four=Button(calc_body, text="4", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(4))
button_four.place(y=220, x=20)
button_five=Button(calc_body, text="5", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(5))
button_five.place(y=220, x=140)
button_six=Button(calc_body, text="6", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(6))
button_six.place(y=220, x=260)

button_one=Button(calc_body, text="1", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(1))
button_one.place(y=280, x=20)
button_two=Button(calc_body, text="2", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(2))
button_two.place(y=280, x=140)
button_three=Button(calc_body, text="3", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(3))
button_three.place(y=280, x=260)

button_zero=Button(calc_body, text="0", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(0))
button_zero.place(y=340, x=20)
button_double_zero=Button(calc_body, text="00", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click(00))
button_double_zero.place(y=340, x=140)
button_dot=Button(calc_body, text=".", height=2, width=10, relief=GROOVE, bg="white",command=lambda: click('.'))
button_dot.place(y=340, x=260)

#Special operations buttons
button_percentage=Button(calc_body, text="%", height=2, width=10, relief=GROOVE, bg="white")
button_percentage.bind("<Button-1>", special)
button_percentage.place(y=407, x=20)

button_squareroot=Button(calc_body, text="SQRT", height=2, width=10, relief=GROOVE, bg="white")
button_squareroot.bind("<Button-1>",special)
button_squareroot.place(y=407, x=140)

#Equal-to button
button_equals=Button(calc_body, text="=", height=2, width=10, relief=RAISED, bg="#ff4d4d", command = equals)
button_equals.place(y=407, x=260)

#Mathimatical operation buttons
button_division=Button(calc_body, text="/", height=2, width=5, relief=GROOVE, bg="blue",command=lambda: click('/'))
button_division.place(y=160, x=400)
button_multiply=Button(calc_body, text="X", height=2, width=5, relief=GROOVE, bg="blue",command=lambda: click('*'))
button_multiply.place(y=220, x=400)
button_subtract=Button(calc_body, text="-", height=2, width=5, relief=GROOVE, bg="blue",command=lambda: click('-'))
button_subtract.place(y=280, x=400)
button_addition=Button(calc_body, text="+", height=6, width=5, relief=GROOVE, bg="blue",command=lambda: click('+'))
button_addition.place(y=340, x=400)

calc_body.mainloop()

