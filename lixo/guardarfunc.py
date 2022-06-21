  def escolhas(self, itemsArg, itemsAmbienteArg, saidasArg):
    items = []
    dialogo = ""
    
    if len(itemsArg) > 0:
      items.append({"items": itemsArg})
      dialogo += "\nitems: "
      for i in itemsArg:
        dialogo += i    
    if len(itemsAmbienteArg) > 0:
      items.append({"Items Ambientes": itemsAmbienteArg})
      dialogo += "\nitemsAmbiente: "
      for i in itemsAmbienteArg:
        dialogo += i
    if len(saidasArg) > 0:
      items.append({"saidas": saidasArg})
      dialogo += "\nsaidas: "
      for i in saidasArg:
        dialogo += i      
    print(dialogo)
    
    dialogo1 = "O que deseja fazer? "
    print(dialogo1)
    for index, data in enumerate(items):
      print(str(index) + ":", "usar " + list(data.keys())[0])
      
    respostaValida = False
    while not respostaValida:
      try:
        inp = int(input("Resposta: "))
      except:
        print("Digite um valor númerico válido")
      else:
        if inp < 0 or inp > len(items) - 1:
          print("Opção não existe")
        else:
          respostaValida = True


    opcaoEscolhida = []
    for item, data in items[inp].items():
      opcaoEscolhida.append(item)
      opcaoEscolhida.append(data)
      
    print("qual", opcaoEscolhida[0], "você quer? ")
    for index, data in enumerate(opcaoEscolhida[1]):
      print(str(index) + ":", data)
    itemEscolhido = 0
    aux = False
    while not aux:
      try:
        inp = int(input("Resposta: "))
      except:
        print("Digite um número inteiro valido")
      else:
        if inp < 0 or inp > len(opcaoEscolhida[i]) -1:
          print("Item não existe")
        else:
          itemEscolhido = inp
          aux = True