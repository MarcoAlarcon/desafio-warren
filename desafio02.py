from operator import length_hint
import os

#Coletando quantos alunos são necessarios para começar a aula

alunos = int(input("Informe a quantidade minima para começar a aula: "))

#Criando minha lista de horarios, e as variaveís que vão ajudar na verificação de informações.
horariosChegada = []
aux1 = True
aux2 = 1
escolha = 0

#loop para incluir os horarios de chegada dos alunos

while aux1 == True:
    #inclui o horario de chegada do aluno na lista de horarios
    horariosChegada.append(input(f'Horario de chegada do {alunos - alunos + aux2}° aluno: '))
    escolha = int(input("Gostaria de inserir mais um horario de chegada?\n1 - sim\n2 - nao\nInforme a opção desejada: "))
    if escolha != 1 and escolha != 2:
        print("Favor inserir um valor válido.")
    if escolha == 2:
        break
    aux2 +=1
    os.system('cls')


#verificação da lista de horarios de chegada. Se a lista conter menos horarios do que o numero minimo de alunos, a aula será cancelada.
if len(horariosChegada) < alunos:
    print("Aula cancelada")
else:   
    print("Aula normal")