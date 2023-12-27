from Telas .Login .login import *
from Telas .Dashboard .dashboard import *
from Telas .Comprando .comprando import *
from Telas .Compra_concluída .concluida import *
from Telas .Consultar_compra .consultar import *
from Funcoes .funcoes_db import *
from Funcoes .funcoes import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images_Filmes")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class App:
    def __init__(self):
        self.admin_list = listar_usuarios("Admin_users", "Admin")
        self.usuarios = dict()
        self.ids = [0]

        self.search_users()
        print(self.usuarios)

        self.janela = Screen_Login()

        self.nome = ""

        self.janela.button_1.configure(command=lambda: self.informar_tela(
            tela="Dashboard_login", nomePerfil=self.janela.entry_1.get()))

        self.janela.window.mainloop()


    def informar_tela(self, tela, nomePerfil="", filme="", dados_filme={}):
        if tela == "Dashboard":
            self.dashboard(nomePerfil=self.nome)

        if tela == "Dashboard_login":
            self.nome = nomePerfil

            if self.verificar_user(nomePerfil):
                self.definir_id(nomePerfil)
            else:
                self.append_user(self.nome)
            self.dashboard(nomePerfil=nomePerfil)

        elif tela == "Comprando":
            self.comprando(filme)

        elif tela == "Login":
            self.login()

        elif tela == "Compra concluída":
            self.concluida(filme, dados_filme)

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
            tela="Comprando", filme="Wonka")
        self.janela.button_2["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="Napoleão")
        self.janela.button_3["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="Jogos vorazes")
        self.janela.button_4["command"] = lambda: self.informar_tela(
            tela="Comprando", filme="As marvels")
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

        self.janela.button_3["command"] = lambda: self.exibir_consulta(self.janela.entry_1.get())


    def comprando(self, filme=""):
        self.janela.window.destroy()

        self.janela = Screen_comprando()

        self.janela.button_1["command"] = lambda: self.informar_tela(
            tela="Login")
        self.janela.button_3["command"] = lambda: self.informar_tela(
            tela="Consultar")
        self.janela.button_4["command"] = lambda: self.informar_tela(
            tela="Dashboard")

        if filme == "As marvels":
            self.janela.caminho_imagem = relative_to_assets("button_4.png")
        elif filme == "Jogos vorazes":
            self.janela.caminho_imagem = relative_to_assets("button_3.png")
        elif filme == "Napoleão":
            self.janela.caminho_imagem = relative_to_assets("button_2.png")
        elif filme == "Wonka":
            self.janela.caminho_imagem = relative_to_assets("button_1.png")

        nova_imagem = PhotoImage(file=self.janela.caminho_imagem)

        self.janela.button_5.configure(image=nova_imagem)
        self.janela.button_5.image = nova_imagem
        
        dados_filme = search_info_gerais(filme)


        self.janela.canvas.create_text(
            600.0,
            233.0,
            anchor="nw",
            text=dados_filme["sala"],
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.janela.canvas.create_text(
            812.0,
            233.0,
            anchor="nw",
            text=dados_filme["horario"],
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )


        self.janela.button_6["command"] = lambda: self.informar_tela(
            tela="Compra concluída", filme=filme, dados_filme=dados_filme)


    def concluida(self, filme="", dados_filme={}):
        self.janela.window.destroy()

        self.janela = Screen_concluida()
        
        self.janela.button_3["command"] = lambda: self.informar_tela(
            tela="Login")
        self.janela.button_5["command"] = lambda: self.informar_tela(
            tela="Consultar")
        self.janela.button_6["command"] = lambda: self.informar_tela(
            tela="Dashboard")

        if filme == "As marvels":
            self.janela.caminho_imagem = relative_to_assets("button_4.png")
        elif filme == "Jogos vorazes":
            self.janela.caminho_imagem = relative_to_assets("button_3.png")
        elif filme == "Napoleão":
            self.janela.caminho_imagem = relative_to_assets("button_2.png")
        elif filme == "Wonka":
            self.janela.caminho_imagem = relative_to_assets("button_1.png")

        nova_imagem = PhotoImage(file=self.janela.caminho_imagem)

        # Configura a nova imagem para o botão
        self.janela.button_1.configure(image=nova_imagem)
        self.janela.button_1.image = nova_imagem

        ticket = gerar_ticket()
        adicionar_compra(self.id, filme, ticket, dados_filme["sala"], dados_filme["horario"])
        
        self.janela.canvas.create_text(
            656.0,
            423.0,
            anchor="nw",
            text=f"{ticket}",
            fill="#000000",
            font=("Inter", 24 * -1)
        )


        self.janela.button_2["command"] = lambda: self.informar_tela(
            tela="Dashboard")


    def exibir_consulta(self, ticket_informado):
        self.consultar()

        self.janela.button_2["command"] = lambda: self.exibir_deletar_compra(ticket_informado)

        consulta = search_tickets(self.id, ticket_informado)

        if consulta == False:
            self.janela.canvas.create_text(
                400.0,
                365.0,
                anchor="nw",
                text="NENHUM TICKET FOI ENCONTRADO!",
                fill="#FFFFFF",
                font=("Inter", 26 * -1)
            )
        else:

            if consulta["filme"] == "As marvels":
                self.janela.caminho_imagem = relative_to_assets("button_4.png")
            elif consulta["filme"] == "Jogos vorazes":
                self.janela.caminho_imagem = relative_to_assets("button_3.png")
            elif consulta["filme"] == "Napoleão":
                self.janela.caminho_imagem = relative_to_assets("button_2.png")
            elif consulta["filme"] == "Wonka":
                self.janela.caminho_imagem = relative_to_assets("button_1.png")

            nova_imagem = PhotoImage(file=self.janela.caminho_imagem)

            self.janela.button_1.configure(image=nova_imagem)
            self.janela.button_1.image = nova_imagem

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
                text=consulta["sala"],
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
                text=consulta["horario"],
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


    def search_users(self):
        for valor in self.admin_list:
            self.ids.append(int(valor[0]))
            self.usuarios[valor[1]] = valor[2]


    def verificar_user(self, username):
        verificador = False

        for user in self.usuarios.values():
            if user == username:
                verificador = True

        return verificador

        
    def append_user(self, username):
        self.ids.append(self.ids[-1] + 1)
        self.id = f"user{self.ids[-1]}"
        self.usuarios[self.id] = username

        self.values_users = (str(self.ids[-1]), str(f"user{self.ids[-1]}"), str(username))

        adicionar_user("Admin_users", "Admin", self.values_users)
        criar_tabela_user(f"user{self.ids[-1]}", "Usuarios")
        

    def definir_id(self, username):
        for id, user in self.usuarios.items():
            if user == username:
                self.id = id


    def exibir_deletar_compra(self, ticket):
        deletar_compra(ticket, self.id)

        self.consultar()

        self.janela.canvas.create_text(
                400.0,
                365.0,
                anchor="nw",
                text="COMPRA DELETADA COM SUCESSO!",
                fill="#FFFFFF",
                font=("Inter", 26 * -1)
            )


if __name__ == "__main__":
    app = App()