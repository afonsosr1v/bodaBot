
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1063x652")
window.configure(bg = "#0C0C0C")


canvas = Canvas(
    window,
    bg = "#0C0C0C",
    height = 652,
    width = 1063,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    531.0,
    46.0,
    image=image_image_1
)

canvas.create_text(
    9.0,
    11.0,
    anchor="nw",
    text="BodaBot",
    fill="#FFFFFF",
    font=("Metrophobic Regular", 80 * -1)
)

canvas.create_text(
    371.0,
    11.0,
    anchor="nw",
    text="v2.0.0",
    fill="#FFFFFF",
    font=("Metrophobic Regular", 80 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    277.0,
    369.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#000000",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=32.0,
    y=115.0,
    width=490.0,
    height=507.0
)

canvas.create_text(
    568.0,
    115.0,
    anchor="nw",
    text="Settings",
    fill="#FFFFFF",
    font=("Metrophobic Regular", 50 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    797.0,
    250.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=578.0,
    y=231.0,
    width=438.0,
    height=37.0
)

canvas.create_rectangle(
    568.0,
    199.0,
    693.0,
    238.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    594.0,
    206.0,
    anchor="nw",
    text="Bot Key",
    fill="#0C0C0C",
    font=("Metrophobic Regular", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    797.0,
    318.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=578.0,
    y=299.0,
    width=438.0,
    height=37.0
)

canvas.create_rectangle(
    568.0,
    267.0,
    693.0,
    306.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    579.0,
    274.0,
    anchor="nw",
    text="Search Key",
    fill="#0C0C0C",
    font=("Metrophobic Regular", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    797.0,
    386.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=578.0,
    y=367.0,
    width=438.0,
    height=37.0
)

canvas.create_rectangle(
    568.0,
    335.0,
    693.0,
    374.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    594.0,
    342.0,
    anchor="nw",
    text="CX Key",
    fill="#0C0C0C",
    font=("Metrophobic Regular", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    797.0,
    454.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=578.0,
    y=435.0,
    width=438.0,
    height=37.0
)

canvas.create_rectangle(
    568.0,
    403.0,
    693.0,
    442.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    587.0,
    410.0,
    anchor="nw",
    text="Server ID",
    fill="#0C0C0C",
    font=("Metrophobic Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=866.0,
    y=503.0,
    width=159.0,
    height=46.0
)

canvas.create_text(
    913.0,
    510.0,
    anchor="nw",
    text="Apply",
    fill="#FFFFFF",
    font=("Metrophobic Regular", 25 * -1)
)
window.resizable(False, False)
window.mainloop()
