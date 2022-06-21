class Inventario:
  def __init__(self):
    self.items = []

  def reset(self):
    self.items = []

  def appendItem(self, item):
    if len(self.items) < 3:
      self.items.append(item)
      print("\n", item, "adicionado ao inventario!", "\n")
      return True
    else:
      print("\n", "Inventario cheio, max 3 itens", "\n")
      return False

  def requestItem(self, item):
    indexItem = self.searchItem(item)
    if indexItem != -1:
      self.items.pop(indexItem)
      return True
    return False

  def requestItems(self):
    return self.items

  # retorna o indice do item, caso não tenha retorna -1
  def searchItem(self, item):
    for i in range(len(self.items)):
      if self.items[i] == item:
        return i
    return -1

  def searchItems(self, itens):
    for i in itens:
      if i not in self.items:
        return False

    return True

  def removeByIndex(self, index):
    self.items.pop(index)
    

  def verItems(self):
    for index, item in enumerate(self.items):
      print(index + ":", item)



