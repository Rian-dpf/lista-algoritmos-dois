#9 - Faca um programa que apresente um menu de opções para o cálculo das seguintes operações
#entre dois números:

while True:

    def apresentaMenu():
        print("Escolha uma das opções abaixo: ")
        print("")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Saída")
        print("")

    def soma():
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual a: {soma}')

    def subtracao():
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        sub = n1 - n2
        print(f'A subtração entre {n1} - {n2} é igual a: {sub}')

    def multiplicacao():
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        mult = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é igual a: {mult}')

    def divisao():
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        div = n1 / n2
        print(f'A divisão entre {n1} / {n2} é igual a: {div}')

    apresentaMenu()
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        soma()
        print("Voltar ao menu principal?")
        print('')

        voltar_menu = input("S/N: ")

        if voltar_menu == 'S':
            pass
        else:
            break

    elif opcao == 2:
        subtracao()
        print("Voltar ao menu principal?")
        print('')

        voltar_menu = input("S/N: ")

        if voltar_menu == 'S':
            pass
        else:
            break

    elif opcao == 3:
        multiplicacao()
        print("Voltar ao menu principal?")
        print('')

        voltar_menu = input("S/N: ")

        if voltar_menu == 'S':
            pass
        else:
            break
        
    elif opcao == 4:
        divisao()
        print("Voltar ao menu principal?")
        print('')

        voltar_menu = input("S/N: ")

        if voltar_menu == 'S':
            pass
        else:
            break
        
    elif opcao == 5:
        break
    else:
        print("Digite uma opção válida!")
        opcao = int(input("Digite a opção desejada: "))