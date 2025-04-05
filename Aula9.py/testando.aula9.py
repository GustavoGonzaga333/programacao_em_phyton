import random


lista  = [3,2,1]


for chances in lista:
    aleatorio =  random.randint(1,2)
    chute = int(input('Escolha um numero: '))  
    if aleatorio == chute:
        print('Ganhou Jogo o número é', aleatorio)
        break
    else:       
        
        print('Errou Feio número foi, ', aleatorio)
        print('Você tem', chances-1, 'chances')  
else:
    print('Suas chances se esgotaram', chances)   
    