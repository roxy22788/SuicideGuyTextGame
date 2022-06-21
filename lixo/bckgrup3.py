import console

class Room:
  def __init__(self, stateObj):
    self.stateObj = stateObj
    self.itens = []
    self.itensAmbiente = []
    self.saidas = []

    
  def escolhas(self): 
    itemsArg = self.itens
    itemsAmbienteArg = self.itensAmbiente
    saidasArg = self.saidas

    for i in range(20): print("=", end="")
    print()
    
    items = []
    
    if len(itemsArg) > 0:
      items.append({"items": itemsArg}) 
    if len(itemsAmbienteArg) > 0:
      items.append({"items ambientes": itemsAmbienteArg})
    if len(saidasArg) > 0:
      items.append({"saidas": saidasArg})
 

    self.__mostrarTodosItens(items)
    resposta = self.__receberResposta(items)
    self.__processarResposta(items, resposta)
    
  #recebe um array de dicionarios
  #  [{'items': ['despertador', 'vassoura']}]
  def __mostrarTodosItens(self, items):
    for i in items:
      itemDescompact = list(i.items())[0]
      print(itemDescompact[0], "presentes: ")
      self.__mostrarItems(itemDescompact[1])
      print()

    print("O que deseja usar? ")
    
    for index, i in enumerate(items):
      itemDescompact = list(i.items())
      print(str(index) + ": usar", itemDescompact[0][0])

  # recebe um array de itens, e mostra  com seus indices
  def __mostrarItems(self, items):
    for index, data in enumerate(items):
      if type(data) == str:
        print(str(index) + ":", data)
      else:
        print(str(index) + ":", data.getName())

  #recebe um array de itens
  # ex1: [{'items': ['despertador', 'vassoura']}]
  # ex2: ["despertador", "vassoura"]
  # retorna o index do item que o usuario quer escolher
  def __receberResposta(self, items):
    aux = False
    while not aux:
      try:
        inp = int(input("Resposta: "))
      except:
        print("Digite um inteiro válido")
      else:
        if inp < 0 or inp > len(items) -1:
          print("item não existe")
        else:
          return inp

  def __processarResposta(self, items, resposta):
    item = items[resposta]
    item = list(item.items())[0]
    
    print("\nqual dos(as)", item[0], "você quer? ")
    self.__mostrarItems(item[1])
    resposta = self.__receberResposta(item[1])

    if item[0] == "items":
      self.stateObj.inventario.appendItem(item[1][resposta])
      self.itens.remove(item[1][resposta])
      self.escolhas()
    elif item[0] == "items ambientes":
      r = item[1][resposta].usar()
      if r:
        self.stateObj.morte(r)
      else:
        print("\nfalta item(s) requiridos\n")
        self.escolhas()
    elif item[0] == "saidas":
      self.stateObj.trocarEstado(self.saidas[resposta])






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





class Sala1(Room):
  def __init__(self, state):
    super().__init__(state)

  def init(self):
    for i in range(25): print("-", end="")
    print("\n", "você está na sala", "\n")
    self.escolhas()

  def reset(self):
    self.itens.clear()
    self.itens = ["corda", "extensão", "banquinho"]

    self.saidas.clear()
    self.saidas = [self.stateObj.quarto1]

  def getName(self):
    return "sala"

    
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
      



class Inventario:
  def __init__(self):
    self.items = []

  def reset(self):
    self.items = []

  def appendItem(self, item):
    self.items.append(item)
    print("\n", item, "adicionado ao inventario!", "\n")

  def requestItem(self, item):
    indexItem = self.searchItem(item)
    if indexItem != -1:
      self.items.pop(indexItem)
      return True
    return False

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

    self.itensResetaveis = [self.inventario, self.quarto1, self.sala1]

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
    console.limparConsole()
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
        
    



# s = StateControl("Julios")
# s.init()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstName = fname
#     self.lastName = lname

#   def printName(self):
#     print(self.firstName, self.lastName)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("welcome", self.firstName, self.lastName, "to the class of", self.graduationyear)


# x = Student("mike", "buceta", 2019)
# x.welcome()


from src.StateControl import StateControl as pika

