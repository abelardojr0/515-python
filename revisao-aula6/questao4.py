lista = []
for i in range(10):
    numero = float(input("Digite um número: "))
    lista.append(numero)

multiplicados = list(map(lambda numero : numero * 2, lista))

print(multiplicados)