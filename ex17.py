#17 - Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A
#função deve imprimir todos os elementos da lista numerando-os.

def imprimiNumerando(lista):
    for i in range(0, len(lista)):
      print(f'{lista[i]} : {i}')

imprimiNumerando([1,5,7])