from customtkinter import CTkButton

class LtkButtonFill(CTkButton):
    """
    Clase LtkButtonFill que hereda de CTkButton. Esta clase representa un botón personalizado con estilos y comportamientos específicos.

    Atributos
    ----------
    master : tkinter object
        El widget padre.
    nombre : str
        El texto que se mostrará en el botón. Por defecto es "LtkButtonFill".
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

    def __init__(self, master, nombre="LtkButtonFill", command=None, **kwargs):
        """
        Constructor de la clase LtkButtonFill.

        Parámetros
        ----------
        master : tkinter object
            El widget padre.
        nombre : str, opcional
            El texto que se mostrará en el botón. Por defecto es "LtkButtonFill".
        command : function, opcional
            La función que se ejecutará cuando se haga clic en el botón.
        **kwargs : dict, opcional
            Argumentos adicionales para el constructor de CTkButton.
        """
        super().__init__(master, **kwargs)

        self.configure(
            fg_color="#40909A",
            border_color="#40909A",
            text=nombre,
            text_color="#F5F5F5",
            font=("Poppins", 14, "bold"),
            hover=True,
            hover_color="#33616B",
            corner_radius=5,
            border_spacing=8,
            cursor="hand2",
            command=command
        )

    def disable(self):
        """
        Deshabilita el botón y cambia su apariencia a un estado deshabilitado.
        """
        self.configure(
            state="disabled",
            fg_color="#DCF0F1",
            hover=False,
            text_color_disabled="#5BACB5",
            cursor="arrow"
        )

    def enable(self):
        """
        Habilita el botón y cambia su apariencia a un estado normal.
        """
        self.configure(
            state="normal",
            fg_color="#40909A",
            hover=True,
            text_color="#F5F5F5",
            cursor="hand2"
        )