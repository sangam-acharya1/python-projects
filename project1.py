menu = {
    "momo": 180,
    "pasta": 150,
    "burger": 180,
    "pizza": 360,
    "fried rice": 120,
}

print("Welcome to Sangam Restaurant!")
your_total = 0

item_1 = input("What would you like to order? ")
if item_1 in menu:
    your_total += menu[item_1]
    print("Your item is added successfully.")
else:
    print("This item is not available at the moment.")

another_item = input("Do you want to order more items? (yes/no) ")
if another_item == 'yes':
    item_2 = input("What is your next order? ")
    if item_2 in menu:
        your_total += menu[item_2]
        print("Your item is added successfully.")
    else:
        print("This item is not available at the moment.")

print(f"Total amount to pay is: {your_total}")
