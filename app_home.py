# Import necessary libraries
from tkinter import *  # gui tool
from PIL import Image, ImageTk
from datetime import datetime
import os

# Dictionaries
parameter_types = {'staircase': '.parsta'}


# Create functions for commands 
def donothing():
   x = 0


def get_inputs(requested, received, labels_stored, parameter_type, file_name):
    
    now = datetime.now() # current date and time
    date_time = now.strftime("_%d_%m_%Y_%H_%M")

    f = open(file_name + date_time + parameter_types[parameter_type], "w")

    for idx, value in enumerate(received):
        f.write(requested[idx] + "\t\t\t")
        f.write(value.get() + "\n")
    
    f.close()
    for widget in window.winfo_children():
        widget.grid_forget()

    
    label_image.pack()

   
def create_form(labels):
    label_image.pack_forget()
    
    labels_stored = []
    entries = []
    for i in range(len(labels)):
        label = Label(window, text=labels[i])
        label.grid(row=i)
        labels_stored.append(label)
        entry = Entry(window)
        entry.grid(row=i, column=1)
        entries.append(entry)
        
    button1=Button(window, text="Submit", command=lambda: get_inputs(labels, entries, labels_stored, 'staircase', 'test'))
    button1.grid(row=i+1, column=1)
    
    
# Create window, define window size, title and disallow resizing
window = Tk()
window.title("DeWeerd Lab PsychoPhysics Software")
window.geometry("1200x600")  #  You want the size of the app to be this size
window.resizable(0, 0)   #  Don't allow resizing in the x or y direction

# Set background image
image = Image.open('images\logo.png')
tkpi = ImageTk.PhotoImage(image)        
label_image = Label(window, image=tkpi)
label_image.pack()

# Create menubar object
menubar = Menu(window)

# Create section of menu dealing with staircases
staircase_menu = Menu(menubar, tearoff=0)
staircase_menu.add_command(label="Create Parameter File",
                            command=lambda labels = ['1', '2', '3']: create_form(labels))
staircase_menu.add_command(label="Edit Parameter File", command=donothing)
staircase_menu.add_command(label="Run Full Staircase", command=donothing)
staircase_menu.add_command(label="Run 1 Trial", command=donothing)

staircase_menu.add_separator()
staircase_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Staircase Options", menu=staircase_menu)

# Create section of menu dealing with stimuli
stimuli_menu = Menu(menubar, tearoff=0)
stimuli_menu.add_command(label="Gabor Patch", command=donothing)
stimuli_menu.add_command(label="Fixation Cross", command=donothing)
stimuli_menu.add_command(label="Fixation Circle", command=donothing)
menubar.add_cascade(label="Stimuli Testing", menu=stimuli_menu)

# Run
window.config(menu=menubar)
window.mainloop()
