inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dictValue):
  print("inventory:")
  item_total = 0
  for k, v in dictValue.items():
    print(str(v) + ' ' + k)
    item_total += v
  print('Total number of: ' + str(item_total))

displayInventory(inventory)
