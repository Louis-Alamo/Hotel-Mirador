from customtkinter import CTkButton

class LtkImageTextButton(CTkButton):


    def __init__(self, master,imagen, funcion, texto="LtkImageTextButton", **kwargs):
        super().__init__(master, **kwargs)

        self.configure(
            fg_color="transparent",
            text=texto,
            text_color="#192D33",
            font=("Poppins", 14, "bold"),
            hover=False,
            border_spacing=8,
            cursor="hand2",
            image=imagen,
            anchor="center",
            command=funcion
        )
