def add_item(menu, item):
    if item not in menu:
        menu.append(item)
        print(f"Item '{item}' has been added to the menu.")
    else:
        print(f"Item '{item}' already exists in the menu.")
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        print(f"Item '{item}' has been removed from the menu.")
    else:
        print(f"Item '{item}' is not present in the menu.")
def availability_item(menu, item):
    if item in menu:
        return f"Item '{item}' is available in the menu."
    else:
        return f"Item '{item}' is not available in the menu."
menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item_input = "Tacos"
remove_item_input = "Salad"
check_item_input = "Pizza"
add_item(menu, add_item_input)
remove_item(menu, remove_item_input)
availability = availability_item(menu, check_item_input)
print("Updated menu:", menu)
print("Availability:", availability)
