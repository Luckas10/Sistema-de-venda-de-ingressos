from gui import *


while True:
    numero = int(input("Informe: "))

    if numero == 1:
        numero = int(input("Informe: "))
        janela1 = Janela1()
    elif numero == 2:
        janela1.window.destroy()
        janela2 = Janela2()
    elif numero == 0:
        break
