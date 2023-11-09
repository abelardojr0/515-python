from tkinter import *

janelinha = Tk()
janelinha.title("Contador de vogais")
janelinha.geometry("400x400")


def contar():
    frase = frase_input.get()
    
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    for letra in frase:
        if letra.lower() == "a":
            contador_a += 1
        elif letra.lower() == 'e':
            contador_e += 1
        elif letra.lower() == 'i':
            contador_i += 1
        elif letra.lower() == 'o':
            contador_o += 1
        elif letra.lower() == 'u':
            contador_u += 1

    resultado.configure(text=f"""
    Quantidade de vogais:
    a - {contador_a}
    e - {contador_e}
    i - {contador_i}
    o - {contador_o}
    u - {contador_u}
""")

frase_texto = Label(text="Digite uma frase:").pack()

frase_input = Entry()
frase_input.pack()

resultado = Label(text="")
resultado.pack()

botao = Button(janelinha, text="Contar", command=contar)
botao.pack()


janelinha.mainloop()