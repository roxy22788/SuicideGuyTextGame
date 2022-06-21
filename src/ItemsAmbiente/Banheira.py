class Banheira:
  def __init__(self, state):
    self.state = state
    self.itemsNecessarios = ["despertador", "extensão", "remedios"]
    self.morte = "Você conectou a extensão na tomada da cozinha e trouxe para o banheiro, lá você conectou o despertador e ligou a banheira para ela encher de agua, enquanto você espera a banheira encher de agua você toma todos os remedios que pegou na cozinha para ficar dopado, então.... vc se deita na banheira e joga o despertador junto com a extensão dentro da banheira de agua... fim"

  def usar(self):
    if self.state.inventario.searchItems(self.itemsNecessarios):
      return self.morte
    else:
      return None

  def getName(self):
    return "banheira"