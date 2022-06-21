from ..Room import Room

class Sala1(Room):
  def __init__(self, state):
    super().__init__(state)

  def init(self):
    for i in range(25): print("-", end="")
    print("\n", "você está na sala", "\n")
    self.escolhas()

  def reset(self):
    self.itens.clear()
    self.itens = ["extensão"]

    self.saidas.clear()
    self.saidas = [self.stateObj.quarto1, self.stateObj.cozinha]

  def getName(self):
    return "sala"