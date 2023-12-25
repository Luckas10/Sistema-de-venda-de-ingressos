from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Screen_comprando:
    def __init__(self):
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
            x=35.0,
            y=417.0,
            width=199.0,
            height=44.0
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
            x=35.0,
            y=342.0,
            width=199.0,
            height=44.0
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
            x=35.0,
            y=267.0,
            width=199.0,
            height=44.0
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
            x=35.0,
            y=192.0,
            width=199.0,
            height=44.0
        )

        self.caminho_imagem = ""
        self.button_image_5 = PhotoImage(
            file=self.caminho_imagem)
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=358.0,
            y=203.0,
            width=150.0,
            height=244.0
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
            x=579.0,
            y=393.0,
            width=332.0,
            height=54.0
        )

        self.canvas.create_text(
            579.0,
            203.0,
            anchor="nw",
            text="Sala:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.canvas.create_text(
            802.0,
            204.0,
            anchor="nw",
            text="Horário:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.canvas.create_text(
            588.0,
            233.0,
            anchor="nw",
            text="nº",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            833.0,
            233.0,
            anchor="nw",
            text="nº",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            687.0,
            301.0,
            anchor="nw",
            text="Cadeira:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.canvas.create_text(
            630.0,
            331.0,
            anchor="nw",
            text="Ordem de chegada",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )
        self.window.resizable(False, False)

