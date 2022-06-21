class BuracoNoTeto:
  def __init__(self, state):
    self.state = state
    self.itemsNecessarios = ["corda", "banquinho"]
    self.morte = "Você pegou seu banquinho, subiu nele, amarrou a corda no buraco presente no teto e deu adeus."

  def usar(self):
    if self.state.inventario.searchItems(self.itemsNecessarios):
      return self.morte
    else:
      return None

  def getName(self):
    return "buraco no teto"