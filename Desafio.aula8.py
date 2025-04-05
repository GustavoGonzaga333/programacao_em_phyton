
ecommerce = {
'simples': 100,
'duplo' : 150,
'luxo' : 250,

}

# classes= quarto_simples,quarto_luxo,quarto_duplo

nomeClient1= input ('Digite seu nome:')
TipoQuarto = input('Selecione Seu Quarto:')
DiasAlocado= int(input ("Vai ficar quantos dias?"))
nomeClient2= input ('Digite seu nome:')
TipoQuarto2 = input('Selecione Seu Quarto:')
DiasAlocado2= int(input ("Vai ficar quantos dias?"))

quartos = [TipoQuarto,TipoQuarto2]

print(nomeClient1,TipoQuarto,nomeClient2,TipoQuarto2)
reservas = (ecommerce[TipoQuarto])
valores = (ecommerce[TipoQuarto]*DiasAlocado)+ecommerce[TipoQuarto2]*DiasAlocado2
print("R$", valores)
print(quartos)