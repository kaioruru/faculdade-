print('=-'*20+'#'+'-='*20 )
print('\033[36mBem vindo a loja do Kaio Colombaroli\033[m')
valor_produtos=float(input('Valor do produto:')) #entrada do valor do produto
quantidade = int(input('Quantidade de produtos:')) #entrada da quantidade de produtos
#se a quantidade for maior ou igual a 1000
if quantidade >= 1000:
    print(f'valor a pagar sem desconto: R${valor_produtos*quantidade :.2f}') #saida do valor sem desconto
    print(f'valor a pagar com desconto: R${(valor_produtos*quantidade)/0.15 :.2f} |Desconto de 15%') #saida do valor com desconto
#se a quantidade estiver entre 100 e 999
elif quantidade >=100:
    print(f'Valor a pagar sem desconto: R${valor_produtos*quantidade :.2f}') 
    print(f'Valor a pagar com desconto: R${(valor_produtos*quantidade)/0.1 :.2f} |Desconto de 10%') 
#se a quantidade estiver entre 10 e 99
elif quantidade >=10:
    print(f'Valor a pagar sem desconto: R${valor_produtos*quantidade :.2f}')
    print(f'Valor a pagar com desconto: R${(valor_produtos*quantidade)/0.05 :.2f} |Desconto de 5%') 
else:
    print(f'Valor a pagar: R${valor_produtos*quantidade :.2f} |\033[31mA quantidade nao entra como atacado \033[m')
print('=-'*20+'#'+'-='*20 )