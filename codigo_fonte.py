from Telas .Login .login import *
from Telas .Dashboard .dashboard import *
from Telas .Comprando .comprando import *
from Telas .Compra_concluída .concluida import *
from Telas .Consultar_compra .consultar import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images_Filmes")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class App:
    def __init__(self):
        self.janela = Screen_Login()

        self.nome = ""

        self.janela.button_1.configure(command=lambda: self.informar_tela(
            tela="Dashboard_login", nomePerfil=self.janela.entry_1.get()))

        self.janela.window.mainloop()

    def informar_tela(self, tela, nomePerfil="", filme=""):
        if tela == "Dashboard":
            self.dashboard(nomePerfil=self.nome)

        if tela == "Dashboard_login":
            self.nome = nomePerfil
            self.dashboard(nomePerfil=nomePerfil)

        elif tela == "Comprando":
            self.comprando(filme)

        elif tela == "Login":
            self.login()

        elif tela == "Compra concluída":
            self.concluida(filme)

    def dashboard(self, nomePerfil):
        self.janela.window.destroy()

        self.janela = Screen_Dashboard(nome_perfil=nomePerfil)

        self.janela.button_1["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="Filme 4")
        self.janela.button_2["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="Filme 3")
        self.janela.button_3["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="Filme 2")
        self.janela.button_4["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="Filme 1")
        self.janela.button_5["command"] = lambda: self.informar_tela(
            tela="Login")

    def comprando(self, filme=""):
        self.janela.window.destroy()

        self.janela = Screen_comprando()

        if filme == "Filme 1":
            self.janela.caminho_imagem = relative_to_assets("button_4.png")
        elif filme == "Filme 2":
            self.janela.caminho_imagem = relative_to_assets("button_3.png")
        elif filme == "Filme 3":
            self.janela.caminho_imagem = relative_to_assets("button_2.png")
        elif filme == "Filme 4":
            self.janela.caminho_imagem = relative_to_assets("button_1.png")

        nova_imagem = PhotoImage(file=self.janela.caminho_imagem)

        # Configura a nova imagem para o botão
        self.janela.button_5.configure(image=nova_imagem)
        self.janela.button_5.image = nova_imagem
        
        self.janela.button_6["command"] = lambda: self.informar_tela(
            tela="Compra concluída", filme=filme)


    def login(self):
        self.janela.window.destroy()

        self.janela = Screen_Login()

        self.janela.button_1.configure(command=lambda: self.informar_tela(
            tela="Dashboard_login", nomePerfil=self.janela.entry_1.get()))


    def concluida(self, filme=""):
        self.janela.window.destroy()

        self.janela = Screen_concluida()
        
        if filme == "Filme 1":
            self.janela.caminho_imagem = relative_to_assets("button_4.png")
        elif filme == "Filme 2":
            self.janela.caminho_imagem = relative_to_assets("button_3.png")
        elif filme == "Filme 3":
            self.janela.caminho_imagem = relative_to_assets("button_2.png")
        elif filme == "Filme 4":
            self.janela.caminho_imagem = relative_to_assets("button_1.png")

        nova_imagem = PhotoImage(file=self.janela.caminho_imagem)

        # Configura a nova imagem para o botão
        self.janela.button_1.configure(image=nova_imagem)
        self.janela.button_1.image = nova_imagem

        self.janela.button_2["command"] = lambda: self.informar_tela(
            tela="Dashboard")


app = App()
