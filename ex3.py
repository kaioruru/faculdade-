print('\033[36mBem vindo a transportadora do Kaio Colombaroli\033[m')
def dimensoesObejto():# cria um função 
    while True:
        while True: #cria um laço 
            try: #caso a a entrada seja uma str vai retornar um erro
                altura = int(input('digite a altura do objeto em cm: '))
            except:
                print('altura invalida')
            else: # se nao tiver erro corta o laço
                break
        while True:
            try:
                comprimento = int(input('digite o comprimento em cm: '))
            except:
                print('comprimento invalida')
            else:
                break
        while True:
            try:
                largura = int(input('digite a largura do objeto: '))
            except:
                print('largura invalida')
            else:
                break
        area = comprimento * altura * largura #cria um variavel com valor da area do objeto
        if area < 100000:#se area é menor que 100000 corta o laço
            break
        else:# se a area for maior que 100000 repete todo o laço
            print('dimensão invalida')
    if  area > 30000:
        valor = 50
    elif area > 10000:
        valor = 30
    elif area > 1000:
        valor = 20
    else:
        valor = 10
    return valor
def pesoObejto():
    while True: # cira um laço que se repete caso o peso seja maior que 30 kg
        while True: # cria um laço que se repete caso  o usuario não coloque um valor numerico
            try:
                peso = float(input('digite o peso do produto em kg: '))
            except:
                print('valor invalido')
            else:
                break
        if peso < 30:
            break
        else:
            print('peso não suportado')
    if peso > 10:
        mult = 3
    elif peso > 1:
        mult = 2
    elif peso > 0.1:
        mult = 1.5
    else:
        mult = 1
    return mult
def rotaObjeto():
    rotas = {'PP':1,'PC':1.2,'PS':1.5}#cria um dicionari com o multiplicador das rotas
    print('rotas\n'
          'PP| Piraqura -> Pinhais\n'
          'PC| Piraquara -> Curitiba\n'
          'PS| Piraquara -> São josé dos Pinhais')#retorna as rotas
    while True:#cria um laço que se repete caso nao seja digitada a rota certa 
        rota = str(input('digite a sua rota: ')).upper()
        if (rota == 'PP') or (rota == 'PC') or (rota == 'PS'): #caso a rota estiver certa corta o laço
            break
        else:
            print(f'a rota {rota} não e compativel')
    return rotas[rota]
#transformando o retorno das funções em variaveis
dimensão = dimensoesObejto()
peso = pesoObejto()
rota = rotaObjeto()
print(f'total a pagar:R${dimensão * peso * rota :.2f} (dimensão:{dimensão}*peso: {peso}*rota: {rota})')
