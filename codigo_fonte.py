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

        elif tela == "Consultar":
            self.consultar()


    def login(self):
        self.janela.window.destroy()

        self.janela = Screen_Login()

        self.janela.button_1.configure(command=lambda: self.informar_tela(
            tela="Dashboard_login", nomePerfil=self.janela.entry_1.get()))


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
        self.janela.button_7["command"] = lambda: self.informar_tela(
            tela="Consultar")
        self.janela.button_8["command"] = lambda: self.informar_tela(
            tela="Dashboard")


    def consultar(self):
        self.janela.window.destroy()

        self.janela = Screen_consultar()

        self.janela.button_4["command"] = lambda: self.informar_tela(
            tela="Login")
        self.janela.button_6["command"] = lambda: self.informar_tela(
            tela="Consultar")
        self.janela.button_7["command"] = lambda: self.informar_tela(
            tela="Dashboard")
        self.janela.button_3["command"] = lambda: self.exibir_consulta(sala=4, horario="14h30")


    def comprando(self, filme=""):
        self.janela.window.destroy()

        self.janela = Screen_comprando()

        self.janela.button_1["command"] = lambda: self.informar_tela(
            tela="Login")
        self.janela.button_3["command"] = lambda: self.informar_tela(
            tela="Consultar")
        self.janela.button_4["command"] = lambda: self.informar_tela(
            tela="Dashboard")

        if filme == "Filme 1":
            self.janela.caminho_imagem = relative_to_assets("button_4.png")
        elif filme == "Filme 2":
            self.janela.caminho_imagem = relative_to_assets("button_3.png")
        elif filme == "Filme 3":
            self.janela.caminho_imagem = relative_to_assets("button_2.png")
        elif filme == "Filme 4":
            self.janela.caminho_imagem = relative_to_assets("button_1.png")

        nova_imagem = PhotoImage(file=self.janela.caminho_imagem)

        self.janela.button_5.configure(image=nova_imagem)
        self.janela.button_5.image = nova_imagem
        
        self.janela.button_6["command"] = lambda: self.informar_tela(
            tela="Compra concluída", filme=filme)


    def concluida(self, filme=""):
        self.janela.window.destroy()

        self.janela = Screen_concluida()
        
        self.janela.button_3["command"] = lambda: self.informar_tela(
            tela="Login")
        self.janela.button_5["command"] = lambda: self.informar_tela(
            tela="Consultar")
        self.janela.button_6["command"] = lambda: self.informar_tela(
            tela="Dashboard")

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


    def exibir_consulta(self, sala=0, horario=""):
        self.janela.canvas.create_text(
            579.0,
            267.0,
            anchor="nw",
            text="Sala:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.janela.canvas.create_text(
            600.0,
            297.0,
            anchor="nw",
            text=sala,
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.janela.canvas.create_text(
            802.0,
            268.0,
            anchor="nw",
            text="Horário:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.janela.canvas.create_text(
            812.0,
            297.0,
            anchor="nw",
            text=horario,
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.janela.canvas.create_text(
            687.0,
            365.0,
            anchor="nw",
            text="Cadeira:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.janela.canvas.create_text(
            630.0,
            395.0,
            anchor="nw",
            text="Ordem de chegada",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.janela.button_1.place(
            x=358.0,
            y=267.0,
            width=150.0,
            height=244.0
        )

        self.janela.button_2.place(
            x=579.0,
            y=457.0,
            width=332.0,
            height=54.0
        )


app = App()
