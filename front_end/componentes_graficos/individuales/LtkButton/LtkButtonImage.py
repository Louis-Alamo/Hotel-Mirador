from customtkinter import CTkButton

class LtkButtonImage(CTkButton):

    def __init__(self, master, image, funcion, **kwargs):

        super().__init__(master, **kwargs)

        self.configure(
            fg_color="transparent",
            text_color="#000000",
            border_color="#5BACB5",
            font=("Poppins", 12),
            text="",
            corner_radius=5,
            cursor="hand2",
            image=image,
            anchor="center",
            command=funcion
        )

import tkinter as tk
from util.ProcesarImagenes import rescale_image_ctk
ventana = tk.Tk()
from PIL import Image, ImageTk
imagene = rescale_image_ctk(image_path='../../../../imagenes/iconos/filtrar.png', new_width=30, new_height=30)
boton = LtkButtonImage(ventana, image=imagene, funcion=lambda: print("hola"))
boton.pack()
ventana.mainloop()




