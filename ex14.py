#14 - Escreva uma função para imprimir o nome e salário de um funcionário usando as seguintes
#condições.
#Deve aceitar o nome e o salário do funcionário.
#Se o salário estiver faltando na chamada de função, atribua o valor padrão 9000 ao salário.

def imprimiNomeSalario(nome, salario=9000):
    print(nome, salario)

imprimiNomeSalario('Rian')