def qtde_vogais (texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "bcdfghjklmnpqrstvxywz":
            contador += 1
    return contador

texto = str(input("Digite um texto qualquer: "))

print(f"Seu texto possui {qtde_vogais(texto)} consoantes")
