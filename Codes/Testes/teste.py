import tkinter as tk

class App:
    def __init__(self):
        self.janela2 = "Nada"
        self.janela_primaria()

    def janela_primaria(self):
        if self.janela2 == "Nada":
            pass
        else:
            self.janela2.destroy()
        self.janela = tk.Tk()

        self.botao = tk.Button(self.janela, text = 'Ir para nova janela', command = self.janela_secundaria)
        self.botao.grid(row = 0, column = 0)

        self.janela.mainloop()


    def janela_secundaria(self):
        self.janela.destroy()
        self.janela2 = tk.Tk()
        self.janela2.title('janela nova')
        self.label_nome = tk.Label(self.janela2, text = "Nome")
        self.label_nome.grid(row = 0, column = 0 )
        self.botao_voltar = tk.Button(self.janela2, text = 'Fechar a janela2', command = self.janela_primaria)
        self.botao_voltar.grid(row = 1, column = 0)

app = App()