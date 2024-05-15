from customtkinter import *
from componentes_graficos.LtkComboBox import LtkComboBoxLine
class LtkCalendar(CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(fg_color="transparent")

        self.etiquete_dia = CTkLabel(self, text="Dia", font=("Poppins", 12, "bold"))
        self.etiquete_dia.grid(row=0, column=0)

        self.entry_dia = CTkEntry(self, font=("Poppins", 12, "bold"), fg_color="#FFFFFF",placeholder_text="DD", text_color="#000000", border_color="#5BACB5", corner_radius=5)
        self.entry_dia.configure(width=35)
        self.entry_dia.grid(row=1, column=0, padx=10, pady=5)

        self.etiqueta_mes = CTkLabel(self, text="Mes", font=("Poppins", 12, "bold"))
        self.etiqueta_mes.grid(row=0, column=1)

        self.entry_mes = CTkEntry(self, font=("Poppins", 12, "bold"), fg_color="#FFFFFF",placeholder_text="MM", text_color="#000000", border_color="#5BACB5", corner_radius=5)
        self.entry_mes.configure(width=35)
        self.entry_mes.grid(row=1, column=1, padx=10, pady=5)

        self.etiqueta_anio = CTkLabel(self, text="Año", font=("Poppins", 12, "bold"))
        self.etiqueta_anio.grid(row=0, column=2)

        self.entry_anio = CTkEntry(self, font=("Poppins", 12, "bold"), fg_color="#FFFFFF",placeholder_text="AAAA", text_color="#000000", border_color="#5BACB5", corner_radius=5)
        self.entry_anio.configure(width=40)
        self.entry_anio.grid(row=1, column=2, padx=10, pady=5)

    def get_date(self):
        """
        Retorna la fecha seleccionada en el calendario.
        """
        return f"{self.entry_dia.get()}/{self.entry_mes.get()}/{self.entry_anio.get()}"


