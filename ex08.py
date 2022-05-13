#8 - Faça um programa que receba dois números. Calcule e mostre:
#• A soma dos números pares desse intervalo de números, incluindo os números digitados;
#• A multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

soma = 0
mult = 1

for i in range(num_1, num_2 + 1):
    if i % 2 == 0:
        soma += i
    else:
        mult *= i

print('A soma dos pares é igual a: ', soma)
print('A multiplicação dos ímpares é igual a: ', mult)