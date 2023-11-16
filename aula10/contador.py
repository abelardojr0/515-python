from tkinter import *

janela = Tk()
janela.title("Contador de letras")
janela.geometry("400x400")

def contar_letras():
    frase = frase_input.get()
    contador_vogal = 0
    contador_consoante = 0
    contador_espaco = 0

    for letra in frase:
        if letra.lower() in "aeiou":
            contador_vogal += 1
        elif letra.lower() in "bcdfghjklmnpqrstvxywz":
            contador_consoante += 1
        elif letra == " ":
            contador_espaco += 1

    resultado.configure(text=f"""
                A frase '{frase}' contém:
                        {contador_vogal} vogais
                        {contador_consoante} consoantes
                        {contador_espaco} espaços
                """)
    frase_input.delete(0, END)

frase_texto = Label(text="Digite uma frase").pack()

frase_input = Entry()
frase_input.pack()

resultado = Label(text="")
resultado.pack()

botao = Button(janela, text="Contar", command=contar_letras)
botao.pack()

janela.mainloop()