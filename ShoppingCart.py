
# Initialize an empty list to store the items and prices
shopping_cart = []

# Function to add an item to the shopping cart
def add_item():
    item = input("What item would you like to add? ")
    price = float(input("What is the price of '{}'? ".format(item)))
    shopping_cart.append({'item': item, 'price': price})
    print("'{}' has been added to the cart.\n".format(item))

# Function to display the contents of the shopping cart
def display_cart():
    if len(shopping_cart) == 0:
        print("The shopping cart is empty.\n")
        return
    
    print("The contents of the shopping cart are:")
    for i, item in enumerate(shopping_cart):
        print("{}. {} - ${:.2f}".format(i+1, item['item'], item['price']))
    print()

# Function to remove an item from the shopping cart
def remove_item():
    if len(shopping_cart) == 0:
        print("The shopping cart is already empty.\n")
        return
    
    index = int(input("Which item would you like to remove? ")) - 1
    if index >= 0 and index < len(shopping_cart):
        removed_item = shopping_cart.pop(index)
        print("'{}' has been removed.\n".format(removed_item['item']))
    else:
        print("Invalid item index.\n")

# Function to compute the total price of the items in the shopping cart
def compute_total():
    total = sum(item['price'] for item in shopping_cart)
    print("The total price of the items in the shopping cart is ${:.2f}\n".format(total))

# Main program loop
print("Welcome to the Shopping Cart Program!\n")
while True:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = input("Please enter an action: ")
    
    if action == '1':
        add_item()
    elif action == '2':
        display_cart()
    elif action == '3':
        remove_item()
    elif action == '4':
        compute_total()
    elif action == '5':
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid action. Please try again.\n")

        
        