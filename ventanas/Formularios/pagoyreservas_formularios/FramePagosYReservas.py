from tkinter import *
from SQL.ConsultarDatosSQL import ConsultarDatosSQL
from SQL.RegistrarDatos import RegistrarDatos
from SQL.EliminarDatos import EliminarDatos
from SQL.ActualizarDatos import ActualizarDatos
from componentes_graficos.TreeviewTable import TreeviewTable
from customtkinter import *
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkFecha import LtkFecha
from util.TraducirValores import convertir_hora_a_cadena

from ventanas.Formularios.cliente_formularios.RegistrarCliente import RegistrarCliente
from ventanas.Formularios.cliente_formularios.EditarCliente import EditarCliente

class RegistrarPagosYReserva:

    def __init__(self):

        self.ventana = CTk()
        self.ventana.title("Registrar Pago y Reserva")

        self.ventana.resizable(False, False)
        self.ventana.grab_set()

        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_formulario()

        self.ventana.mainloop()

    def crear_formulario(self):

        CTkLabel(self.ventana, text="Pagos y Reservas", text_color="#000000", font=("Poppins", 24, "bold"), fg_color="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.frame_datos_personales = CTkFrame(self.ventana)
        self.frame_datos_personales.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.etiqueta_titulo = CTkLabel(self.frame_datos_personales, text="Pagos", font=("Poppins", 14, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqeuta_clave_pago = CTkLabel(self.frame_datos_personales, text="Clave de pago: ",  font=("Poppins", 12, "bold"))
        self.etiqeuta_clave_pago.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_clave = LtkEntryLine(self.frame_datos_personales, texto="Clave de pago")
        self.campo_clave.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_horario = CTkLabel(self.frame_datos_personales, text="Hora de pago: ", font=("Poppins", 12, "bold"))
        self.etiqueta_horario.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.horario_pago = LtkComboBoxLine(self.frame_datos_personales,
                                               ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00",
                                                "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                                                "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"])
        self.horario_pago.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.etiqueta_fecha = CTkLabel(self.frame_datos_personales, text="\nFECHA DE PAGO",
                                         font=("Poppins", 12, "bold"))
        self.etiqueta_fecha.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.etiqueta_dia= CTkLabel(self.frame_datos_personales, text="Día: ",
                                         font=("Poppins", 12, "bold"))
        self.etiqueta_dia.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.dia_pago = LtkComboBoxLine(self.frame_datos_personales,
                                            ["01", "02", "03", "04", "05", "06", "07", "08",
                                             "09", "10", "11", "12", "13", "14", "15", "16",
                                             "17", "18", "19", "20", "21", "22", "23", "24","25","26","27","28","29","30","31"])
        self.dia_pago.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        self.etiqueta_mes = CTkLabel(self.frame_datos_personales, text="Mes: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_mes.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.mes_pago = LtkComboBoxLine(self.frame_datos_personales,
                                        ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                                         "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.mes_pago.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        self.etiqueta_año = CTkLabel(self.frame_datos_personales, text="Año: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_año.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.dia_año = LtkComboBoxLine(self.frame_datos_personales,
                                        [ "2005", "2006", "2007", "2008",
                                         "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                                         "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029",
                                         "2030", "2031"])
        self.dia_año.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        self.etiqueta_metodopago= CTkLabel(self.frame_datos_personales, text="Método de pago: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_metodopago.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        self.metodo_pago = LtkComboBoxLine(self.frame_datos_personales,
                                       ["Efectivo", "Tarjeta de crédito", "Tarjeta de débito"])
        self.metodo_pago.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

        #Crear el formulario de negocio

        self.frame_datos_negocio = CTkFrame(self.ventana)
        self.frame_datos_negocio.grid(row=1, column=1, padx=10, pady=10)

        self.etiqueta_datos_negocio = CTkLabel(self.frame_datos_negocio, text="\t\t \t \t \t \t \t        Datos de reserva", font=("Poppins", 14, "bold"))
        self.etiqueta_datos_negocio.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.etiqueta_clave_reserva = CTkLabel(self.frame_datos_negocio, text="Clave Reserva: ", font=("Poppins", 12, "bold"))
        self.etiqueta_clave_reserva.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.campo_clave_reserva = LtkEntryLine(self.frame_datos_negocio, texto="Clave Reserva")
        self.campo_clave_reserva.disable()
        self.campo_clave_reserva.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

        self.etiqueta_clave_cliente = CTkLabel(self.frame_datos_negocio, text="Clave Cliente: ", font=("Poppins", 12, "bold"))
        self.etiqueta_clave_cliente.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.campo_clave_cliente = LtkEntryLine(self.frame_datos_negocio, texto="Clave Cliente")
        self.campo_clave_cliente.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.etiqueta_inicio_reserva = CTkLabel(self.frame_datos_negocio, text="\t\n\n\n\n\n\n\n\n\n\n FECHA DE INICIO DE RESERVA ",
                                         font=("Poppins", 12, "bold"))
        self.etiqueta_inicio_reserva.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.etiqueta_dia1 = CTkLabel(self.frame_datos_negocio, text="Día: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_dia1.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.dia1 = LtkComboBoxLine(self.frame_datos_negocio,
                                        ["01", "02", "03", "04", "05", "06", "07", "08",
                                         "09", "10", "11", "12", "13", "14", "15", "16",
                                         "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                         "30", "31"])
        self.dia1.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        self.etiqueta_mes1 = CTkLabel(self.frame_datos_negocio, text="Mes: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_mes1.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        self.mes1 = LtkComboBoxLine(self.frame_datos_negocio,
                                        ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                                         "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.mes1.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        self.etiqueta_año1 = CTkLabel(self.frame_datos_negocio, text="Año: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_año1.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        self.dia_año1 = LtkComboBoxLine(self.frame_datos_negocio,
                                       ["2005", "2006", "2007", "2008",
                                        "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                                        "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026",
                                        "2027", "2028", "2029",
                                        "2030", "2031"])
        self.dia_año1.grid(row=7, column=1, padx=10, pady=10, sticky="ew")



        self.etiqueta_fin_reserva = CTkLabel(self.frame_datos_negocio, text="\n\n\n\n\n\n\n\n\n\n FECHA DE FINALIZACIÓN DE RESERVA",
                                                 font=("Poppins", 12, "bold"))
        self.etiqueta_fin_reserva.grid(row=4, column=2, padx=10, pady=10, sticky="w")

        self.etiqueta_dia2 = CTkLabel(self.frame_datos_negocio, text="Día: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_dia2.grid(row=5, column=2, padx=10, pady=10, sticky="w")

        self.dia2 = LtkComboBoxLine(self.frame_datos_negocio,
                                        ["01", "02", "03", "04", "05", "06", "07", "08",
                                         "09", "10", "11", "12", "13", "14", "15", "16",
                                         "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                                         "30", "31"])
        self.dia2.grid(row=5, column=3, padx=10, pady=10, sticky="ew")

        self.etiqueta_mes2 = CTkLabel(self.frame_datos_negocio, text="Mes: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta_mes2.grid(row=6, column=2, padx=10, pady=10, sticky="w")

        self.mes2 = LtkComboBoxLine(self.frame_datos_negocio,
                                        ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                                         "Septiembre", "Octubre", "Noviembre", "Diciembre"])
        self.mes2.grid(row=6, column=3, padx=10, pady=10, sticky="ew")

        self.etiqueta2 = CTkLabel(self.frame_datos_negocio, text="Año: ",
                                     font=("Poppins", 12, "bold"))
        self.etiqueta2.grid(row=7, column=2, padx=10, pady=10, sticky="w")

        self.año2 = LtkComboBoxLine(self.frame_datos_negocio,
                                       ["2005", "2006", "2007", "2008",
                                        "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                                        "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026",
                                        "2027", "2028", "2029",
                                        "2030", "2031"])
        self.año2.grid(row=7, column=3, padx=10, pady=10, sticky="ew")


        self.frame_botones = CTkFrame(self.ventana, fg_color="#FFFFFF")
        self.frame_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="e")


        self.boton_cancelar = LtkButtonFill(self.frame_botones, nombre="Cancelar", funcion=lambda: self.aceptar())
        self.boton_cancelar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.boton_aceptar = LtkButtonFill(self.frame_botones, nombre="Aceptar", funcion=lambda: self.aceptar())
        self.boton_aceptar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")


    def aceptar(self):
        pass




RegistrarPagosYReserva()
