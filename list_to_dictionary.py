import fantasy_game_inventory as inv


# Add items in list to a inventory (dictionary)
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory[item] = 1;
        else:
            inventory[item] += 1;


# Start of program
playerInv2 = {
    'gold coin': 42,
    'rope': 1
}

dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby'
]

# Inventories before adding items
inv.displayInventory(playerInv2)

addToInventory(playerInv2, dragonLoot)

# After adding items
inv.displayInventory(playerInv2)
