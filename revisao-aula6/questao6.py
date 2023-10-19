def media (lista):
    return sum(lista) / len(lista)

# def media (lista):
#     soma = 0
#     for numero in lista:
#         soma = soma + numero
#     media = soma / len(lista)
#     return media


quantidade = int(input("Digite a quantidade de números que você vai inserir na lista: "))

lista = []
for i in range(quantidade):
    numero = float(input("Digite um número: "))
    lista.append(numero)

print(media(lista))
