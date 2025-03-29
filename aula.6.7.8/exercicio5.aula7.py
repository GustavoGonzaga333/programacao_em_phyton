carros=['corsa','fiesta','astra']
valor=(3000,4500,7600)
print('carros',carros)

valor_compra=[]
valor_total=[]

escolha1= int(input('ID do Produto'))
escolha2= int(input('ID do Produto'))
escolha3= int(input('ID do Produto'))

Simulação= [carros[escolha1], carros[escolha2],carros[ escolha3]]
valor_total= [valor[escolha1], valor[escolha2],valor[ escolha3]]

total= valor_total[0] + valor_total[1] + valor_total[2]
print('Seus produtos', Simulação)
print('Valores dos seus produtos', valor_total) 

print('*******************************************')



print('valor total',total )


print('Obrigada volte sempre')