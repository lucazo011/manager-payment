print('{:=^40}'.format('Terabyte SHOP'))
preco = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO 
    [1] á vista dinheiro/cheque
    [2] á vista cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão''')
opcao = int(input('Qual a opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(
        'Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas Parcelas?'))
    parcela = total / totalparc
    print('Essa compra será parcelada em {}x de R${:.2f} COM JUROS'.format(
        totalparc, parcela))
else:
    total = preco
    print('OPÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(
    preco, total))
