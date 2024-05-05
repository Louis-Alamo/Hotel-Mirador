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





