from tkinter import *
from tkinter import ttk

class Inventory():

    products = []

    def __init__(self, products):
        self.products = products

    def add(self, product):
        self.products.append(product)
    
    def remove(self, index):
        self.products[index] = None

    def totalValue(self):
        sum = 0
        for i in range(self.products.length):
            sum += self.products[i].price
        return sum
    
    def totalStock(self):
        quantity = 0
        for i in range(self.products.length):
            quantity += self.products[i].stock
    



class Product():
    def __init__(self, name, price, stock):
        self.id = name
        self.price = price
        self.stock = stock

#get input
        
def input_get():
    global input_name
    global input_price
    global input_stock
    global text_box

    name = input_name.get()
    price = input_price.get()
    stock = input_stock.get()

    if(type(name) != 'str' or type(price) != 'int' or type(stock) != 'int'):
        text_box.insert( END , "Please use the CORRECT FORMAT (String, int, int)")
        return

    text_box.insert( END, "Generated new Product object!")

    return Product(name, price, stock)


# tkinter gui

root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()

ttk.Label(frm, text="Add products").grid(column=2, row=0)

name_label = ttk.Label(frm, text="Name").grid(column=1, row=1)
price_label = ttk.Label(frm, text="Price").grid(column=2, row=1)
stock_label = ttk.Label(frm, text="Stock").grid(column=3, row=1)

input_name = ttk.Entry(frm, text="Product")
input_price = ttk.Entry(frm, text="Price")
input_stock = ttk.Entry(frm, text="Stock")

input_name.grid(column=1, row=2)
input_price.grid(column=2, row=2)
input_stock.grid(column=3, row=2)

ttk.Button(frm, text="Enter", command=input_get).grid(column=2,row=3)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)

text_box = Text(frm, height=20, width=50)
text_box.grid(column=2, row=4)

root.mainloop()

