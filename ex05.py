#5 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva
#uma mensagem de erro se a opção for invalidar.

print('Escolha a opção: ')
print('')
print('1 - Soma de 2 números')
print('2 - Diferença entre 2 números')
print('1 - Produto entre 2 números')
print('1 - Divisão entre 2 números')
print('')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    soma = n1 + n2
    print(f'A soma de {n1} + {n2} é igual a: {soma}')
elif opcao ==2:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    if n1 > n2:
        diferenca = n1 - n2 
        print(f'A diferença entre {n1} e {n2} é igual a {diferenca}')
    else:
        diferenca = n2 - n1
        print(f'A diferença entre {n2} e {n1} é igual a {diferenca}')
elif opcao == 3:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    produto = n1 * n2
    print(f'O produto entre {n1} e {n2} é  igual a {produto}')
elif opcao == 4:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))

    divisao = n1 / n2
    print(f'O divisão entre {n1} e {n2} é  igual a {divisao}')
else:
    print('Digite uma opção válida!')