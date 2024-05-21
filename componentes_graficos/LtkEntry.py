from customtkinter import CTkEntry
import tkinter as tk

class LtkEntryFill(CTkEntry):
    """
    Clase LtkEntryFill que hereda de CTkEntry. Esta clase representa un campo de entrada personalizado con estilos y comportamientos específicos.

    Atributos
    ----------
    master : tkinter object
        El widget padre.
    texto : str
        El texto que se mostrará en el campo de entrada cuando esté vacío.
    **kwargs : dict
        Argumentos adicionales para el constructor de CTkEntry.

    Métodos
    -------
    disable():
        Deshabilita el campo de entrada y cambia su apariencia a un estado deshabilitado.
    enable():
        Habilita el campo de entrada y cambia su apariencia a un estado normal.
    get_text():
        Retorna el texto actual en el campo de entrada.
    delete_text():
        Borra todo el texto en el campo de entrada.
    """

    def __init__(self, master, texto="",  **kwargs):
        """
        Constructor de la clase LtkEntryFill.

        Parámetros
        ----------
        master : tkinter object
            El widget padre.
        texto : str, opcional
            El texto que se mostrará en el campo de entrada cuando esté vacío.
        **kwargs : dict, opcional
            Argumentos adicionales para el constructor de CTkEntry.
        """
        super().__init__(master, **kwargs)
        self.configure(
            fg_color="#DCF0F1",
            border_color="#5BACB5",
            text_color="#000000",
            font=("Poppins", 14, "bold"),
            corner_radius=5,
            placeholder_text=texto,
            cursor="xterm",
        )

    def disable(self):
        """
        Deshabilita el campo de entrada y cambia su apariencia a un estado deshabilitado.
        """
        self.configure(
            state="disabled",
            fg_color="#DCF0F1",
            border_color="#DCF0F1",
            cursor="arrow"
        )

    def enable(self):
        """
        Habilita el campo de entrada y cambia su apariencia a un estado normal.
        """
        self.configure(
            state="normal",
            fg_color="#DCF0F1",
            text_color="#000000",
            border_color="#5BACB5",
            cursor="xterm"
        )

    def get_text(self):
        """
        Retorna el texto actual en el campo de entrada.
        """
        return self.get()

    def delete_text(self):
        """
        Borra todo el texto en el campo de entrada.
        """
        self.delete(0,tk.END)



class LtkEntryLine(CTkEntry):
    """
    Clase LtkEntryLine que hereda de CTkEntry. Esta clase representa un campo de entrada personalizado con estilos y comportamientos específicos.

    Atributos
    ----------
    master : tkinter object
        El widget padre.
    texto : str
        El texto que se mostrará en el campo de entrada cuando esté vacío.
    **kwargs : dict
        Argumentos adicionales para el constructor de CTkEntry.

    Métodos
    -------
    disable():
        Deshabilita el campo de entrada y cambia su apariencia a un estado deshabilitado.
    enable():
        Habilita el campo de entrada y cambia su apariencia a un estado normal.
    get_text():
        Retorna el texto actual en el campo de entrada.
    delete_text():
        Borra todo el texto en el campo de entrada.
    """

    def __init__(self, master, texto="",  **kwargs):
        """
        Constructor de la clase LtkEntryFill.

        Parámetros
        ----------
        master : tkinter object
            El widget padre.
        texto : str, opcional
            El texto que se mostrará en el campo de entrada cuando esté vacío.
        **kwargs : dict, opcional
            Argumentos adicionales para el constructor de CTkEntry.
        """
        super().__init__(master, **kwargs)
        self.configure(
            fg_color="#FFFFFF",
            border_color="#5BACB5",
            text_color="#000000",
            font=("Poppins", 12),
            corner_radius=5,
            placeholder_text=texto,
            cursor="xterm",
        )

    def disable(self):
        """
        Deshabilita el campo de entrada y cambia su apariencia a un estado deshabilitado.
        """
        self.configure(
            state="disabled",
            fg_color="#FFFFFF",
            text_color="#BDE1E4",
            border_color="#DCF0F1",
            cursor="arrow",
            font = ("Poppins", 12, "bold"),
        )

    def enable(self):
        """
        Habilita el campo de entrada y cambia su apariencia a un estado normal.
        """
        self.configure(
            state="normal",
            fg_color="#FFFFFF",
            text_color="#000000",
            border_color="#5BACB5",
            cursor="xterm"
        )

    def get_text(self):
        """
        Retorna el texto actual en el campo de entrada.
        """
        return self.get()

    def delete_text(self):
        """
        Borra todo el texto en el campo de entrada.
        """
        self.delete(0,tk.END)
        
    def set_text(self, text):
        """
        Establece el texto del campo de entrada.

        Parámetros
        ----------
        text : str
            El texto que se establecerá en el campo de entrada.
        """
        self.delete(0, tk.END)
        self.insert(0, text)
        
