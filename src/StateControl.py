from .Inventario import Inventario 

from .Rooms.Quarto1 import Quarto1
from .Rooms.Sala1 import Sala1
from .Rooms.Cozinha import Cozinha
from .Rooms.Banheiro import Banheiro
from .Rooms.Deposito import Deposito

from . import Console

class StateControl:
  def __init__(self, nomePersonagem):
    self.nomePersonagem = nomePersonagem
    self.nomeVilao = "Dono da porra toda"
    self.state = None

    #inventario
    self.inventario = Inventario()

    #quartos
    self.quarto1 = Quarto1(self)
    self.sala1 = Sala1(self)
    self.cozinha = Cozinha(self)
    self.banheiro = Banheiro(self)
    self.deposito = Deposito(self)

    self.itensResetaveis = [self.inventario, self.quarto1, self.sala1, self.cozinha, self.banheiro, self.deposito]

    #inicia todas as variaveis de todos os objetos
    self.reset()

  def init(self):
    # dialogo1 = self.nomeVilao + ": Olá " + self.nomePersonagem + ", eu sou muito grato por você ter aceitado os termos, isso me dá o poder de fazer qualquer coisa contigo. Bom... para começar irei te trancar em um mundo ficticio onde passará o resto da vida"
    # dialogo2 = self.nomePersonagem + ": \"para sempre\"?, bobagem... isso é algum daqueles desafios de tentar achar maneiras de sair do mundo?"
    # dialogo3 = self.nomeVilao + ": ta ;-; vc me pegou, é isso msm, tu parece manjar dos bagui, então pararei de explicar e tente por você msm"
    # dialogo4 = self.nomeVilao + " te teletransporta para um quarto...."
    # dialogo5 = self.nomePersonagem + ": Então vamos lá neh... como aqui é um mundo ficticio, o que aconteceria se eu morresse? eu morreria de verdade ou seria a maneira de sair dessa merda? bom, vale minha vida se eu errar, mas irei tentar...."

    # dialogo = [dialogo1, dialogo2, dialogo3, dialogo4, dialogo5]
    # for i in dialogo:
    #   console.escrever(i)
    #   print()
    #   print()

    self.trocarEstado(self.quarto1)

  def trocarEstado(self, newEstado):
    Console.limparConsole()
    self.state = newEstado
    self.state.init()

  def morte(self, morte):
    print(morte)
    rejogar = None
    while rejogar == None:
      try:
        print("Rejogar?\n1) sim\n2) não")
        inp = int(input("Resposta: "))
      except:
        print("digite um inteiro válido")
      else:
        if inp == 1:
          rejogar = True
        elif inp == 2:
          rejogar = False
        else:
          print("resposta invalida")
          
    if rejogar:
      self.reset()
      self.trocarEstado(self.quarto1)
    else:
      print("\n", "xauuuu", "\n")
      exit()

  def reset(self):
    for i in self.itensResetaveis:
      i.reset()
        