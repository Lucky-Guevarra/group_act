import tkinter as tk
from tkinter import ttk
from tkinter import *

xgeo = 400
ygeo = 320
items = []

dict = {"PENCIL P":"15.00", "PEN":"25.00", "YELLOW PAD":"2.00", "BONDPAPER":"1.00", "COLOR":"45.50"}

root = tk.Tk()
root.title("Cashier")
root.geometry(f"{xgeo}x{ygeo}")
root.resizable(width=False, height=False)

lbl1 = tk.Label(root, text="Please Enter The Item Name Below:").grid(row=0,column=0, padx= 5, pady=5)
lbl2 = tk.Label(root, text="Enter Item Name:").grid(row=1, column=0, padx= 5, pady=5)
lst = tk.Listbox(root, width=20)
lst.grid(row=4, column=0)

for item in items:
    lst.insert(tk.END, item)

def add_item():
    global items
    item = ent.get()
    price = float(dict[str.upper(item)])
    toshow = f"{str.upper(item)} {price}"
    value = float(lbl4["text"])
    value2 = float(lbl6["text"])
    value3 = float(lbl8["text"])
    print(lbl4["text"], lbl6["text"],lbl8["text"])
    lbl4["text"] = f"{value + price}"
    value2 = 0
    lbl6["text"] = f"{value2 + (float(lbl4["text"]) * 0.1)}"
    lbl8["text"] = f"{float(lbl6["text"]) + float(lbl4["text"])}"
    print(lbl4["text"], lbl6["text"],lbl8["text"])
    items.append(item)
    print(items)
    lst.insert(tk.END, toshow)

def remove_item():
    global items
    selected_item = lst.curselection()
    print(selected_item)
    item = ent.get()
    price = float(dict[str.upper(item)])
    selected_price = float(dict[selected_item])
    value = float(lbl4["text"])
    value2 = float(lbl6["text"])
    value3 = float(lbl8["text"])
    lbl4["text"] = f"{value - price}"
    print(value2)
    print(len(items))
    lbl6["text"] = f"{value2 - value2 / float(len(items)) }"
    print(value, value2, value3)
    lbl8["text"] = f"{value3 - (value + value2) / float(len(items))}"
    if selected_item:
        index = int(selected_item[0])
        lst.delete(index)
        items.pop(index)
    print(items)
ent = tk.Entry(root, textvariable="Enter Item Here")
ent.grid(row=2, column=0, padx= 30, pady=30)
btn1 = tk.Button(root, text="Submit", command=add_item).place(x=40,y=113)
btn2 = tk.Button(root, text="Remove", command=remove_item).place(x=100,y=113)
lbl3 = tk.Label(root, text="Subtotal:").place(x=200,y=55)
lbl4 = tk.Label(root, text="0")
lbl4.place(x=200,y=75)
lbl5 = tk.Label(root, text="Tax (10%):").place(x=200,y=95)
lbl6 = tk.Label(root, text="0")
lbl6.place(x=200,y=115)
lbl7 = tk.Label(root, text="TOTAL:").place(x=200, y=135)
lbl8 = tk.Label(root, text="0")
lbl8.place(x=200, y=155)
btn3 = tk.Button(root, text="Checkout").place(x=200, y=185)



root.mainloop()
