# import tkinter as tk - This imports the tkinter library and gives it the alias 'tk' for easier access to its functions and classes.

# Widgets - GUI elements like buttons, labels, text boxes
# Windows - Main container for the application
# Label - A widget used to display text or images
# Button - A widget that can be clicked to perform an action
# Geometry - The size and position of the window

# tk.photoImage - A class used to handle image files in tkinter, use a variable before it to display images
# call that variable by putting window.iconphoto(True, variable_name) to set the window icon

#//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------//#

import tkinter as tk # you have to use 'tk.' prefix to access tkinter functions

#//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------//#

window = tk.Tk() # Create the main window
# window.geometry("500x500") # Set the size of the window
window.title("Weather Dashboard") # Set the title of the window which is on the top left corner

#//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------//#

def buttonclicked():
    print("You Clicked the button!")

Icon = tk.PhotoImage(file='IMG_4510.png') # Load an icon image from a file, file has to be in the same directory as this script
window.iconphoto(True, Icon) # Set the window icon

Button = tk.Button(window, 
                 text="Hello! This is my GUI in Python!", 
                 font=('Arial', 34, 'bold'), 
                 fg='black', 
                 bg='orange',
                 command=buttonclicked) # Create a button widget with some text and styling
# Create a label widget with some text and styling
# font = (font family, size, type) /// fg = foreground color (text color) /// bg = background color

Button.pack() # Add the button to the window and make it visible /// and if we want to put it in a specific position we can use .place(x= , y= ) instead of .pack()
#//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------//#

window.mainloop() # Start the main event loop to run the application and widget and etc have to be created before this line 

#//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------//#
