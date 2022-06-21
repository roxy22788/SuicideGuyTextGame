import console


class buracoNoTeto:
  def __init__(self, state):
    self.state = state
    self.itemsNecessarios = ["corda", "banquinho"]
    self.morte = "Você pegou seu banquinho, subiu nele, amarrou a corda no buraco presente no teto e deu adeus."

  def usar(self):
    if self.state.inventario.searchItems(self.itemsNecessarios):
      self.state

  def getName(self):
    return "buraco no teto"


class Quarto1:
  def __init__(self, stateObj):
    self.stateObj = stateObj
    self.itens = []
    self.itensAmbiente = []
    self.saidas = []
    
    self.reset()

  def reset(self):
    self.itens = ["despertador"]
    self.itensAmbiente = ["buraco no teto"]
    self.saidas = ["sala"]

  def init(self):
    # dialogo1 = "Você está no seu quarto"
    # if len(self.itens) > 0:
    #   dialogo1 += "\nitens: "
    #   for i in self.itens:
    #     dialogo1 += i
    # if len(self.itensAmbiente) > 0:
    #   dialogo1 += "\nutilizaveis: "
    #   for i in self.itensAmbiente:
    #     dialogo1 += i
    # if len(self.saidas) > 0:
    #   dialogo1 += "\nsaidas: "
    #   for i in self.saidas:
    #     dialogo1 += i
    # console.escrever(dialogo1)
    # console.escrever("\no que deseja fazer? ")
    # console.escrever("\n1) pegar itens")
    # console.escrever("\n2) usar itens")
    # console.escrever("\n3) ir para a saida\n")
    #inp = input("Resposta: ")
    self.escolhas(self.itens, self.itensAmbiente, self.saidas)

  def escolhas(self, itemsArg, itemsAmbienteArg, saidasArg): 
    items = []
    dialogo = ""
    
    if len(itemsArg) > 0:
      items.append({"items": itemsArg})
      dialogo += "\nitems: "
      for i in itemsArg:
        dialogo += i    
    if len(itemsAmbienteArg) > 0:
      items.append({"items ambientes": itemsAmbienteArg})
      dialogo += "\nitemsAmbiente: "
      for i in itemsAmbienteArg:
        dialogo += i
    if len(saidasArg) > 0:
      items.append({"saidas": saidasArg})
      dialogo += "\nsaidas: "
      for i in saidasArg:
        dialogo += i      

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
      print(str(index) + ":", data)

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
    print()
    print("dentro de processar resposta")
    print(items)
    print()
    item = items[resposta]
    item = list(item.items())[0]
    print(item)
    
    print("qual dos(as)", item[0], "você quer? ")
    self.__mostrarItems(item[1])
    resposta = self.__receberResposta(item[1])
    print("você escolheu", item[1][resposta])

    if item[0] == "items":
      self.stateObj.inventario.appendItem(item[1][resposta])
      self.itens.remove(item[i][resposta])
    elif item[0] ==  "items ambientes":
      pass
      
      

    
      



class Inventario:
  def __init__(self):
    self.items = []

  def reset(self):
    self.items = []

  def appendItem(self, item):
    self.items.append(item)

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

    self.itensResetaveis = [self.inventario, self.quarto1]
  

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
    self.state = newEstado
    self.state.init()

  def morte(self, morte):
    print(morte)
    aux = False
    while not aux:
      inp = input("Rejogar? s=sim n=não")
      if inp == "s":
        aux = True
      else:
        print("resposta invalida")

    self.reset()
    self.trocarEstado(self.quarto1)

  def reset(self):
    for i in self.itensResetaveis:
      i.reset()
        
    



s = StateControl("Julios")
s.init()


