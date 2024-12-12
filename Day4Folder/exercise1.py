'''
Expand on the previous NTUC Cashier program

This time, the customer can choose up to 3 items to buy
e.g. apples, oranges, and eggs

You can set a price for each item.
1. Ask the customer what they are buying
2. Ask the customer how many units of the item are they buying
3. Keep asking the customer until the customer says "enough"
4. Calculate the total purchase of the customer
'''
candy = 1
chocolate = 2
can_drinks = 2
total = 0

answer = input("Are you buying anything?")
while answer == "yes":
    item = input("What are you buying today?")
    quantity = input("How many of each item?")
    quantity = int(quantity)
    if item == "candy":
        price = candy * quantity
        total = total + price
    if item == "chocolate":
        price = chocolate * quantity
        total = total + price
    if item == "can_drinks":
        price = can_drinks * quantity
        total = total + price
    answer = input("Anything else?")
print("The total is $", total)
print("thank you for visiting NTUC")


