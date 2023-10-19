from textos.caracter import *

texto = str(input("Digite um texto qualquer: "))
while True:
    menu = int(input("""
                1 - Contar as vogais
                2 - Contar as consoantes
                3 - Contar o tamanho do texto
                4 - Transformar em maiúsculo
                5 - Transformar em minúsculo
                0 - Sair
    """))
    if menu == 1:
        print(contar_vogais(texto))
    elif menu == 2:
        print(contar_consoantes(texto))
    elif menu == 3:
        print(tamanho_da_palavra(texto))
    elif menu == 4:
        print(transformar_em_maiusculo(texto))
    elif menu == 5:
        print(transformar_em_minusculo(texto))
    elif menu == 0:
        break
    else:
        print("Opção inválida")





