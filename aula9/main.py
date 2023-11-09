from tkinter import *

telinha = Tk()
telinha.title("Aula Infinity")
telinha.configure(bg="#ff60a9")
telinha.geometry("400x300")



def saudacao():
    sexo = sexo_input.get()
    nome = nome_input.get()

    if sexo.upper() == "F":
        resultado.configure(text=f"Seja vem vinda {nome}")
    elif sexo.upper() == "M":
        resultado.configure(text=f"Seja vem vindo {nome}")
    else:
        resultado.configure(text=f"Seja vem vinde {nome}")

    sexo_input.delete(0, END)
    nome_input.delete(0, END)



titulo = Label(text="Título da telinha", bg="#ff60a9")
titulo.pack()

nome_texto = Label(text="Digite o seu nome: ", bg="#ff60a9")
nome_texto.pack()

nome_input = Entry(width=18)
nome_input.pack()

sexo_texto = Label(text="Digite seu sexo [M | F]", bg="#ff60a9")
sexo_texto.pack()

sexo_input = Entry()
sexo_input.pack()

resultado = Label(text="", bg="#ff60a9")
resultado.pack()

teste = ""


botao = Button(telinha, text="Enviar", command=saudacao)
botao.pack()



telinha.mainloop()