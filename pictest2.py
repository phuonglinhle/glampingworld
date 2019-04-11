from tkinter import *
root = Tk()
photo = PhotoImage(file="P:\Python\GWlogo.gif") # specify the path to your file
label = Label(root, image=photo)  #put the image in a label to disdaply it in the window
label.pack()  # show the label on the screen
root.mainloop() # Create an event loop to display the window