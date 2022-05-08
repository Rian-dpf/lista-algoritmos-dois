#3 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela a
#média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso
#a nota não possua um valor valido, este fato deve ser informado ao usuário e o programa termina.

n1 = float(input('Digite sua primeira  nota: '))
n2 = float(input('Digite sua segunda  nota: '))

media = (n1 + n2) / 2

if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
    print(f'Sua média é igual a: {media}')
else:
    print("Nota inválida, digite uma nota entre 0 e 10.")