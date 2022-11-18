#4.1 Os alunos do PdA estão sendo avaliados, para passar para o próximo ciclo, deverão  tirar 7 na média.

#-Se o aluno tirar maior ou igual a 7 ele está aprovado.
#-Se o aluno tiver nota 6 e for participativo, irá para recuperação.
#-Senão, será reprovado.
#Faça um algoritmo que auxilie a avaliar a nota dos alunos.

nota = int(input('Qual a sua nota:'))
participacao = int(input('Qual a sua frequencia de participação de 1 á 10? '))

if nota >= 7 and nota <10:
    print('Você passou!')
elif nota == 6 and participacao >= 5: 
   print('Você está de recuperação!')
else : 
    print('Você reprovou!')
