inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(v, k)
        total += v
    print('Total number of items:', total)


def addToInventory(inventory, addedItems):
    for addedItem in addedItems:
        inventory.setdefault(addedItem, 0)
        inventory[addedItem] += 1
    return inventory


addToInventory(inventory, dragonLoot)
displayInventory(inventory)
