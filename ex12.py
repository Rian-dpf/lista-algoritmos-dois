#12 - Fazer uma função que receba três notas de um aluno, e que retorne a média dessas 3 notas.

def media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    print(f'A média é igual: {media: .1f}')

media(8.4,9,9)