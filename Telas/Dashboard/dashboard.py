from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Screen_Dashboard:
    def __init__(self, nome_perfil):
        self.window = Tk()

        self.window.geometry("1000x650")
        self.window.configure(bg = "#F9AAD0")
        self.window.title("Ticket System - TODOS OS INGRESSOS VENDIDOS, SÃO PARA O DIA DA COMPRA!")


        self.canvas = Canvas(
            self.window,
            bg = "#F9AAD0",
            height = 650,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            270.0,
            651.0,
            fill="#AD53A6",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=815.0,
            y=203.0,
            width=150.0,
            height=244.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=645.0,
            y=203.0,
            width=150.0,
            height=244.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=475.0,
            y=203.0,
            width=150.0,
            height=244.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=305.0,
            y=203.0,
            width=150.0,
            height=244.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=35.0,
            y=417.0,
            width=199.0,
            height=44.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=35.0,
            y=342.0,
            width=199.0,
            height=44.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=35.0,
            y=267.0,
            width=199.0,
            height=44.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=35.0,
            y=192.0,
            width=199.0,
            height=44.0
        )

        self.canvas.create_text(
            106.0,
            42.0,
            anchor="nw",
            text="Bem-vindo",
            fill="#FFFFFF",
            font=("Inter", 22 * -1)
        )

        self.nomePerfil = nome_perfil
        self.canvas.create_text(
            106.0,
            71.0,
            anchor="nw",
            text=self.nomePerfil,
            fill="#FFFFFF",
            font=("Inter", 22 * -1)
        )

        self.canvas.create_text(
            437.0,
            503.0,
            anchor="nw",
            text="Sugestões de filmes para o cartaz:",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            425.0,
            69.0,
            anchor="nw",
            text="FILMES EM CARTAZ",
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", 44 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            635.0,
            564.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=432.0,
            y=542.0,
            width=406.0,
            height=42.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            75.0,
            70.0,
            image=self.image_image_1
        )
        self.window.resizable(False, False)
        
