from tkinter import * # Import tkinter
    
class PhoneOrder:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Phone Order Application") # Set title of a window
        
        #set up labels for the loan calculator in the left column of the window, align labels left (Sticky=W)
        Label(window, text = "Customer's Email").grid(row = 1, column = 1, sticky = W)
        Label(window, text = "First Name").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Last Name").grid(row = 2, column = 3, sticky = W)
        Label(window, text = "Phone Number").grid(row = 1, column = 3, sticky = W)
        Label(window, text = "\nADD PRODUCT\n").grid(row = 3, column = 2, sticky = W)        
        Label(window, text = "Item Name").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Item Quantity").grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Item Price").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Item Total").grid(row = 7, column = 1, sticky = W)

        # set up the input area for the calculator in the right column, using Entry for textboxes and assigning the values entered to variables
        self.email = StringVar()
        Entry(window, textvariable = self.email, justify = RIGHT).grid(row = 1, column = 2)
        self.firstname = StringVar()
        Entry(window, textvariable = self.firstname,justify = RIGHT).grid(row = 2, column = 2)
        self.lastname = StringVar()
        Entry(window, textvariable = self.lastname, justify = RIGHT).grid(row = 2, column = 4)
        self.phone = StringVar()
        Entry(window, textvariable = self.phone, justify = RIGHT).grid(row = 1, column = 4)
        self.itemname = StringVar()
        Entry(window, textvariable = self.itemname, justify = RIGHT).grid(row = 4, column = 2)
        self.itemquant = IntVar()
        Entry(window, textvariable = self.itemquant, justify = RIGHT).grid(row = 5, column = 2)
        self.itemprice = IntVar()
        Entry(window, textvariable = self.itemprice, justify = RIGHT).grid(row = 6, column = 2)
        
        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        self.itemtotal = StringVar()
        Label(window, textvariable = self.itemtotal).grid(row = 7, column = 2, sticky = E)
        Button(window, text = "Compute Payment", command = self.gettotal).grid(row = 8, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop to display the window
      
    #calculate Monthly Payment using  the formula provided    
    def gettotal(self, itemprice, itemquant):
        itemtotal = itemquant * itemprice
        self.itemtotal.set(format(itemtotal, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
        return itemtotal

PhoneOrder()  # Create GUI 