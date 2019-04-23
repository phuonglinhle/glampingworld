'''
Program:     Shopping Cart System  - runs in console - NOT in Windows
Description: The following example implements a shopping cart system 
             using classes with instance data members and methods. 
'''


class ItemToPurchase:                     # this ItemToPurchase class is a template for creating instances of a Item
   def __init__(self):                    # this type of method is known as a constructor, setting up attributes of a new instance with specified values
      self.item_name = 'none'             # we are initializing the Item with name, description, price and quantity attributes
      self.item_description = 'none'
      self.item_price = 0.0
      self.item_quantity = 0

   def print_item_cost(self):             # print_item_cost is a method of the ItemToPurchase class that prints the name of item, quantity, its price and total cost
      totalCost = self.item_quantity * self.item_price
      print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, totalCost))
   
   def print_item_description(self):       # print_item_description is a method of the ItemToPurchase class that prints the name of item and its description
      print('%s: %s' % (self.item_name, self.item_description))


class ShoppingCart:                        # this ShoppingCart class is a template for creating instances of a ShoppingCart
   def __init__(self, customer_name, current_date):
      self.customer_name = customer_name   # we are initializing the ShoppingCart m with a customer name, curent date and list of shopping cart items that is empty
      self.current_date = current_date
      self.cart_items = []
   
   def add_item(self, item):                # add_item is a method of the ShoppingCart class that appends an item to the shopping cart    
      self.cart_items.append(item)
   
   def remove_item(self, item_name):        # remove_item is a method of the ShoppingCart class looks for an item in a shopping cart and if it finds it, then it removes it from the list
      found = False                         # if the item is not found an item not found message is generated.
      for i in self.cart_items:
         if i.item_name == item_name:
            found = True
            self.cart_items.remove(i)
      if found == False:
         print('Item not found in cart. Nothing removed.')
   
   def modify_item(self, item):             # modify_item is a method of the ShoppingCart class looks for an item in a shopping cart and if it finds it, then it changes the item name and quantity
      found = False                         # if the item is not found an item not found message is generated.
      for i in range(len(self.cart_items)):
         if self.cart_items[i].item_name == item.item_name:
            found = True
            self.cart_items[i].item_quantity = item.item_quantity
      if found == False:
         print('Item not found in cart. Nothing modified.')
   
   def get_num_items_in_cart(self):          # get_num__items_in_cart is a method of the ShoppingCart class that counts and returns the number of items in the shopping cart   
      totalNumItems = 0
      for i in self.cart_items:
         totalNumItems += i.item_quantity
      return totalNumItems
   
   def get_cost_of_cart(self):                # get_cost_of-cart is a method of the ShoppingCart class that calculates the total cost of items in the cart by multiplying the item cost by quantity and adding it all up
      totalCost = 0
      for i in self.cart_items:
         totalCost += (i.item_price * i.item_quantity)
      return totalCost
   
   def print_total(self):                     # print_total is a method of the ShoppingCart class that prints the name of customer, current date, number of carts in the cart, cost of items and total cost
      print('%s\'s Shopping Cart - %s' % (self.customer_name, self.current_date))
      print('Number of Items: %d\n' % self.get_num_items_in_cart())
      
      if len(self.cart_items) > 0:
         for i in self.cart_items:
            i.print_item_cost()
      else:                                    # if the cart is empty, an empty message is displayed to the user
         print('SHOPPING CART IS EMPTY')
      totalCost = self.get_cost_of_cart()
      print('\nTotal: $%d' % totalCost)
   
   def print_descriptions(self):               # print_description is a method of the ShoppingCart class that prints the name of customer, current date, and item descriptions
      print('%s\'s Shopping Cart - %s\n' % (self.customer_name, self.current_date))
      print('Item Descriptions')
      if len(self.cart_items) > 0:
         for i in self.cart_items:
            i.print_item_description()
      else:
         print('SHOPPING CART IS EMPTY')       # if the cart is empty, an empty message is displayed to the user


def print_menu(theCart):                       #print_menu is a function of the ShoppingCart class that prints the menu options as long as the user does not enter a valid option
   menuOp = ' '
   
   print('MENU')
   print('a - Add item to cart')
   print('r - Remove item from cart')
   print('c - Change item quantity')
   print('i - Output items\' descriptions')
   print('o - Output shopping cart')
   print('q - Quit\n')
   
   while menuOp != 'a' and menuOp != 'r' and menuOp != 'c' and menuOp != 'i' and menuOp != 'o' and menuOp != 'q':
      menuOp = input('Choose an option:\n')
   
   if menuOp == 'a':                         #if a user selects to add item to cart, the program asks for item name, description, price, and quantity and creates an instance of ItemToPurchase
      print('ADD ITEM TO CART')
      name = input('Enter the item name:\n')
      description = input('Enter the item description:\n')
      price = float(input('Enter the item price:\n'))
      quantity = int(input('Enter the item quantity:\n'))
      
      newItem = ItemToPurchase()             # create a new instance of ItemToPurchase and assign values to its attributes.
      newItem.item_name = name
      newItem.item_description = description
      newItem.item_price = price
      newItem.item_quantity = quantity
      theCart.add_item(newItem)
   
   elif menuOp == 'r':                       # if the user selects to remove item from cart, ask for a name of an itema and use the remove_itemmethod, passing it the item name as an argument
      print('REMOVE ITEM FROM CART')
      name = input('Enter name of item to remove:\n')
      theCart.remove_item(name)
   
   elif menuOp == 'c':                       #if the user selects to change the item quantity, ask for item name, and new quantity.
      print('CHANGE ITEM QUANTITY')
      name = input('Enter the item name:\n')
      quantity = int(input('Enter the new quantity:\n'))
      
      item = ItemToPurchase()                # create a new instance of ItemToPurchase and assign values to its name and quantity attributes and call modify_item method with the new item as an argument
      item.item_name = name
      item.item_quantity = quantity
      theCart.modify_item(item)
   
   elif menuOp == 'i':                       # if the user selects to print descriptions, call the print_descriptions method of the ShoppingCart
      print('OUTPUT ITEMS\' DESCRIPTIONS')
      theCart.print_descriptions()
   
   elif menuOp == 'o':                       # if the user selects to output shopping cart, call the print_total method of the ShoppingCart
      print('OUTPUT SHOPPING CART')
      theCart.print_total()
   
   return menuOp                             #return menu option the user selected.

if __name__ == "__main__":                   # the main module of the shopping cart class starts here.
   menuChoice = ' '
   custName = input('Enter customer\'s name:\n') # ask for the customer name and today's date.
   dayDate = input('Enter today\'s date:\n')
   
   print('\nCustomer name: %s' % custName)       # print customer name and today's date.
   print('Today\'s date: %s' % dayDate)
   
   myCart = ShoppingCart(custName, dayDate)      # create an instance of Shopping Cart called myCart passing it as arguments customer name and date
   
   while menuChoice != 'q':                      # as long as the menu choice is not 'q' call the print_menu function and assign the value it returns to the menuChoice variable.
      print('')
      menuChoice = print_menu(myCart)
