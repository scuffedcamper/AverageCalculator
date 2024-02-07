import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import datetime

#Creates a list to keep track of inputs
inputs = []
ver = "1.1"
#Creating the main window and theming it
main_window = ThemedTk(theme = "equilux")
main_window.configure(bg="grey28")


#Function gets the number from the entry, makes sure it is a number, then appends it to a list then averages it
def get_text():
    global inputs
    global output
    try:
        user_input = float(entry.get())
        inputs.append(user_input)
    except ValueError:
        temp_win = tk.Toplevel()
        temp_text = tk.Label(temp_win, text="Not a Number")
        temp_text.pack(pady=10)
    
    output.set("Average: " + str(float(sum(inputs)/len(inputs))))

#Function saves the average to the text file and displays the current time and date
def text_file():
    global inputs
    now = datetime.now()
    try:
        if sum(inputs)/len(inputs) != 0:
            try:
                output_file = open("averages.txt", "x")
                output_file.write("Average at " + str(now) + ": " + str(sum(inputs)/len(inputs)) + "\n")
                output_file.close()
            except FileExistsError:
                output_file = open("averages.txt", "a")
                output_file.write("Average at " + str(now) + ": " + str(sum(inputs)/len(inputs)) + "\n")
                output_file.close()
    except ZeroDivisionError:
        temp_win2 = tk.Toplevel()
        temp_text = tk.Label(temp_win2, text="Input averages").pack(pady=3)

#Function clears the inputs and averages
def clear_avg():
    global inputs
    inputs = []
    output.set("Average: ")


#Initalizing output variables used in 'Average' text
output = tk.StringVar()
output.set("Average: ")



#Adds the label, entry, buttons, and titles the window
ttk.Label(main_window, text="Average Calculator", font=('Segoe UI', 18)).pack()
ttk.Label(main_window, text="Ver: " + ver, font=('Segoe UI', 10)).pack()
entry = ttk.Entry(main_window, width=30)
entry.pack(pady=10)

ttk.Button(main_window, text="Calculate total", command=get_text).pack(pady=3)

average_label = ttk.Label(main_window, textvariable=output)
average_label.pack(pady=10)
ttk.Button(main_window, text="Clear averages", command=clear_avg).pack(pady=3)

ttk.Button(main_window, text="Add averages to .txt file", command=text_file).pack(pady=3)



main_window.title("Average Calculator")




        
main_window.mainloop()