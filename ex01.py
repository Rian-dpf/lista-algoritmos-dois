#1 - Leia um número real fornecido pelo usuário. Se o número for positivo imprima a raiz quadrada. Do
#contrário, imprima o número ao quadrado.
import math

num_real = int(input("Digite um númro real qualquer: "))

if num_real >= 0:
    print(f'A raiz quadrada de {num_real} é: ', math.sqrt(num_real))
else:
    print(f'O quadrado de {num_real} é: ', num_real * num_real)