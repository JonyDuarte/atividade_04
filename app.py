# declaração de variáveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# Inicia o loop
while True:
    print("Sala 1 - Laranja Mecânica - 18 anos")
    print("Sala 2 - Onde os fracos não tem vez - 16 anos")
    print("Sala 3 - Meu malvado Favorito 4 - Livre")

    # recebe o número da sala desejada
    sala = input("Informe a sala desejada: ")

    # verifica a sala inserida pelo usuário
    match sala:
        case "1":
            idade_minima = 18
        case "2":
            idade_minima = 16
        case "3":
            idade_minima = 0
        # default (valor inválido)
        case _:
            print("Sala inexistente.")
            continue
    # verifica a idade do usuário e a classificação do filme
    if idade >= idade_minima:
        print(f"Entrada de {nome} autorizada. Bom filme!")
        break
    else:
        print(f"Entrada de {nome} não autorizada.")
        print(f"Favor escolher outro filme.")
        continue 

              
