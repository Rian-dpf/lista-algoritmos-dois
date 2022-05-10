#13 - Agora, faça uma função de acordo com a média informe o status do aluno de acordo com a
#tabela a seguir:

def media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def statusAluno(media_aluno):

    if media_aluno > 6:
        print('Aprovado!')
    elif media_aluno >= 4 and media_aluno <= 6:
        print('Verificação suplementar!')
    else:
        print('Reprovado!')

media_aluno = media(0,2,9)

statusAluno(media_aluno)