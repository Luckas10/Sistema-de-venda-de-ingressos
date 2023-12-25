import tkinter as tk

def mudar_texto():
    novo_texto = "Novo Texto!"
    canvas.itemconfig(texto, text=novo_texto)

# Criar a janela principal
janela = tk.Tk()
janela.title("Mudar Texto no Canvas")

# Criar um canvas
canvas = tk.Canvas(janela, width=200, height=100)
canvas.pack()

# Criar um texto no canvas
texto = canvas.create_text(100, 50, text="Texto Inicial", font=("Arial", 12))

# Criar um botão para mudar o texto
botao_mudar = tk.Button(janela, text="Mudar Texto", command=mudar_texto)
botao_mudar.pack()

# Iniciar o loop principal da aplicação
janela.mainloop()
