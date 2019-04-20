from tkinter import * # Import tkinter
from PIL import Image, ImageTk

class PhoneOrder:
    
    def carttotal(self):
        self.itemtotal = self.itemquant.get() * self.itemprice.get()
        self.itemtotalVar.set(format(self.itemtotal,'10.2f'))
        
    def __init__(self):
        window = Tk() # Create a window

        window.geometry('900x530')

        #Create Background
        
        Label(window, bg='#9EE9AB').place(x=0,y=0, relwidth=1,relheight=1)

        #Insert logo
        window.img=Image.open('C:\\Users\\impli\\OneDrive\\Desktop\\python\\logo.jpg')
        logo=ImageTk.PhotoImage(window.img)
        Label(window, image=logo).place(relx=0.85, rely=0.2, anchor=S)

        window.title("Phone Order Application") # Set title of a window
        Label(window, text = "\nCUSTOMER INFORMATION\n", font=('georgia',10, 'bold'), bg='#9EE9AB',fg='#008B8B').grid(row = 0, column = 2, sticky = W)
        
        #radio buttons for new/returning customer
        Radiobutton(window, text='New customer', font=('georgia',9), bg='#9EE9AB', value = 1).grid(row=0, column=3, sticky=W)
        Radiobutton(window, text='Returning customer', font=('georgia',9), bg='#9EE9AB', value = 2).grid(row=0, column=4, sticky=W)
        
        #set up labels for the app in the left column of the window, align labels left (Sticky=W)     
        Label(window, text = "Email", font=('georgia',9), bg='#9EE9AB').grid(row = 1, column = 1, sticky = W)
        Label(window, text = "First Name", font=('georgia',9), bg='#9EE9AB').grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Last Name", font=('georgia',9), bg='#9EE9AB').grid(row = 2, column = 3, sticky = W)
        Label(window, text = "Phone Number", font=('georgia',9), bg='#9EE9AB').grid(row = 1, column = 3, sticky = W)

        Label(window, text = "\nADD PRODUCT\n", font=('georgia',10, 'bold'), bg='#9EE9AB', fg='#008B8B').grid(row = 3, column = 2, sticky = W)        
        Label(window, text = "Item Name", font=('georgia',9), bg='#9EE9AB').grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Quantity", font=('georgia',9), bg='#9EE9AB').grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Item Price", font=('georgia',9), bg='#9EE9AB').grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Item Total", font=('georgia',9), bg='#9EE9AB').grid(row = 7, column = 1, sticky = W)

        #Add Info
        Label(window, text = "\nSHIPPING INFORMATION\n", font=('georgia',10, 'bold'), bg='#9EE9AB',fg='#008B8B').grid(row = 8, column = 2, sticky = W)        
        Label(window, text = "Street", font=('georgia',9), bg='#9EE9AB').grid(row = 9, column = 1, sticky = W)
        Label(window, text = "City", font=('georgia',9), bg='#9EE9AB').grid(row = 10, column = 1, sticky = W)
        Label(window, text = "State", font=('georgia',9), bg='#9EE9AB').grid(row = 11, column = 1, sticky = W)
        Label(window, text = "Postal Code", font=('georgia',9), bg='#9EE9AB').grid(row = 12, column = 1, sticky = W)

        #Label(window, text = "\nOR\n", font=('georgia',10, 'bold'), bg='#9EE9AB',fg='#008B8B').grid(row = 13, column = 2, sticky = W)        

        Label(window, text = "\nBILLING INFORMATION\n", font=('georgia',10, 'bold'), bg='#9EE9AB', fg='#008B8B').grid(row = 8, column = 4, sticky = W)        
        Label(window, text = "Street", font=('georgia',9), bg='#9EE9AB').grid(row = 9, column = 3, sticky = W)
        Label(window, text = "City", font=('georgia',9), bg='#9EE9AB').grid(row = 10, column = 3, sticky = W)
        Label(window, text = "State", font=('georgia',9), bg='#9EE9AB').grid(row = 11, column = 3, sticky = W)
        Label(window, text = "Postal Code", font=('georgia',9), bg='#9EE9AB').grid(row = 12, column = 3, sticky = W)
        Label(window, text = "Name on Card", font=('georgia',9), bg='#9EE9AB').grid(row = 13, column = 3, sticky = W)
        Label(window, text = "Card Number", font=('georgia',9), bg='#9EE9AB').grid(row = 14, column = 3, sticky = W)
        Label(window, text = "Expiration Date", font=('georgia',9), bg='#9EE9AB').grid(row = 15, column = 3, sticky = W)
        Label(window, text = "Security Code", font=('georgia',9), bg='#9EE9AB').grid(row = 16, column = 3, sticky = W)

        # set up the input area for the calculator in the right column, using Entry for textboxes and assigning the values entered to variables
        self.email = StringVar()
        Entry(window, textvariable = self.email, justify = RIGHT).grid(row = 1, column = 2)
        self.firstname = StringVar()
        Entry(window, textvariable = self.firstname,justify = RIGHT).grid(row = 2, column = 2)
        self.lastname = StringVar()
        Entry(window, textvariable = self.lastname, justify = RIGHT).grid(row = 2, column = 4)
        self.phone = StringVar()
        Entry(window, textvariable = self.phone, justify = RIGHT).grid(row = 1, column = 4)
        #self.itemName = StringVar()
        #Entry(window, textvariable = self.itemName, justify = RIGHT).grid(row = 4, column = 2)
        
        #option menu for item name
        self.itemName = StringVar(window)
        self.itemName.set("") # default value
        itemNameButton=OptionMenu(window,self.itemName,"Tent","Helmet","Bike","Backpack","Sleeping Bag","YETI Cooler")
        itemNameButton.place(x=122,y=140)
        itemNameButton.config(width=13)

        #store all the entry of the itemName
        cartlist=[]
        testing=[]
        
        self.itemquant = IntVar()
        Entry(window, textvariable = self.itemquant, justify = RIGHT).place(x=120,y=170)
        self.itemprice = DoubleVar()
        Entry(window, textvariable = self.itemprice, justify = RIGHT).place(x=120,y=190)

#Add to Cart Button & output the entry
        
        addcartLabel=Label(window, text = "CART SUMMARY", font=('georgia',10, 'bold'), bg='#9EE9AB', fg='#008B8B')
        addcartLabel.place(relx=0.85, rely=0.3, anchor=S)

        def addcart():
            cartlist.append(self.itemName.get())
            addcartLabeloutput.config(text="%s @ $%.2f each x %d = $%s" %(self.itemName.get(), self.itemprice.get(),self.itemquant.get(), self.itemtotal))

        addcartLabeloutput=Label(window, bg='#9EE9AB')
        addcartLabeloutput.place(relx=0.85, rely=0.4, anchor=S)
        addcartButton=Button(window, text = "Add to Cart",font=('georgia',10), width='16', bg = 'yellow', fg = '#008B8B', command=addcart)
        addcartButton.grid(row = 7, column = 3, sticky = W)

        #Calculate Item total with button
        itemtotalButton=Button(window, text = "Calculate Total",font=('georgia',10), width='16', bg='#EF6262',fg='white',command = self.carttotal)
        itemtotalButton.grid(row = 6, column = 3, sticky = W)

        # Output area
        self.itemtotalVar = StringVar()
        Label(window, textvariable = self.itemtotalVar, font=('georgia',9), bg='#9EE9AB').grid(row = 7, column = 2)
        
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

        # Option menu for card type
        cardtype = StringVar(window)
        cardtype.set("VISA") # default value
        Label(window, text = "Card Type", font=('georgia',9), bg='#9EE9AB').grid(row = 17, column = 3, sticky = W)
        cardtypeButton=OptionMenu(window,cardtype,"VISA","Mastercard","PayPal")
        cardtypeButton.grid(row = 17, column = 4)
        cardtypeButton.config(width=13)

        #submit order button
        def OrderConf():
            if cartlist != testing:
                orderconf=Label(window, text='Order success.\nConfirmation #011252213',font=('georgia',12, 'bold'), bg='#9EE9AB', fg='#DC143C')
                orderconf.place(relx=0.85, rely=0.7, anchor=S)

        submitOrder=Button(window, text = "Submit Order", font=('georgia',10), width='16', bg='#008B8B',fg='white', command=OrderConf)
        submitOrder.place(relx=0.85, rely=0.5, anchor=S)

        #Help button
        def helpservice():
            orderconf=Label(window, text='Call IT: 817-807-8888',font=('georgia',11, 'bold'), bg='#9EE9AB', fg='#4B0082')
            orderconf.place(relx=0.85, rely=0.87, anchor=S)

        helpButton=Button(window, text = "Need help?", font=('georgia',10), width='16', bg='#4B0082',fg='white', command=helpservice)
        helpButton.place(relx=0.85, rely=0.95, anchor=S)

        Frame(window, bg='#008B8B').place(relx=0.7, rely=0,relwidth=0.002,relheight=5,anchor='n')

        window.mainloop() # Create an event loop to display the window

        
PhoneOrder()  # Create GUI 


#ADd help button _ doesnt have to function
# submit order button
# Add if functions?
# Test case for eavery field, missing or incorrect data; out of range