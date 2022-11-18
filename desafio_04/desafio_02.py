# A PDA quer verificar se o Tiago está qualificado para tirar férias. Para estar em condições, os seguintes requisitos devem ser satisfeitos:
# - Ter trabalhado no mínimo 12 meses completos.
# - Ter disponibilidade de tirar férias entre dezembro e janeiro.
# Faca um algoritmo que valide ou não essas duas opções para saber se o Tiago pode tirar férias. O programa deverá escrever a mensagem “Tiago pode sair de férias “ ou  “Tiago não pode sair de férias”.

meses = int(input('Tiago, quantos meses você trabalhou nesse ano?'))

disponibilidade = input('Quais meses você tem disponibilidade?')
if meses >= 12 and disponibilidade == 'dezembro' and'janeiro':
    print('Tiago pode sair de férias!')
else:
        print('Tiago não pode sair de férias!')