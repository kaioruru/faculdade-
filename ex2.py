# dicionari pra retornar oque o cliente pediu
nome_produtos = {
    100:'Cachorro Quente no valor de 9,00',
    101:'Cachorro Quente Duplo no valor de 11,00',
    102:'Z-Egg no valor de 12,00',
    103:'X-Salada no valor de 12,00',
    104:'X-Bacon no valor de 14,00',
    105:'X-Tudo no valor de 17,00',
    200:'Refrigerante Lata no valor de 5,00',
    201:'Chá Gelado no valor de 4,00'
}
valor_produtos={100:9,101:11,102:12,103:12,104:14,105:17,200:5,201:4}#dicionario com o valor dos produtos para a soma
#retornando o cardapio
print('\033[36mBem vindo a lanchonete do Kaio Colombaroli\033[m') #identificador
print('-='*7,'\033[7mcardápio\033[m','=-'*7)
print('|codigo |      Descrição      | valor |\n'
      '|   100 |   Cachorro Quente   |  9,00 |\n'
      '|   101 |Cachorro Quente Duplo| 11,00 |\n'
      '|   102 |         Z-Egg       | 12,00 |\n'
      '|   103 |       X-Salada      | 12,00 |\n'
      '|   104 |        X-Bacon      | 14,00 |\n'
      '|   105 |        X-Tudo       | 17,00 |\n'
      '|   200 |  Refrigerante Lata  |  5,00 |\n'
      '|   201 |     Chá Gelado      |  4,00 |\n'
      )
valor_a_pagar = 0
while True: #iniciando o laço
    x = int(input('entre com o código do pedido: '))
    if (x>=100)and(x<=105) or (x>=200)and(x<=201):#verificando se o a entrada e igual a o codigo do pedido
        print(f'você pediu um {nome_produtos[x]}')
        valor_a_pagar += valor_produtos[x] #somando o valor dos produtos 
        repetir = input('deseja pedir algo mais?(S/N):').upper()
        if repetir=='N': #se a pessoa nao pedir mais nada 
            print(f'O total a ser pago é : \033[32mR${valor_a_pagar :.2f}\033[m')#retorna o valor a pagar em verde
            break
    else:
        x = int(input('entre com o código do pedido: '))
        print('erro')