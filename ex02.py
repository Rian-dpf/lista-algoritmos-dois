#2 - Escreva um programa que, dados dois números inteiros fornecidos pelo usuário, mostre na tela o
#maior deles, assim como a diferença existente entre ambos.

num_1 = int(input("Digite um número inteiro: "))
num_2 =  int(input("Digite outro número inteiro: "))

if num_1 > num_2:
    diferenca = num_1 - num_2
    print(f'{num_1} é maior  que {num_2}')
    print(f'A diferença entre {num_1} e {num_2} é de {diferenca}')
else:
    diferenca = num_2 - num_1
    print(f'{num_2} é maior  que {num_1}')
    print(f'A diferença entre {num_2} e {num_1} é de {diferenca}')
