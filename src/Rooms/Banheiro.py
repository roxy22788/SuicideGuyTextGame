from ..Room import Room
from ..ItemsAmbiente.Banheira import Banheira

class Banheiro(Room):
  def __init__(self, state):
    super().__init__(state)

  def init(self):
    for i in range(25): print("-", end="")
    print("\n", "você está no banheiro", "\n")
    self.escolhas()

  def reset(self):
    self.itensAmbiente.clear()
    self.itensAmbiente = [Banheira(self.stateObj)]
    
    self.saidas.clear()
    self.saidas = [self.stateObj.cozinha]

  def getName(self):
    return "banheiro"