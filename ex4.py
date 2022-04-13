def cadastrarPeca(): #iniciando uma função 
    peças = [] # cria uma lista 
    codigo = 1 #inicia um contador 
    while True: # inicia um laço de repetição sem condiçao
        codigo = len(peças)+1 #a varivale cofigo vai ser igual ao numero de peças ja cadastradas +1
        print(f'codigo da peça:{codigo}') #retorna o codigo da peça que vai ser gerada 
        nome = str(input('digite o nome da peça: ')) #entrada do nome da peça 
        marca = str(input('digite a marca da peça: ')) #entrada da marca da peça
        preço = float(input('digite o valor da peça: ')) #entrada do valor da peça
        peças.append({'nome':nome,'marca':marca,'preço':preço,'codigo':codigo}) #adiciona a lista de peças um dicionario com os valores das variaveis 
        continuar = str(input('quer adicionar uma nova peça? (S/N): ')).upper() #entrada de um de uma string em maiusculo
        if continuar =='N': #caso o usuario queira para de cadastrar o laço de repetição é cortado 
            break#para o laço
        else:# caso o usuario queira continuar sera retornado uma string para separar a peça anterior da proxima 
            print('-='*20)
    return peças # a função vai retornar a lista das peças
def consultarPeca(): #iniciando a função 
    print('1-consultar todas as peças\n'#retorna uma tabela com opções
          '2-consultar peça por codigo\n'
          '3-consultar peça por marca\n'
          '4-retornar')
    x = int(input('>> ')) #entrada da opção escolhida
    if x ==1: #se a opção for 1 
        for _ in peças: #inicia o laço 
            peça = _ #atribui o valor de cada item da lista a variavel peça
            print('-='*10)
            print(f'nome: ',peça['nome'],'\nmarca: ',peça['marca'],'\ncodigo: ',peça['codigo']) #retorna o nome da peça, marca e o codigo
    elif x == 2: #se a opção for 2
        y = int(input('digite o codigo: ')) #pede a entrada do codigo da peça
        verificador = 0 #inicia uma variavel sem valor
        for _ in peças: #inicia um laço 
            peça = _ #atribui o valor de cada item da lista a variavel peça
            if peça['codigo'] == y: #se a variavel peça for igual ao codigo 
                print(f'nome: ',peça['nome'],'\nidade: ',peça['marca'],'\ncodigo: ',peça['codigo'])#retorna o nome da peça, marca e o codigo 
                verificador = 1 #variavel verificador recebera o valor 1 
        if verificador == 0:#se a variavel verificador for igual a 0 
            print('codigo invalido')# retorna codigo invalido 
    elif x == 3: # se a opção for 3
        y = str(input('digite a marca: ')) #pede a entrada da marca 
        verificador = 0  #inicia uma variavel sem valor
        for _ in peças: #inicia um laço
            peça = _ #atribui o valor de cada item da lista a variavel peça
            if peça['marca'] == y: #se a variavel for igual a marca 
                print(f'nome:',peça['nome'],'\nmarca: ',peça['marca'],'\ncodigo: ',peça['codigo']) # retorna a peça 
                verificador = 1 #a variavel verificador recebe 1
        if verificador == 0:#se a variavel verificador for igual a 0
            print('codigo invalido') #retorna codigo invalido
def removerPeca(): #inicia a função
    y = int(input('digite o codigo da peça: ')) #pede o codigo da peça
    for _ in peças: #inicia um laço
        peça = _ #atribui o valor de cada item da lista a variavel peça
        if peça['codigo'] == y: #se o codigo da peça for igual ao da peça digitada  
            peças.remove(_)#remove a peça
    return peças #retorna a lista de peças
print('\033[36mBem Vindo ao Controle de Estoque da Bicicletaria do Kaio Colombaroli\033[m\n' 
      '1-cadastra peça\n'#retorna a tabela com opções
      '2-consultar peça\n'
      '3-remover peça\n'
      '4-sair')
acao = int(input('>>'))#pede a opção escolhida 
while True:#inicia o laço
    if acao == 1:#se a opção for 1 
        peças = cadastrarPeca() #usa a função
        print('-'*20) 
        print('1-cadastra peça\n'#retorna a tabela com opções
              '2-consultar peça\n'
              '3-remover peça\n'
              '4-sair')
        acao = int(input('>>')) #pede a opção escolhida 
    elif acao == 2:#se a opção for 2
        continuar = consultarPeca()#usa a função
        print('-'*20)
        print('1-cadastra peça\n'#retorna a tabela com opções
              '2-consultar peça\n'
              '3-remover peça\n'
              '4-sair')
        acao = int(input('>>')) #pede a opção escolhida 
    elif acao == 3:#se a opção for 3
        print('-'*20)
        peças = removerPeca()#usa a função
        print('1-cadastra peça\n'#retorna a tabela com opções
              '2-consultar peça\n'
              '3-remover peça\n'
              '4-sair')
        acao = int(input('>>')) #pede a opção escolhida 
    elif acao == 4: #se a opção for 4
        break#corta o laço
        
    