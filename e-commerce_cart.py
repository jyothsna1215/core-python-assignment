def total_price(cart):
    if not cart:
        print("The cart is empty.")
        return
    total = sum(cart.values())
    if len(cart) > 5:
        total *= 0.9  # Apply discount (10%)
        print(f"Total price of items after discount is {total:.2f}")
    else:
        print(f"Total price of items is {total:.2f}")
cart = {}
while True:
    item = input("Enter the item name: ")
    if item.lower() == "done":
        break
    price = int(input(f"Enter the cost of '{item}': "))
    cart[item] = price
total_price(cart)
