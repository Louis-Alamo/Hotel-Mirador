from customtkinter import CTkButton


class LtkButtonLine(CTkButton):
    """
    Clase LtkButtonLine que hereda de CTkButton. Esta clase representa un botón personalizado con estilos y comportamientos específicos.

    Atributos
    ----------
    master : tkinter object
        El widget padre.
    nombre : str
        El texto que se mostrará en el botón. Por defecto es "LtkButtonLine".
    command : function
        La función que se ejecutará cuando se haga clic en el botón.
    **kwargs : dict
        Argumentos adicionales para el constructor de CTkButton.

    Métodos
    -------
    disable():
        Deshabilita el botón y cambia su apariencia a un estado deshabilitado.
    enable():
        Habilita el botón y cambia su apariencia a un estado normal.
    """

    def __init__(self, master, nombre="LtkButtonLine", command=None, **kwargs):
        """
        Constructor de la clase LtkButtonLine.

        Parámetros
        ----------
        master : tkinter object
            El widget padre.
        nombre : str, opcional
            El texto que se mostrará en el botón. Por defecto es "LtkButtonLine".
        command : function, opcional
            La función que se ejecutará cuando se haga clic en el botón.
        **kwargs : dict, opcional
            Argumentos adicionales para el constructor de CTkButton.
        """
        super().__init__(master, **kwargs)

        self.configure(
            fg_color="transparent",
            border_color="#40909A",
            text=nombre,
            text_color="#40909A",
            font=("Poppins", 14, "bold"),
            hover=True,
            hover_color="#33616B",
            corner_radius=5,
            border_spacing=8,
            cursor="hand2",
            command=command
        )

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        """
        Cambia el color del borde y del texto cuando el mouse pasa por encima del botón.
        """
        self.configure(
            border_color="#33616B",
            text_color="#33616B"
        )

    def on_leave(self, event):
        """
        Revierte el color del borde y del texto cuando el mouse deja de pasar por encima del botón.
        """
        self.configure(
            border_color="#40909A",
            text_color="#40909A"
        )

    def disable(self):
        """
        Deshabilita el botón y cambia su apariencia a un estado deshabilitado.
        """
        self.configure(
            state="disabled",
            border_color="#BDE1E4",
            text_color="#BDE1E4",
            cursor="arrow"
        )

    def enable(self):
        """
        Habilita el botón y cambia su apariencia a un estado normal.
        """
        self.configure(
            state="normal",
            fg_color="transparent",
            border_color="#40909A",
            text_color="#40909A",
            cursor="hand2"
        )
