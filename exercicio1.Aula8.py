# import random

# numero = random.randint(1,20)
# chute = int(input("Faça sua Escolha"))

# if numero == chute:
#     print('Acertou em cheio!', numero)
# else:
#     print('errou feio', numero)


# ////////////////////////////////////////////////////////

# carta_motorista = bool(input('Possui CNH?'))
# idade=int(input('Digite sua Idade'))

# if carta_motorista == 'sim' and idade >=18:
#     print ('habilitado')
# else:
#     print('Não pode dirigir')
 

#//////////////////////////////////////////////////


import random 

alunos = {
        'Ana':[10,9,8,5.5,3,7,10],
        'Fernanda':[1,2,3,6,5,2,7],
        'Leo':[10,10,10,10,10,10,10]
     }

# média de notas soma() / len()
# maior média max()
# maior nota de cada aluno max()
# mediana ordenar a lista - meio  
# amplitude 
# moda 


NOTAS_ANA = alunos['Ana']
maior_nota_ana = max(NOTAS_ANA)
NOTAS_FERNANDA = alunos['Fernanda']
maior_nota_fernanda = max(NOTAS_FERNANDA)
NOTAS_LEO =alunos['Leo']
maior_nota_leo = max(NOTAS_LEO)

print(f'MAIOR NOTA ANA - {maior_nota_ana}\nMAIOR NOTA FERNANDA - {maior_nota_fernanda}\nMAIOR NOTA LEO - {maior_nota_leo} ' )

media_ana = sum(alunos['Ana'])/len(alunos['Ana'])
media_fernanda = sum(alunos['Fernanda'])/len(alunos['Fernanda'])
media_leo = sum(alunos['Leo'])/len(alunos['Leo'])

medias = [media_ana, media_fernanda,media_leo]
media_total = sum(medias) / len(medias)
print('MÉDIA GERAL', media_total)


lista_nomes = ['Ana','Fernanda','Leo']
maior = max(medias)
indice = medias.index(maior)
print(lista_nomes[indice], 'Maior Media', maior)


NOTAS_ANA.sort()
print(f'mediana  ana- {NOTAS_ANA[3:4]}')
print(f'amplitude  ana- {max(NOTAS_ANA) - min(NOTAS_ANA)}')
NOTAS_FERNANDA.sort()
print(f'mediana  fernanda- {NOTAS_FERNANDA[3:4]}')
print(f'amplitude  fernanda- {max(NOTAS_FERNANDA) - min(NOTAS_FERNANDA)}')
NOTAS_LEO.sort()
print(f'mediana  leo - {NOTAS_LEO[3:4]}')
print(f'amplitude  leo- {max(NOTAS_LEO) - min(NOTAS_LEO)}')

moda = max(set(NOTAS_ANA), key=NOTAS_ANA.count)
print('moda ANa', moda)

moda = max(set(NOTAS_FERNANDA), key=NOTAS_FERNANDA.count)
print('moda Fernanda', moda)

moda = max(set(NOTAS_LEO), key=NOTAS_LEO.count)
print('moda Leo', moda)

