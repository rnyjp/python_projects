from tkinter import *
from tkinter import ttk
import bs4
import requests
from bs4 import BeautifulSoup

window = Tk()
window.geometry("500x300")
window.title("RO-Share")
window.resizable(0, 0)

ttk.Label(window, text="RO-Share",
          background='', foreground="black",
          font=("Times New Roman", 20)).place(x=205,y=10)

# label
ttk.Label(window, text="Select the Company :",
          font=("Times New Roman", 12)).place(x=50,y=100)

ttk.Label(window, text="Price",
          font=("Times New Roman", 12)).place(x=150,y=173)

price_value = StringVar()
price_value.set("0")

price_display = Entry(window, bg='white',textvariable = price_value,justify="left",font=('arial', 13, 'bold'))
#price_display.configure(state='disabled')
price_display.place(x=200,y=170)

# Iniating steps to fetch data from internet

url_burger = requests.get('https://www.moneycontrol.com/india/stockpricequote/consumerfood/burgerkingindia/BKI01')
url_jet = requests.get('https://www.moneycontrol.com/india/stockpricequote/transportlogistics/jetairways/JA01')

data_burger = bs4.BeautifulSoup(url_burger.text, "html5lib")
data_jet = bs4.BeautifulSoup(url_jet.text, "html5lib")

price_burger = data_burger.find("div", {"id": "nsecp"}).get_text()
price_jet = data_jet.find("div", {"id": "nsecp"}).get_text()


def selected(event):

    capture = str(company_choosen.get())

    # Checking with company name
    if capture == 'Burger King India Ltd.':
        print("Share price of Burger King :" + price_burger)
        price_value.set("₹ "+ price_burger)

    if capture == 'Jet Airways Ltd.':
        print("Share price of Jet Airways :" + price_jet)
        price_value.set("₹ "+ price_jet)

    if capture == 'SELECT':
        print("NILL")
        price_value.set(" ")



# Combobox creation
n = StringVar()
company_choosen = ttk.Combobox(window, width=27, justify= LEFT, textvariable=n)       # Adding combobox drop down list
company_choosen['values'] = ('SELECT',
                          'Burger King India Ltd.',
                          'Jet Airways Ltd.')

company_choosen['state'] = 'readonly'  #Set the 'state' property to 'readonly' to prevent users from entering custom values.

company_choosen.place(x=200,y=100)
company_choosen.current(0)              # To display default value show from list

company_choosen.bind('<<ComboboxSelected>>', selected)

window.mainloop()



