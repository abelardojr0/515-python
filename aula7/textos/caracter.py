def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

def contar_consoantes(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "bcdfghjklmnpqrstvxywz":
            contador += 1
    return contador

def tamanho_da_palavra(texto):
    return len(texto)

def transformar_em_maiusculo(texto):
    return texto.upper()

def transformar_em_minusculo(texto):
    return texto.lower()