#15 - Escreva uma função Python que receba uma lista e retorne uma nova lista com elementos
#exclusivos da primeira lista.

numeros = [1, 2, 2, 3, 3, 4, 5]


def pegaNumerosUnicos(numeros):

    lista_numeros_unicos = []

    numeros_unicos = set(numeros)

    for numero in numeros_unicos:
        lista_numeros_unicos.append(numero)

    return lista_numeros_unicos


print(pegaNumerosUnicos(numeros))
