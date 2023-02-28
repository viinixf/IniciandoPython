
# print('Digite a altura da pessoa: ')
# valor1 = float(input())
# print('Digite o gênero da pessoa: ')
# genero = int(input())
# homem = 72.7 * valor1 - 58
# mulher = 62.1 * valor1 - 44.7
# if genero == 1:
#     print('O peso ideal para homem é: ', homem)
# if (genero == 2):
#     print('O peso ideal para mulher é: ', mulher)
# if (genero != 1 & genero != 2):
#     print('Gênero não encontrado')

##############################################################################
# altura = float(input("Informe a altura: "))
# genero = int(input("Informe o genero, usando 1 para feminino e 2 masculino"))
# if genero == 1:
#     peso = 62.1 * altura - 44.7
# if genero == 2:
#     peso = 72.7 * altura - 58
# print("Peso ideal", peso)
##############################################################################

# horarioInicialHora = print(
#     'Digite o horário de início do jogo somente horas: ')
# horarioInicialMinuto = print(
#     'Digite o horário de início do jogo somente minutos: ')
# horarioFinalHora = print('Digite o horário do fim do jogo somente horas: ')
# horarioFinalMinutos = print(
#     'Digite o horário do fim do jogo somente minutos: ')

# horarioInicial = horarioInicialHora * 60 + horarioInicialMinuto
# horarioFinal = horarioFinalHora * 60 + horarioFinalMinutos

# if horarioInicial < horarioFinal:
#     duracao = horarioFinal - horarioInicial
# else : duracao = 24 * 60 - horarioInicial + horarioFinal

# print('Horas', duracao//60)
# print('Minutos: ', duracao%60)
##############################################################################


# print('Digite o número inteiro de quatro digítos: ')
# numero = int(input())
# if numero >= 1111 & numero <= 9999 : 
#     a = (numero // 1000) * 1000
#     b = numero % 1000
#     verificaCapicua = a + b
#     if verificaCapicua == numero : print('O número capicua é: ', verificaCapicua)
# else : print('Número não é capicua')
##############################################################################


# print('Digite o primeiro valor')
# v1 = int(input())
# print('Digite o segundo valor')
# v2 = int(input())
# print('Digite o terceiro valor')
# v3 = int(input())

# maior = v1
# if v2 > maior : maior = v2
# if v3 > maior : maior = v3

# menor = v1
# if v2 < menor : menor = v2
# if v3 < menor : menor = v3

# meio = v1 + v2 + v3 - maior - menor

# print('Ordem crescente: ', menor, meio, maior)

##############################################################################