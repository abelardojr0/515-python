from tkinter import *

janela = Tk()
janela.title("Verificador de Senhas")
janela.geometry("200x200")

def verificar():
    senha = senha_input.get()
    temLetra = False
    temNumero = False

    if len(senha) >= 8:
        for caracter in senha:
            if caracter.lower() in "abcdefghijklmnopqrstuvxywz":
                temLetra = True
            elif caracter in "0123456789":
                temNumero = True
        if temNumero == True and temLetra == True:
            resultado.configure(text="Senha válida")
        else:
            resultado.configure(text="Senha inválida")
    else:
        resultado.configure(text="Senha inválida")

senha_texto = Label(text="Digite uma senha").pack(side="right", padx=5, pady=10)

senha_input = Entry()
senha_input.pack(padx=5, pady=10)

botao = Button(janela, text="Verificar", command=verificar)
botao.pack()

resultado = Label(text="")
resultado.pack()


janela.mainloop()