from itertools import combinations_with_replacement
from funcoes import tratativaVetor

n = int(input("Informe o numero:"))
v = list(input("Informe os numeros do vetor separados com uma virgula: "))

#tratativa para retirar as virgulas desnecessarias da variavel v e transformar ela em um vetor de numeros inteiros.
tratativaVetor(v)
v=list(map(int,v))

#Iterator que vai representar o tamanho do vetor de combinações, sempre buscando o menor numero de ocorrencias possiveis.
tamanhoArray = 2

#Variavel para armazenar as combinações de vetores que vao ser criados.
array2D = [[]] 

#Onde vai ser guardado os vetores que vão ser mostrados em tela.
arrayFinal = [] 


while len(arrayFinal) == 0:
    #Criando as combinacoes do vetor baseado nos numeros que foram passados da variavel v.
    array2D = combinations_with_replacement(v,tamanhoArray)

    #A funcao combinations_with_replacemnte retorna um objeto, é preciso fazer a tratativa dos dados do objeto para poder trabalhar com as validações. 
    temp = list(map(list, array2D))

    #Percorrendo a lista com as combinações criadas e verificando quais delas, quando somadas, são iguais ao numero informado na variavel n.
    for i in range(len(temp)):
        if sum(temp[i]) == 10:
            arrayFinal.append(temp[i])
    tamanhoArray += 1

print(f'\nNumero informado = {n}')
print(f'Vetores criados com o menor número de elementos:')
for i in range(len(arrayFinal)):
    print(arrayFinal[i])