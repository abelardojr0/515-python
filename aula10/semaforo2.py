from tkinter import *

janela = Tk()
janela.title("Semáforo 2")
janela.geometry("200x400")


def vermelho():
    resultado.configure(text="Pare! Sinal fechado")
def amarelho():
    resultado.configure(text="Atenção! Reduza a velocidade")
def verde():
    resultado.configure(text="Acelera! Sinal aberto")

botao_vermelho = Button(width=10, bg="red", command=vermelho)
botao_vermelho.pack(pady=10)

botao_amarelo = Button(width=10, bg="yellow", command=amarelho )
botao_amarelo.pack(pady=10)

botao_verde = Button(width=10, bg="green", command=verde)
botao_verde.pack(pady=10)

resultado = Label(text="")
resultado.pack()


janela.mainloop()