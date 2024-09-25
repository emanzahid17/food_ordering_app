rest_name = 'Cookie Foodie'

menu = {
    'SKU1': {'ITEM': 'PIZZA', 'PRICE': 5.80},
    'SKU2': {'ITEM': 'BURGER', 'PRICE': 3.50},
    'SKU3': {'ITEM': 'PASTA', 'PRICE': 6.00},
    'SKU4': {'ITEM': 'SALAD', 'PRICE': 4.25},
    'SKU5': {'ITEM': 'SODA', 'PRICE': 1.50}
}

cart = {}

actions = {
    "1": "Add item to cart",
    "2": "Remove item from cart",
    "3": "Modify items' quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit"
}

gst = 0.05 #sales tax

#creating function for displaying menu

def display_menu():
  '''this function displays the menu which includes serial number, item name, and price'''

  print("\n**COOKIE FOODIE's MENU**\n")

  for sku in menu:
    stock = sku[3: ]
    name = menu[sku]['ITEM']
    price = menu[sku]['PRICE']

    print(f'({stock}) {name} - ${price}')
  print('\n')

#creating function for add to cart
def add_to_cart(sku, quantity = 1):
  '''this function adds item to cart. take input from user which includes item number and
  quantity. by default quantity is 1'''

  if sku in menu:
    #check if item is already in cart or not
    if sku not in cart:
      cart[sku] = quantity
    else:
      cart[sku] += quantity
      print(f'{quantity} {menu[sku]["ITEM"]} added to cart')
  else:
    print('Invalid item number, try valid item number')

#create function for removing items from cart

def remove_from_cart(sku):
  '''this function removes item from cart. take input from user which includes item number'''

  if sku in cart:
    removed = cart.pop(sku)
    print(f'Removed {menu[sku]["ITEM"]} from cart')
  else:
    print(f"Sorry! The {menu[sku]['ITEM']} is not in the cart.")

#3rd action --modifying item's quantity

def modify_item_quantity(sku, new_quantity):
  '''this function modifies item's quantity. take input from user which includes item number and new quantity'''

  if sku in cart:
    if new_quantity > 0:
      cart[sku] = new_quantity
      print(f'Quantity of {menu[sku]["ITEM"]} modified to {new_quantity}')
    else:
      remove_from_cart(sku)
  else:
    print(f"The item is not in the cart.")

def view_cart():
  '''this function displays cart to customer'''

  print("\n**YOUR CART**\n")
  before_tax = 0


  for sku in cart:
    quan = cart[sku]
    price = menu[sku]['PRICE']

    before_tax += quan * price


    print(f'{quan} * {menu[sku]["ITEM"]}')

  tax = before_tax*gst
  total = before_tax + tax

  print(f'Before tax: ${before_tax:.2f}')
  print(f'GST: ${tax:.2f}')
  print(f'Total: ${total:.2f}')
  print('\n')

#creating function for checkout

def checkout():
  '''this function displays cart to customer'''
  print("\n**CHECKOUT**\n")

  view_cart()
  print('Thank you for placing the order!')
  print("\n")

#creating fucntion for displaying action for customer

def display_actions():
  '''this function displays action for customer'''
  print("\n**PLEASE CHOOSE YOUR OPTION**\n")

  for action in actions:
    details = actions[action]
    print(f'({action}) {details}')


def get_sku_quantity(sku_prompt, quantity_prompt = None):
  '''this function will take sku and quantity from customer'''


  sku_num = input(sku_prompt)
  sku = 'SKU' + sku_num

  if quantity_prompt:
    qty = input(quantity_prompt)
    if not qty.isdigit():
      qty = 1
    else:
      qty = int(qty)
    return sku, qty
  else:
    return sku
  
def order_from_customer():
  '''this function will take order from cuustomers'''
  print("\n**Welcome to the COOKIE FOODIE!")

  ordering = True
  while ordering:
    display_actions()
    resp = input('Enter your choice: ')
    if resp == '1': #add item to cart
      display_menu()
      sku_prompt = 'enter the meal number from the menu item you want to order: '
      quantity_prompt = 'enter the quantity of the meal you want to order: '
      sku, quantity = get_sku_quantity(sku_prompt, quantity_prompt)
      add_to_cart(sku, quantity)

    elif resp == '2': #remove from cart
      display_menu()
      view_cart()
      sku_prompt = 'enter the meal number from the cart you want to remove: '
      sku = get_sku_quantity(sku_prompt)
      remove_from_cart(sku)

    elif resp == '3': #modify cart
      display_menu()
      view_cart()
      sku_prompt = 'enter the meal number from the cart you want to modify: '
      quantity_prompt = 'enter the new quantity: '
      sku, quantity = get_sku_quantity (sku_prompt, quantity_prompt)
      modify_item_quantity(sku, quantity)
    elif resp == '4': #view cart
      view_cart()
    elif resp == '5': #checkout
      checkout()
      ordering = False
    elif resp == '6': #exit
      print('Thank you! I hope you have a good experience with us!')
      ordering = False
    else:
      print('Invalid choice. Please try again.')


order_from_customer()