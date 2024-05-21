from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkComboBox import LtkComboBoxLine

class FormularioEmpleado:

    def __init__(self, callback):

        self.callback = callback
        self.ventana = CTk()
        self.ventana.title("Registrar Empleado")

        self.ventana.resizable(False, False)
        self.ventana.grab_set()
        self.ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_formulario()

        self.ventana.mainloop()

    def crear_formulario(self):

        CTkLabel(self.ventana, text="Empleado", text_color="#000000", font=("Poppins", 24, "bold"), fg_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.frame_datos_personales = CTkFrame(self.ventana)
        self.frame_datos_personales.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.etiqueta_titulo = CTkLabel(self.frame_datos_personales, text="Datos Personales", font=("Poppins", 14, "bold"))
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

        self.etiqueta_datos_negocio = CTkLabel(self.frame_datos_negocio, text="Datos de Negocio", font=("Poppins", 14, "bold"))
        self.etiqueta_datos_negocio.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqueta_clave_empleado = CTkLabel(self.frame_datos_negocio, text="Clave Empleado: ", font=("Poppins", 12, "bold"))
        self.etiqueta_clave_empleado.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_clave_empleado = LtkEntryLine(self.frame_datos_negocio, texto="Clave Empleado")
        self.campo_clave_empleado.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_cargo_empleado = CTkLabel(self.frame_datos_negocio, text="Clave Empleado: ", font=("Poppins", 12, "bold"))
        self.etiqueta_cargo_empleado.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.cargo_empleado = LtkComboBoxLine(self.frame_datos_negocio, ["Administrador","Recepcionista", "Empleado"])
        self.cargo_empleado.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="ew")


        self.etiqueta_horario = CTkLabel(self.frame_datos_negocio, text="Horario: ", font=("Poppins", 12, "bold"))
        self.etiqueta_horario.grid(row=3, column=0, padx=10, pady=10, sticky="w")


        self.horario_entrada = LtkComboBoxLine(self.frame_datos_negocio, ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"])
        self.horario_entrada.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.horario_salida = LtkComboBoxLine(self.frame_datos_negocio, ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"])
        self.horario_salida.grid(row=4, column=1, padx=10, pady=10, sticky="ew")



        self.frame_botones = CTkFrame(self.ventana, fg_color="#FFFFFF")
        self.frame_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="e")


        self.boton_cancelar = LtkButtonFill(self.frame_botones, nombre="Cancelar", funcion=lambda: self.aceptar())
        self.boton_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.boton_aceptar = LtkButtonFill(self.frame_botones, nombre="Aceptar", funcion=lambda: self.aceptar())
        self.boton_aceptar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


    def aceptar(self):
        pass
    
    def on_close(self):
        self.ventana.destroy()
        self.callback()




