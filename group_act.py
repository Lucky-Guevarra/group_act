import tkinter as tk
from tkinter import ttk
from datetime import datetime

def show_calendar():
    year = int(year_entry.get())
    month = month_var.get()


    month_number = datetime.strptime(month, "%B").month


    first_day_of_month = datetime(year, month_number, 1).weekday()


    days_in_month = [
        0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]


    if month_number == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29


    window = tk.Toplevel(root)
    window.title(f"Calendar - {month} {year}")


    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for col, day in enumerate(days_of_week):
        ttk.Label(window, text=day).grid(row=0, column=col, padx=5, pady=5)


    row = 1
    day = 1

    for i in range(6):  
        for j in range(7):  
            if i == 0 and j < first_day_of_month:
                ttk.Label(window, text="").grid(row=row, column=j, padx=5, pady=5)
            elif day <= days_in_month[month_number]:
                ttk.Label(window, text=str(day)).grid(row=row, column=j, padx=5, pady=5)
                day += 1
            else:
                break
        row += 1


root = tk.Tk()
root.title("Calendar Viewer")


ttk.Label(root, text="Enter Year:").grid(row=0, column=0, padx=5, pady=5)
year_entry = ttk.Entry(root)
year_entry.grid(row=0, column=1, padx=5, pady=5)


ttk.Label(root, text="Select Month:").grid(row=1, column=0, padx=5, pady=5)
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
month_var = tk.StringVar(value=months[0])
month_dropdown = ttk.Combobox(root, textvariable=month_var, values=months)
month_dropdown.grid(row=1, column=1, padx=5, pady=5)

show_button = ttk.Button(root, text="Show Calendar", command=show_calendar)
show_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
