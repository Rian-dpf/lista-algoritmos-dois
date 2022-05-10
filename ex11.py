#11 - Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado
#pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, os valoresinicial
#e final devem ser informados também pelo usuário, conforme exemplo abaixo:

tabuada = int(input('Montar a tabuada de: '))
valor_inicial = int(input('Começar por: '))
valor_final = int(input('Terminar em: '))

print('')
print(f'Vou montar a tabuada e {tabuada} começando em {valor_inicial} e terminando em {valor_final}:')
print('')

while valor_inicial <= valor_final:
    print(tabuada, 'X', valor_inicial, ' = ' ,tabuada * valor_inicial)

    valor_inicial += 1