from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Screen_Register:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("1000x650")
        self.window.configure(bg="#F9AAD0")

        self.canvas = Canvas(
            self.window,
            bg="#F9AAD0",
            height=650,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            707.0,
            325.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            415.0,
            650.0,
            fill="#AD53A6",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            bg="#AD53A6",
            relief="flat"
        )
        self.button_1.place(
            x=99.0,
            y=564.0,
            width=216.0,
            height=44.0
        )

        self.canvas.create_text(
            141.0,
            537.0,
            anchor="nw",
            text="Já tem cadastro?",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            bg="#AD53A6",
            relief="flat"
        )
        self.button_2.place(
            x=99.0,
            y=479.0,
            width=216.0,
            height=44.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            207.0,
            406.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=71.0,
            y=384.0,
            width=272.0,
            height=42.0
        )

        self.canvas.create_text(
            61.0,
            350.0,
            anchor="nw",
            text="Senha:",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            207.0,
            309.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=71.0,
            y=287.0,
            width=272.0,
            height=42.0
        )

        self.canvas.create_text(
            61.0,
            253.0,
            anchor="nw",
            text="E-mail:",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            207.0,
            212.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=71.0,
            y=190.0,
            width=272.0,
            height=42.0
        )

        self.canvas.create_text(
            61.0,
            156.0,
            anchor="nw",
            text="Nome:",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            61.0,
            99.0,
            anchor="nw",
            text="Bem vindo!",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            123.0,
            49.0,
            anchor="nw",
            text="Ticket System.",
            fill="#FFFFFF",
            font=("Inter", 29 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            86.0,
            66.0,
            image=self.image_image_2
        )
        self.window.resizable(False, False)
