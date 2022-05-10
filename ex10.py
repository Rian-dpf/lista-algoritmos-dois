#10 - O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia
#da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o
#programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado
#pelo usuário, conforme o exemplo abaixo:

preco_pao = float(input('Qual o preço do pão hoje: '))
preco_pao_vezes_50 = preco_pao * 50

cont = 1

while cont <= 50:
    tabela = preco_pao + preco_pao

    cont += 1

    print(tabela)