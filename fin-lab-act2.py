import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger

xgeo = 400
ygeo = 320
items = []
placeholder = 0
ask_amount = False
delitems = False
destroyroot2 = False

dict = {"PENCIL P":"15.00", "PEN":"25.00", "YELLOW PAD":"2.00", "BONDPAPER":"1.00", "COLOR":"45.50"}

root = tk.Tk()
root.title("Cashier")
root.geometry(f"{xgeo}x{ygeo}")
root.resizable(width=False, height=False)

lbl1 = tk.Label(root, text="Please Enter The Item Name Below:").grid(row=0,column=0, padx= 5, pady=5)
lbl2 = tk.Label(root, text="Enter Item Name:").grid(row=1, column=0, padx= 1, pady=1)
lst = tk.Listbox(root, width=20)
lst.grid(row=4, column=0, padx=5, pady=30)

for item in items:
    lst.insert(tk.END, item)

def cancel():
        global askamount
        askamount = False
        print("canceled")

def reset():
    global destroyroot2
    global items
    lst.delete(0, END)
    print(items)
    lbl4["text"] = 0
    lbl6["text"] = 0
    lbl8["text"] = 0
    for item in range(len(items)):
         items.pop(item)
    print(items)
    destroyroot2 = True
     
def ask_amountv2():
    global askamount
    
    while askamount:
        global destroyroot2
        while destroyroot2:
             root2.destroy()
             destroyroot2 = False
             return destroyroot2
        def cancel2():
             root2.destroy()
        def schange():
             def destroy():
                  lbl10.destroy()
                  lbl9.destroy()
                  btn_3.destroy()
                  reset()
             askint = float(ent_2.get())
             value3 = float(lbl8["text"])
             change_due = askint - value3 
             lbl9 = tk.Label(root, text="Change due:")
             lbl9.place(x=200, y=215)
             lbl10 = tk.Label(root, text="0")
             lbl10.place(x=200, y= 235)
             value = float(lbl10["text"])
             lbl10["text"] = format(value + change_due, ".2f")
             btn_3 = tk.Button(root, text="Done", command=destroy)
             btn_3.place(x=200, y=255)
        def enter():
             schange()
             root2.destroy()
        xgeo2 = 200
        ygeo2 = 100
        root2 = tk.Tk()
        root2.title("Chkt")
        root2.geometry(f"{xgeo2}x{ygeo2}")
        root2.resizable(width=False, height=False)
        lbl = tk.Label(root2, text="Enter Amount Given:")
        ent_2 = tk.Entry(root2)
        lbl.pack(padx=5, pady=5)
        ent_2.pack(padx=5, pady=5)
        btn = tk.Button(root2, text="Enter", command= enter)
        btn_2 = tk.Button(root2, text="Cancel", command= cancel2)
        btn.place(x=30, y=60, width=60)
        btn_2.place(x=110, y=60, width=60)

        root2.mainloop()
    print("stopped")



def ask_amount1():
    global askamount
    askamount = True
    ask_amountv2()
    askint = askinteger("Input", "Enter Amount Given:")
    value3 = float(lbl8["text"])
    change_due = askint - value3 
    lbl9 = tk.Label(root, text="Change due:")
    lbl9.place(x=200, y=215)
    lbl10 = tk.Label(root, text="0")
    lbl10.place(x=200, y= 235)
    value = float(lbl10["text"])
    lbl10["text"] = f"{format(value + change_due)}"
    return ask_amount
    

def add_item():
    global items
    item = ent.get()
    price = float(dict[str.upper(item)])
    toshow = f"{str.upper(item)} {price}"
    value = float(lbl4["text"])
    value2 = float(lbl6["text"])
    value3 = float(lbl8["text"])
    print(lbl4["text"], lbl6["text"],lbl8["text"])
    lbl4["text"] = format(value + price, ".2f")
    value2 = 0
    lbl6["text"] = format(value2 + (float(lbl4["text"]) * 0.1), ".2f")
    lbl8["text"] = format(float(lbl6["text"]) + float(lbl4["text"]), ".2f")
    print(lbl4["text"], lbl6["text"],lbl8["text"])
    items.append(item)
    print(items)
    lst.insert(tk.END, toshow)
    placeholder = lbl8["text"]
    return placeholder

def remove_item():
    global items
    selected_item = lst.curselection()
    print(selected_item)
    item = ent.get()
    price = float(dict[str.upper(item)])
    selected_price = float(dict[str.upper(items[selected_item[0]])])
    value = float(lbl4["text"])
    value2 = float(lbl6["text"])
    value3 = float(lbl8["text"])
    lbl4["text"] = format(value - selected_price,".2f")
    print(value2)
    print(len(items))
    lbl6["text"] = format(value2 - (selected_price * 0.1),".2f")
    print(value, value2, value3)
    lbl8["text"] = format(value3 - (selected_price + (selected_price * .1)), ".2f")
    if selected_item:
        index = int(selected_item[0])
        lst.delete(index)
        items.pop(index)
    print(items)
    placeholder = lbl8["text"]
    return placeholder

def gateway():
     check = str.upper(ent.get())
     if check in dict:
          add_item()
     else:
          xgeo3 = 200
          ygeo3 = 100
          root3 = tk.Tk()
          root3.title("Chkt")
          root3.geometry(f"{xgeo3}x{ygeo3}")
          root3.resizable(width=False, height=False)
          lbl = tk.Label(root3,text="No Item Found").pack(padx=5, pady=5)
          

ent = tk.Entry(root)
ent.grid(row=2, column=0, padx= 5, pady=5)
btn1 = tk.Button(root, text="Submit", command=gateway).place(x=40,y=83)
btn2 = tk.Button(root, text="Remove", command=remove_item).place(x=100,y=83)
lbl3 = tk.Label(root, text="Subtotal:").place(x=200,y=55)
lbl4 = tk.Label(root, text="0")
lbl4.place(x=200,y=75)
lbl5 = tk.Label(root, text="Tax (10%):").place(x=200,y=95)
lbl6 = tk.Label(root, text="0")
lbl6.place(x=200,y=115)
lbl7 = tk.Label(root, text="TOTAL:").place(x=200, y=135)
lbl8 = tk.Label(root, text="0")
lbl8.place(x=200, y=155)
btn3 = tk.Button(root, text="Checkout", command=ask_amount1).place(x=200, y=185)


root.mainloop()
