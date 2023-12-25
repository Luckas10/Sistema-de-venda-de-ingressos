from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Screen_concluida:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("1000x650")
        self.window.configure(bg = "#F9AAD0")


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

        self.caminho_imagem = ""
        self.button_image_1 = PhotoImage(
            file=self.caminho_imagem)
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=560.0,
            y=167.0,
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
            x=469.0,
            y=536.0,
            width=332.0,
            height=54.0
        )

        self.canvas.create_text(
            508.0,
            423.0,
            anchor="nw",
            text="Seu ticket é:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            508.0,
            458.0,
            anchor="nw",
            text="Obrigado pela compra",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            656.0,
            423.0,
            anchor="nw",
            text="#123456",
            fill="#000000",
            font=("Inter", 24 * -1)
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
            y=417.0,
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
            y=342.0,
            width=199.0,
            height=44.0
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
            y=267.0,
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
            y=192.0,
            width=199.0,
            height=44.0
        )

        self.canvas.create_text(
            401.0,
            69.0,
            anchor="nw",
            text="COMPRA CONCLUÍDA",
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", 44 * -1)
        )
        self.window.resizable(False, False)

