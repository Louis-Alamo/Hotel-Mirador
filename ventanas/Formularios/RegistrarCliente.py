from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkComboBox import LtkComboBoxLine
class RegistrarCliente:

    def __init__(self):

        self.ventana = CTk()
        self.ventana.title("Registrar Cliente")

        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_formulario()

        self.ventana.mainloop()

    def crear_formulario(self):

        CTkLabel(self.ventana, text="Cliente", text_color="#000000", font=("Poppins", 24, "bold"), fg_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.frame_datos_personales = CTkFrame(self.ventana)
        self.frame_datos_personales.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.etiqueta_titulo = CTkLabel(self.frame_datos_personales, text="\t    Datos Personales", font=("Poppins", 14, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqeuta_nombre_completo = CTkLabel(self.frame_datos_personales, text="Nombre Completo: ",  font=("Poppins", 12, "bold"))
        self.etiqeuta_nombre_completo.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_nombre_completo = LtkEntryLine(self.frame_datos_personales, texto="Nombre Completo")
        self.campo_nombre_completo.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_apellido_paterno = CTkLabel(self.frame_datos_personales, text="Apellido Paterno: ", font=("Poppins", 12, "bold"))
        self.etiqueta_apellido_paterno.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.campo_apellido_paterno = LtkEntryLine(self.frame_datos_personales, texto="Apellido Paterno")
        self.campo_apellido_paterno.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_apellido_materno = CTkLabel(self.frame_datos_personales, text="Apellido Materno: ", font=("Poppins", 12, "bold"))
        self.etiqueta_apellido_materno.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.campo_apellido_materno = LtkEntryLine(self.frame_datos_personales, texto="Apellido Materno")
        self.campo_apellido_materno.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


        #Crear el formulario de negocio

        self.frame_datos_negocio = CTkFrame(self.ventana)
        self.frame_datos_negocio.grid(row=1, column=1, padx=10, pady=10)

        self.etiqueta_datos_negocio = CTkLabel(self.frame_datos_negocio, text="\t       Datos de Cliente", font=("Poppins", 14, "bold"))
        self.etiqueta_datos_negocio.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqueta_clave_cleinte = CTkLabel(self.frame_datos_negocio, text="Clave Cliente: ", font=("Poppins", 12, "bold"))
        self.etiqueta_clave_cleinte.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_clave_cliente = LtkEntryLine(self.frame_datos_negocio, texto="Clave Cliente")
        self.campo_clave_cliente.disable()
        self.campo_clave_cliente.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_telefono1 = CTkLabel(self.frame_datos_negocio, text="Número teléfono: ", font=("Poppins", 12, "bold"))
        self.etiqueta_telefono1.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.campo_telefono1 = LtkEntryLine(self.frame_datos_negocio, texto="Número teléfono")
        self.campo_telefono1.disable()
        self.campo_telefono1.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_telefono2 = CTkLabel(self.frame_datos_negocio, text="Número teléfono (auxiliar): ",font=("Poppins", 12, "bold"))
        self.etiqueta_telefono2.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.campo_telefono2 = LtkEntryLine(self.frame_datos_negocio, texto="Número teléfono (auxiliar)")
        self.campo_telefono2.disable()
        self.campo_telefono2.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_correo1 = CTkLabel(self.frame_datos_negocio, text="Correo electrónico: ",font=("Poppins", 12, "bold"))
        self.etiqueta_correo1.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.campo_correo1 = LtkEntryLine(self.frame_datos_negocio, texto="Correo electrónico")
        self.campo_correo1.disable()
        self.campo_correo1.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_correo2 = CTkLabel(self.frame_datos_negocio, text="Correo electrónico (auxiliar): ",font=("Poppins", 12, "bold"))
        self.etiqueta_correo2.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.campo_correo2 = LtkEntryLine(self.frame_datos_negocio, texto="Correo electrónico (auxiliar)")
        self.campo_correo2.disable()
        self.campo_correo2.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky="ew")



        self.frame_botones = CTkFrame(self.ventana, fg_color="#FFFFFF")
        self.frame_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="e")


        self.boton_cancelar = LtkButtonFill(self.frame_botones, nombre="Cancelar", funcion=lambda: self.aceptar())
        self.boton_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.boton_aceptar = LtkButtonFill(self.frame_botones, nombre="Aceptar", funcion=lambda: self.aceptar())
        self.boton_aceptar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


    def aceptar(self):
        pass



