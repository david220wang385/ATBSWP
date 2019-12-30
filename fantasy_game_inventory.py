# Displays contents of an "inventory," where keys are items and values are the item's quantity
def displayInventory(inventory):
    print("Inventory:")
    totalItems = 0
    for item, quantity in inventory.items():
        print(str(quantity) + "\t" + item)
        totalItems += quantity
    print("Total number of items: ", totalItems, "\n")
