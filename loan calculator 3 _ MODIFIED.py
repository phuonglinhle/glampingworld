from tkinter import * # Import tkinter
from PIL import Image, ImageTk

class PhoneOrder:
    
    def __init__(self):
        window = Tk() # Create a window
        
        #I'll worry about this later
        # Listbox(window, selectmode='single').insert(1, "Python")

        #Create Background
        window.img=Image.open('C:\\Users\\impli\\OneDrive\\Desktop\\python\\1.png')
        background=ImageTk.PhotoImage(window.img)
        label = Label(window, image=background).place(x=0,y=0, relwidth=1,relheight=1)

        #Insert logo
        window.img=Image.open('C:\\Users\\impli\\OneDrive\\Desktop\\python\\logo.jpg')
        logo=ImageTk.PhotoImage(window.img)
        label = Label(window, image=logo).grid(row=0,column=5,sticky=E)

        window.title("Phone Order Application") # Set title of a window
        Label(window, text = "\nCUSTOMER INFORMATION\n", bg='#9EE9AB',fg='blue').grid(row = 0, column = 2, sticky = W)
        
        #radio buttons for new/returning customer
        Radiobutton(window, text='New customer',bg='#9EE9AB', value = 1).grid(row=0, column=3, sticky=W)
        Radiobutton(window, text='Returning customer',bg='#9EE9AB', value = 2).grid(row=0, column=4, sticky=W)
        #set up labels for the app in the left column of the window, align labels left (Sticky=W)
               
        Label(window, text = "Customer's Email", bg='#9EE9AB').grid(row = 1, column = 1, sticky = W)
        Label(window, text = "First Name", bg='#9EE9AB').grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Last Name", bg='#9EE9AB').grid(row = 2, column = 3, sticky = W)
        Label(window, text = "Phone Number", bg='#9EE9AB').grid(row = 1, column = 3, sticky = W)
        Label(window, text = "\nADD PRODUCT\n", bg='#9EE9AB', fg='blue').grid(row = 3, column = 2, sticky = W)        
        Label(window, text = "Item Name", bg='#9EE9AB').grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Item Quantity", bg='#9EE9AB').grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Item Price", bg='#9EE9AB').grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Item Total", bg='#9EE9AB').grid(row = 7, column = 1, sticky = W)
        Button(window, text = "Add to Cart", bg = 'yellow', fg = 'blue').grid(row = 6, column = 3, sticky = W)

        #Button not working.
        
        #Frame(window, bg='blue').place(relx=0.5, rely=0,relwidth=0,relheight=5,anchor='n')

        Label(window, text = "\nADD SHIPPING INFORMATION\n",bg='#9EE9AB',fg='blue').grid(row = 8, column = 2, sticky = W)        
        Label(window, text = "Street", bg='#9EE9AB').grid(row = 9, column = 1, sticky = W)
        Label(window, text = "City", bg='#9EE9AB').grid(row = 10, column = 1, sticky = W)
        Label(window, text = "State", bg='#9EE9AB').grid(row = 11, column = 1, sticky = W)
        Label(window, text = "Postal Code", bg='#9EE9AB').grid(row = 12, column = 1, sticky = W)

        Label(window, text = "\nADD BILLING INFORMATION\n",bg='#9EE9AB', fg='blue').grid(row = 8, column = 4, sticky = W)        
        Label(window, text = "Street", bg='#9EE9AB').grid(row = 9, column = 3, sticky = W)
        Label(window, text = "City", bg='#9EE9AB').grid(row = 10, column = 3, sticky = W)
        Label(window, text = "State", bg='#9EE9AB').grid(row = 11, column = 3, sticky = W)
        Label(window, text = "Postal Code", bg='#9EE9AB').grid(row = 12, column = 3, sticky = W)
        Label(window, text = "Name on Card", bg='#9EE9AB').grid(row = 13, column = 3, sticky = W)
        Label(window, text = "Card Number", bg='#9EE9AB').grid(row = 14, column = 3, sticky = W)
        Label(window, text = "Expiration Date", bg='#9EE9AB').grid(row = 15, column = 3, sticky = W)
        Label(window, text = "Security Code", bg='#9EE9AB').grid(row = 16, column = 3, sticky = W)

        

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
        
        
        #input for Shipping
        self.shipstreet = StringVar()
        Entry(window, textvariable = self.shipstreet, justify = RIGHT).grid(row = 9, column = 2)
        self.shipcity = StringVar()
        Entry(window, textvariable = self.shipcity,justify = RIGHT).grid(row = 10, column = 2)
        self.shipstate = StringVar()
        Entry(window, textvariable = self.shipstate, justify = RIGHT).grid(row = 11, column = 2)
        self.shipcode = StringVar()
        Entry(window, textvariable = self.shipcode, justify = RIGHT).grid(row = 12, column = 2)
        
        #input for billing
        self.billstreet = StringVar()
        Entry(window, textvariable = self.billstreet, justify = RIGHT).grid(row = 9, column = 4)
        self.billcity = StringVar()
        Entry(window, textvariable = self.billcity,justify = RIGHT).grid(row = 10, column = 4)
        self.billstate = StringVar()
        Entry(window, textvariable = self.billstate, justify = RIGHT).grid(row = 11, column = 4)
        self.billcode = StringVar()
        Entry(window, textvariable = self.billcode, justify = RIGHT).grid(row = 12, column = 4)
        self.billname = StringVar()
        Entry(window, textvariable = self.billname, justify = RIGHT).grid(row = 13, column = 4)
        self.billnumber = StringVar()
        Entry(window, textvariable = self.billnumber,justify = RIGHT).grid(row = 14, column = 4)
        self.billexp = StringVar()
        Entry(window, textvariable = self.billexp, justify = RIGHT).grid(row = 15, column = 4)
        self.billseccode = StringVar()
        Entry(window, textvariable = self.billseccode, justify = RIGHT).grid(row = 16, column = 4)


        
        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        #FIXME
        Button(window, text = "Calculate Total", bg = 'blue', fg = 'white').grid(row = 7, column = 3, sticky = W)
        
        window.mainloop() # Create an event loop to display the window
        
        #calculate Monthly Payment using  the formula provided    
    def carttotal(self, itemprice, itemquant):
        itemtotal = itemquant * itemprice
        self.itemtotal.set(format(itemtotal, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
        return itemtotal


PhoneOrder()  # Create GUI 
