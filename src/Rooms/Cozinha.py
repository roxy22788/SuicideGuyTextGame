from ..Room import Room

class Cozinha(Room):
  def __init__(self, state):
    super().__init__(state)

  def init(self):
    for i in range(25): print("-", end="")
    print("\n", "você está na cozinha", "\n")
    self.escolhas()

  def reset(self):
    self.itens.clear()
    self.itens = ["remedios"]

    self.saidas.clear()
    self.saidas = [self.stateObj.sala1, self.stateObj.banheiro, self.stateObj.deposito]

  def getName(self):
    return "cozinha"