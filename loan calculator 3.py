from tkinter import * # Import tkinter
    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Loan Calculator") # Set title of a window
        
        #set up labels for the loan calculator in the left column of the window, align labels left (Sticky=W)
        Label(window, text = "Annual Interest Rate (%)").grid(row = 1, column = 1, sticky = W)                     
        Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Loan Amount ($)").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Monthly Payment ($)").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Total Payment ($)").grid(row = 5, column = 1, sticky = W)
        
        # set up the input area for the calculator in the right column, using Entry for textboxes and assigning the values entered to variables
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar,justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2)
        
        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        self.monthlyPaymentVar = StringVar()
        Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)
        self.totalPaymentVar = StringVar()
        Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)
        Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 6, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop to display the window

    # function computePayment calls the getMonthlyPayment function with arguments assigned to the values from the user
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), 
            float(self.annualInterestRateVar.get()) / 1200, 
            int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f')) #assign the value and format the monthlyPaymentVar to the value of monthlyPayment returned from getMonthlyPayment function
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())   #calculate totalPayment 
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
        
    #calculate Monthly Payment using the formula provided    
    def getMonthlyPayment(self,loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
           - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

LoanCalculator()  # Create GUI 
