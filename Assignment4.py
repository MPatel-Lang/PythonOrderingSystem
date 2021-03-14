# This is my sample program, with a block comment at the top. The block comment needs to contain the following
# 1. Name: Mehul Patel
# 2. Date: 10/15/2020
# 3. Program description: Prompt the user for input, and indicate they can enter in the word “quit” to quit. The user should enter
#         in a part and then the quantity on two separate lines (so you’ll need two input statements). After both
#         pieces of information have been entered in, check if the order is allowed or not, and display an error
#         message with the appropriate information (part doesn’t exist, part exists but not enough quantity).
#
#

# importing json module of python
import json

# sample json data
supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket":{"price": 3.99, "quantity": 32},"gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4},"dodad": {"price": 0.5, "quantity": 0}}'

# loading json data using loads method of json and storing in json_data
Data = json.loads(supplier_data)

# defining a empty user order dict
orders = {}
# displaying a menu to user
print("Welcome to the parts ordering system, please enter in a part name, followed by a quantity")

#fetching parts from json_data
parts = Data["parts"]
# displaying parts, using for loop to do the same
print("Parts for order are:")
for part in parts:
    print(part)
    
# infinite while loop for prompting user untill quit is hit
while True:
    # prompting user for part name
    part_name = input("Please enter in a part name, or quit to exit: ")
    
    # if quit exit the loop
    if part_name=="quit":
        break
    # elseif part not in parts list display error
    elif part_name not in parts:
        # display error message
        print("Error, part does not exist, try again")
        # continue loop for correct input
        continue
        
    # otherwise, part name is correct
    # prompting user for order quantity
    # converting input quantity to integer using int function
    quantity = int(input("Please enter in a quantity to order: "))
    
    # checking for correct quantity, including quantity from both json_data
    # and users already orders
    
    # order quantity from json_data
    Data_Quantity = Data[part_name]["quantity"]
    # order quantity from already ordered goods
    # using dict method get to fetch value from passed key, if key not exist
    # returning 0 by default
    ord_quant = orders.get(part_name,0)
    
    # actual quantity present
    actual_quant = Data_Quantity - ord_quant
    
    # checking if quant> actual_quant, displaying error
    if quantity> actual_quant:
        print("Error, only {} of {} are available!".format(actual_quant,part_name))
        # continue loop for correct input
        continue
        
    # otherwise order quant is correct, adding quantity in orders dict of user
    # with already present order quantity
    orders[part_name] = ord_quant + quantity
    
# after all orders completed, displaying orders detils
print("Your order")
# defining sum counter to fetch total orders value
total = 0
# for loop for every order in orders dict
for order in orders:
    # fetching details from respective datas
    # order price per quantity
    price = Data[order]["price"]
    # total price of order
    order_price = price * orders[order]
    # displaying message
    print("{} - {} @ {:.2f} = {:.2f}".format(order,orders[order],price,order_price))
    # add order price to total
    total +=order_price
    
# displaying total
print("Total: ${:.2f}".format(total))
# print thank you
print("Thank you for using the parts ordering system!")
