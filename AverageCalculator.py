import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import datetime
import pyperclip
import subprocess
import sys

def main():
    # Run your main script without showing the console window
    subprocess.Popen([sys.executable, "your_main_script.py"], shell=True, creationflags=subprocess.DETACHED_PROCESS)

if __name__ == "__main__":
    main()

#Creates a list to keep track of inputs
inputs = []
ver = "1.3"
#Creating the main window and theming it
main_window = ThemedTk(theme = "equilux")
main_window.configure(bg="grey28")



#Function gets the number from the entry, makes sure it is a number, then appends it to a list then averages it
def get_av(event=None):
    global inputs
    global output
    console_output.set(" ")
    try:
        user_input = int((entry.get()).replace(" ", ""))
        user_input = float(user_input)
        preinputs = list(entry.get().split(" "))
        no_str = [item for item in preinputs if item != ""]
        temp_list = [int(x) for x in no_str]
        inputs.extend(temp_list)
        output.set("Average: " + str(float(sum(inputs)/len(inputs))))

    except ValueError:
        popup("Type a number")
    entry.delete(0, tk.END)
    
    
    #output.set("Average: " + str(float(sum(inputs)/len(inputs))))

#Function saves the average to the text file and displays the current time and date
def text_file():
    global inputs
    now = datetime.now()
    console_output.set(" ")
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
        popup("Input Averages")

#Function clears the inputs and averages
def clear_avg():
    global inputs
    console_output.set(" ")
    inputs = []
    output.set("Average: ")

def copy_av():
    global main_window
    try:
        copy_clip = str(sum(inputs)/len(inputs))
        pyperclip.copy(copy_clip)
        console_output.set("Copied")
        
    except ZeroDivisionError:
        popup("Input Averages")

#function to manage popups
def popup(stuffs):
    popup = ThemedTk(theme = "equilux")
    popup.configure(bg="grey28")
    popup.title("Notification")
    label = tk.Label(popup, text=stuffs)
    label.pack(pady=10)
    ok_button = tk.Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()

#function that controls the output at the bottom
def output_text(stuffs):
    global console_output
    console_output.set(stuffs)




#Initalizing output variables used in 'Average' text
output = tk.StringVar()
output.set("Average: ")

console_output = tk.StringVar()
console_output.set(" ")




#Labels and entries
av_lab = ttk.Label(main_window, text="Average Calculator", font=('Segoe UI', 18))
ver_lab = ttk.Label(main_window, text="Ver: " + ver, font=('Segoe UI', 10))
entry = ttk.Entry(main_window, width=30)
average_label = ttk.Label(main_window, textvariable=output)

av_lab.grid(row=0, column = 0, columnspan = 2, pady = 3)
ver_lab.grid(row = 1, column = 0, columnspan = 2, pady = 3)
entry.grid(row = 2, column = 0, columnspan = 2, pady = 3)
average_label.grid(row = 3, column = 0, pady = 3, columnspan = 2)

entry.bind("<Return>", get_av)

#Buttons on row 5
total_but = ttk.Button(main_window, text="Calculate Average", command=get_av)
clear_but = ttk.Button(main_window, text="Clear Averages", command=clear_avg)

total_but.grid(row = 5, column = 0, pady = 3, sticky = "E")
clear_but.grid(row = 5, column = 1, pady = 3, sticky = "W")


#buttons on row 6
txt_but = ttk.Button(main_window, text="Add Averages to .txt File", command=text_file)
copy_but = ttk.Button(main_window, text="Copy Averages to Clipboard", command=copy_av)

txt_but.grid(row = 6, column = 0, pady = 3, sticky = "E")
copy_but.grid(row = 6, column = 1, pady = 3, sticky = "W")


#label for notificatoins
console = ttk.Label(main_window, textvariable= console_output)
console.grid(row=7, column = 0, columnspan = 2)

main_window.resizable(False, False)
main_window.title("Average Calculator")    
main_window.mainloop()