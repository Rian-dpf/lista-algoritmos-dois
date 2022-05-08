#6 - Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a
#tabela abaixo:

altura =  float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.6 and imc <=  24.9:
    print('Saudável!')
elif imc >= 25.0 and imc <= 29.9:
    print('Peso em excesso!')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade Grau I!')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade Grau II (Severa)!')
else:
    print('Obesidade Grau III (Mórbida)!')