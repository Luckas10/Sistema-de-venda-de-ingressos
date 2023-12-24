from Login .code_login import *
from Register .code_register import *
from Dashboard .dashboard import *

import tkinter as tk


class App:
    def __init__(self):
        self.screen_register = "Nada"
        self.tela_de_login()

    def tela_de_login(self):
        if self.screen_register == "Nada":
            pass
        else:
            self.screen_register.window.destroy()

        self.screen_login = Screen_Login()

        self.screen_login.button_1["command"] = self.tela_de_cadastro

        self.screen_login.window.mainloop()

    def tela_de_cadastro(self):
        self.screen_login.window.destroy()

        self.screen_register = Screen_Register()

        self.screen_register.button_1["command"] = self.tela_de_login

        self.screen_register.window.mainloop()

    def tela_de_compra_concluida(self):
        self.screen_login.window.destroy()

        self.screen_dashboard = App()

        self.screen_dashboard.button_1["command"] = self.tela_de_cadastro #Falta mudar muita coisa, tá completamente errado, amanhã vou tentar ajeitar, n peguei muito a lógica, mas deve ser um bglh besta

        self.screen_dashboard.window.mainloop()

app = App()
