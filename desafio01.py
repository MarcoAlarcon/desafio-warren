from funcoes import reverso

n = 1
reversivel = 0

while n < 100000:

    #Criando uma lista do numero reverso para validar se existe um 0 na primeira posição do numero. ex. n=31 listaR = [1,3]
    listaR = list(reversed([int(x) for x in str(n)])) 

    #Funcao que atribui o valor de n ao contrario na variavel reversivel. ex. n=31 reversivel=13
    reversivel = reverso(n) 

     # Verificando se a primeira posição da listaR contem o valor 0. Verifico apenas a listaR porque nesse cenario não tem como a variavel n começar com 0.
    if listaR[0] != 0:
        # Verificação de valores impares.
        if (n + reversivel) % 2 != 0: 
            print(f"{n} + {reversivel} = {n+reversivel} - impar.")
    n+=1