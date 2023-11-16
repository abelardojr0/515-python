from tkinter import *

janela = Tk()
janela.title("Place")
janela.geometry("350x350")

nome_texto = Label(text="Digite seu nome")
nome_texto.place(x=5, y=5)

nome_input = Entry()
nome_input.place(x=100, y=5)

botao = Button(text="Enviar", width=30)
botao.place(x=5, y=30)



janela.mainloop()