#4 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for
#maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo
#concedido.

salario = float(input('Digite o seu salário: '))
prestacao_emprestimo  = float(input('Digite o valor da  prestação do seu empréstimo: '))

vinte_salario = (20 / 100 ) * salario

if prestacao_emprestimo > vinte_salario:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')