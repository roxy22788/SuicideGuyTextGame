from ..Room import Room

class Deposito(Room):
  def __init__(self, state):
    super().__init__(state)

  def init(self):
    for i in range(25): print("-", end="")
    print("\n", "você está no deposito", "\n")
    self.escolhas()

  def reset(self):
    self.itens.clear()
    self.itens = ["banquinho", "corda"]

    self.saidas.clear()
    self.saidas = [self.stateObj.cozinha]

  def getName(self):
    return "deposito"
    