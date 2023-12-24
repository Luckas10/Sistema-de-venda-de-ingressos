from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./Images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Screen_consultar:
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
            x=358.0,
            y=267.0,
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
            x=579.0,
            y=457.0,
            width=332.0,
            height=54.0
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
            x=785.93994140625,
            y=104.0,
            width=125.06007385253906,
            height=44.0
        )

        self.canvas.create_text(
            579.0,
            267.0,
            anchor="nw",
            text="Sala:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.canvas.create_text(
            802.0,
            268.0,
            anchor="nw",
            text="Horário:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.canvas.create_text(
            588.0,
            297.0,
            anchor="nw",
            text="nº",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            833.0,
            297.0,
            anchor="nw",
            text="nº",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            687.0,
            365.0,
            anchor="nw",
            text="Cadeira:",
            fill="#FFFFFF",
            font=("Inter", 26 * -1)
        )

        self.canvas.create_text(
            630.0,
            395.0,
            anchor="nw",
            text="Ordem de chegada",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            566.0,
            126.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=368.0,
            y=104.0,
            width=396.0,
            height=42.0
        )

        self.canvas.create_text(
            412.0,
            65.0,
            anchor="nw",
            text="Informe o número do ticket",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
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
            y=417.0,
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
            y=342.0,
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
            y=267.0,
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
            y=192.0,
            width=199.0,
            height=44.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()


app = Screen_consultar()