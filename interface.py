import tkinter as tk


def ver_disciplinas():
    print("clicou em ver disciplinas")

janela = tk.Tk()
janela.title("Meu Organizador")

botao1 = tk.Button(janela, text="Ver disciplinas", command=ver_disciplinas)
botao1.pack()

botao2 = tk.Button(janela, text="Sair", command=janela.destroy)
botao2.pack()

janela.mainloop()