from tkinter import *

caixinha = Tk()
caixinha.title("Semáforo")
caixinha.geometry("200x400")

def checar_cor():
    cor = cor_input.get().lower()

    if cor == "verde":
        resultado.configure(text="Acelera", fg="green")
    elif cor == "amarelo":
        resultado.configure(text="Atençao", fg="yellow")
    elif cor == "vermelho":
        resultado.configure(text="Pare", fg="red")
    else:
        resultado.configure(text="Cor inválida", fg="blue")


cor_texto = Label(text="Digite um cor:").pack()

cor_input = Entry()
cor_input.pack()

resultado = Label(text="")
resultado.pack()

botao = Button(caixinha, text="Enviar", command=checar_cor)
botao.pack()


caixinha.mainloop()