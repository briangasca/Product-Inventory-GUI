from tkinter import *
from tkinter import ttk

#to-do: make inventory creator.

#for now, global inventory


class Inventory():

    products = []

    def __init__(self):
        pass

    def add(self, product):
        self.products.append(product)
        for product in self.products:
            print(product.name)
    
    def remove(self, index):
        if(isinstance(index, int)):
            self.products[index] = None
        else:
            for product in self.products:
                if(product == index):
                    self.products.remove(product)
                
        

    def totalValue(self):
        sum = 0
        for i in range(self.products.length):
            sum += self.products[i].price
        return sum
    
    def totalStock(self):
        quantity = 0
        for i in range(self.products.length):
            quantity += self.products[i].stock
    
    def updateStock(self, product):
        global text_box
        for existing_product in self.products:
            if existing_product.name == product.name:
                existing_product.stock += product.stock
                break
        else:
            # If the loop completes without 'break', it means the product is not in the inventory
            self.add(product)

        text_box.delete('1.0', END)
        text_box.insert(END, "Product Name: Price | In-Stock:\n")

        for i in self.products:
            text_box.insert(END, f"{i.name}: ${i.price} | In Stock: {i.stock}\n")

    def clear(self):
        self.products.clear()

        text_box.delete('1.0', END)
        text_box.insert(END, "Product Name: Price | In-Stock:\n")
        

    



class Product():
    #Name, Price, In-Stock Amount, Inventory where it's stored.
    def __init__(self, name, price, stock, inventory):
        self.name = name
        self.price = price
        self.stock = stock
        self.inventory = inventory


GLOBAL_INVENTORY = Inventory()


#get input
        
        
def input_get():
    global input_name
    global input_price
    global input_stock
    global text_box
    global GLOBAL_INVENTORY

    name = input_name.get()

    try:
        price = float(input_price.get())
        stock = int(input_stock.get())
    except:
        text_box.insert( END , "Please use the CORRECT FORMAT (String, int, int)\n")

    # text_box.insert( END, "Generated new Product object!\n")


    new_product = Product(name, price, stock, GLOBAL_INVENTORY)
    GLOBAL_INVENTORY.updateStock(new_product)
    

    return new_product


# tkinter gui

root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()

ttk.Label(frm, text="Inventory Manager").grid(column=2, row=0)
ttk.Label(frm, text=":Inventory:").grid(column=2,row=4)

name_label = ttk.Label(frm, text="Name").grid(column=1, row=1)
price_label = ttk.Label(frm, text="Price").grid(column=2, row=1)
stock_label = ttk.Label(frm, text="Stock").grid(column=3, row=1)

input_name = ttk.Entry(frm, text="Product")
input_price = ttk.Entry(frm, text="Price")
input_stock = ttk.Entry(frm, text="In-Stock")

input_name.grid(column=1, row=2)
input_price.grid(column=2, row=2)
input_stock.grid(column=3, row=2)

ttk.Button(frm, text="Add To Inventory", command=input_get).grid(column=2,row=3)
ttk.Button(frm, text="Clear Inventory", command=GLOBAL_INVENTORY.clear).grid(column=2,row=6)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)

#Inventory box
text_box = Text(frm, height=20, width=50    )
text_box.grid(column=2, row=5)
text_box.insert(END, "Product Name: Price | In-Stock:\n")   


root.mainloop()

