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
    inventarioArg = self.stateObj.inventario

    for i in range(20): print("=", end="")
    print()
    
    items = []
    
    if len(itemsArg) > 0:
      items.append({"items": itemsArg}) 
    if len(itemsAmbienteArg) > 0:
      items.append({"items ambientes": itemsAmbienteArg})
    if len(saidasArg) > 0:
      items.append({"saidas": saidasArg})
    #itens padrões
    items.append({"inventario": ["ver itens", "remover itens"]})
 

    self.__mostrarTodosItens(items)
    resposta = self.__receberResposta(items)
    self.__processarResposta(items, resposta)
    
  #recebe um array de dicionarios
  #  [{'items': ['despertador', 'vassoura']}]
  def __mostrarTodosItens(self, items):
    for i in items:
      itemDescompact = list(i.items())[0]
      print("opções de", itemDescompact[0], "presentes: ")
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
      r = self.stateObj.inventario.appendItem(item[1][resposta])
      if r:
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
    elif item[0] == "inventario":
      items = self.stateObj.inventario.requestItems()
      if len(items) != 0:
        if resposta == 0:
          print("\nItens no inventario: ")
          self.__mostrarItems(items)
        elif resposta == 1:
          self.__mostrarItems(items)
          print("Qual dos itens você quer remover?")
          r = self.__receberResposta(items)
          self.stateObj.inventario.removeByIndex(r)
          print("item removido")
      else:
        print("\ninventario vazio\n")
        
      self.escolhas()