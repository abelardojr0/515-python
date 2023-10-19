par_ou_impar = lambda numero : "é par" if numero % 2 == 0 else "é ímpar"

numero = int(input("Digite um número: "))

print(par_ou_impar(numero))