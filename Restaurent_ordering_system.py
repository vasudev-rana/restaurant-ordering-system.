#Define the menu of Resturant
menu = {
    'Pizza' : 80,
    'Pasta' : 60,
    'Maggie' : 50,
    'Burger' : 60,
    'Sandwich' : 40,
    'Coffee' : 75,
    'Salad' : 30,
}
print("Welcome to Rana's Restaurant:")
print("Pizza: Rs80\nPasta: Rs60\nMaggie: Rs50\nBurger: Rs60\nSandwich: Rs40\nCoffee: Rs75\nSalad: Rs30")

order_total = 0

item1 = input("Enetr the name of item:-")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order. ")
else:
    print(f"Orderes item {item1} is not avaiable yet! ")    
    
another_order = input("Do you want another item? (yes/No) ")
if another_order == "Yes":
    item2 = input("Enter the name of next item: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your {item2} has been added.")
    else:
        print(f"Your {item2} is not avaiable yet! ")    
    
    print(f"The total amount of your order is: {order_total} ")