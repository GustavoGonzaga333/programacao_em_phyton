
# nome=input('Digite Seu Nome:')
# idade=input('Digite Sua Idade:')
# endereco=input('Digite Seu Endereco:')


# dados_cadastrados={}

# dados_cadastrados['nome']=nome
# dados_cadastrados['idade']=idade
# dados_cadastrados['endereço']=endereco
# print(dados_cadastrados)


ecommerce = {
'livros': 360,
'tablet': 1000,
'fone': 300,
'formas_pag':['pix','cartao','dinheiro',]
}

escolha1=input('digite o nome do produto')
escolha2=input('digite o nome do produto')
escolha3=input('digite o nome do produto')
print(ecommerce['formas_pag'][0])
print(ecommerce['formas_pag'][1])
print(ecommerce['formas_pag'][2])

valores = []
carrinho = []

carrinho.append(escolha1)
carrinho.append(escolha2)
carrinho.append(escolha3)

valores.append(ecommerce[escolha1])
valores.append(ecommerce[escolha2])
valores.append(ecommerce[escolha3])

soma=sum(valores)
metodo_pagamento=int(input("Qual o metodo de pagamento que voce deseja"))
forma=ecommerce['formas_pag'][metodo_pagamento]
print(forma)
print('total', soma)
