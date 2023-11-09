from tkinter import *

janela = Tk()
janela.title("Média")
janela.geometry("300x300")


def calcular():
    nota1 = float(nota1_input.get())
    nota2 = float(nota2_input.get())
    nota3 = float(nota3_input.get())
    media = (nota1 + nota2 + nota3) / 3

    if media == 10:
        resultado.configure(text="Tu é brabo", fg="blue")
    elif media >=7 and media <10:
        resultado.configure(text="Aprovado", fg="green")
    elif media < 7 and media >= 0:
        resultado.configure(text="Reprovado", fg="red")
    else:
        resultado.configure(text="Notas inválidas", fg="yellow")



        


nota1_texto = Label(text="Digite a primeira nota: ")
nota1_texto.pack()

nota1_input = Entry()
nota1_input.pack()

nota2_texto = Label(text="Digite a segunda nota: ")
nota2_texto.pack()

nota2_input = Entry()
nota2_input.pack()

nota3_texto = Label(text="Digite a terceira nota: ")
nota3_texto.pack()

nota3_input = Entry()
nota3_input.pack()

resultado = Label(text="")
resultado.pack()


botao = Button(janela, text="Calcular Média", command=calcular)
botao.pack()


janela.mainloop()