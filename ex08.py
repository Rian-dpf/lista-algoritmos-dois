#8 - Faça um programa que receba dois números. Calcule e mostre:
#• A soma dos números pares desse intervalo de números, incluindo os números digitados;
#• A multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

diferenca  = num_1 - num_2

if num_1 > num_2:
    if diferenca % 2 == 0:
        for i in range(num_2, num_1 + 1):
            if i % 2 != 0:
                continue
            else:
                teste = []
                teste.append(i)
                print(teste)