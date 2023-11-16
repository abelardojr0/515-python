from tkinter import *

janela = Tk()
janela.title("Grid")
janela.geometry("300x300")

nome_texto = Label(text="Digite seu nome")
nome_texto.grid(row=1, column=1)

nome_input = Entry()
nome_input.grid(row=1, column=2)

botao = Button(janela, text="Enviar", width=30)
botao.grid(row=2, column=1, columnspan=2)

janela.mainloop()
