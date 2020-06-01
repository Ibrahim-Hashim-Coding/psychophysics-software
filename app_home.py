# Import necessary libraries
from tkinter import *  # gui tool
from PIL import Image, ImageTk


# Create functions for commands 
def donothing():
   x = 0


# Create window, define window size, title and disallow resizing
window = Tk()
window.title("DeWeerd Lab PsychoPhysics Software")
window.geometry("1200x600")  # You want the size of the app to be 500x500
window.resizable(0, 0)   #Don't allow resizing in the x or y direction

# Set image background
image = Image.open('images\logo.png')
tkpi = ImageTk.PhotoImage(image)        
label_image = Label(window, image=tkpi)
label_image.place(x=0, y=35)


# Create menubar object
menubar = Menu(window)

# Staircases
staircase_menu = Menu(menubar, tearoff=0)
staircase_menu.add_command(label="Create Parameter File", command=donothing)
staircase_menu.add_command(label="Edit Parameter File", command=donothing)
staircase_menu.add_command(label="Run Full Staircase", command=donothing)
staircase_menu.add_command(label="Run 1 Trial", command=donothing)

staircase_menu.add_separator()
staircase_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Staircase Options", menu=staircase_menu)

# Stimuli
stimuli_menu = Menu(menubar, tearoff=0)
stimuli_menu.add_command(label="Gabor Patch", command=donothing)
stimuli_menu.add_command(label="Fixation Cross/Circle", command=donothing)
stimuli_menu.add_separator()
stimuli_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Stimuli Testing", menu=stimuli_menu)


window.config(menu=menubar)
window.mainloop()
