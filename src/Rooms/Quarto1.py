from ..Room import Room
from ..ItemsAmbiente.BuracoNoTeto import BuracoNoTeto

class Quarto1(Room):
  def __init__(self, stateObj):
    super().__init__(stateObj)
    
  def reset(self):
    self.itens.clear()
    self.itens = ["despertador"]

    self.itensAmbiente.clear()
    self.itensAmbiente = [BuracoNoTeto(self.stateObj)]

    self.saidas.clear()
    self.saidas = [self.stateObj.sala1]

  def init(self):
    dialogo1 = "Você está no seu quarto"
    print(dialogo1)
    self.escolhas()

  def getName(self):
    return "quarto"