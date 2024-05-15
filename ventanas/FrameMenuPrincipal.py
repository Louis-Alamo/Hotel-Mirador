import os
from customtkinter import *
from tkinter import Frame
from componentes_graficos.LtkButton import LtkImageTextButton
from componentes_graficos.LtkFecha import LtkFecha
from componentes_graficos.LtkReloj import LtkReloj



from ventanas.FrameEmpleados import FrameEmpleados
from ventanas.FrameHabitaciones import FrameHabitacion
from ventanas.FrameServiciosAdicionales import FrameServiciosAdicionales
from ventanas.FrameClientes import FrameClientes
from ventanas.FrameReservas import FrameReservas    

from util.ProcesarImagenes import rescale_image_ctk

class FrameMenuPrincipal():

    def __init__(self):

        self.ventana = CTkToplevel()

        self.ventana.geometry("1200x650")
        self.ventana.title("Sistema de Gestión de Hotel")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#FFFFFF")

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        print(self.ruta_ventana)

        self.frameBarraIzquierda = CTkFrame(self.ventana, fg_color="#DCF0F1", width=210, height=650)
        self.frameBarraIzquierda.place(x=0, y=0)

        self.frameBarraSuperior = CTkFrame(self.ventana, fg_color="#FFFFFF",width=990, height=80)
        self.frameBarraSuperior.place(x=210, y=0)

        self.etiqueta_titulo_hotel = CTkLabel(self.ventana, text="Hotel mirador",fg_color="#DCF0F1", font=("Poppins", 20, "bold"))
        self.etiqueta_titulo_hotel.place(x=40, y=20)

        self.crear_botones_menu_lateral_izquierdo()
        self.cargar_menu_superior()

        self.ventana.mainloop()


    def crear_botones_menu_lateral_izquierdo(self):
        #Cargar las imagenes correspondientes

        self.icono_principal = rescale_image_ctk(os.path.join(self.ruta_ventana,"..\\imagenes/iconos\\icono-principal.png"), 30,30)
        self.icono_habitaciones = rescale_image_ctk(os.path.join(self.ruta_ventana,"..\\imagenes/iconos\\icono-habitacion.png"), 30,30)
        self.icono_reserva = rescale_image_ctk(os.path.join(self.ruta_ventana,"..\\imagenes\\iconos\\icono-reserva.png"),30,30)
        self.icono_servicios = rescale_image_ctk(os.path.join(self.ruta_ventana,"..\\imagenes\\iconos\\icono-servicios.png"),30,30)
        self.icono_cliente = rescale_image_ctk(os.path.join(self.ruta_ventana,"..\\imagenes\\iconos\\icono-cliente.png"),30,30)
        self.icono_empleados = rescale_image_ctk(os.path.join(self.ruta_ventana,"..\\imagenes\\iconos\\icono-empleados.png"), 30,30)


        self.boton_principal = LtkImageTextButton(self.frameBarraIzquierda,self.icono_principal, funcion=lambda: self.menu_principal(), texto="Principal")
        self.boton_principal.configure(width=120)
        self.boton_principal.place(x=40,y=111)

        self.boton_habitaciones = LtkImageTextButton(self.frameBarraIzquierda,self.icono_habitaciones, funcion=lambda: self.menu_habitaciones(), texto="Habitaciones")
        self.boton_habitaciones.configure(width=120)
        self.boton_habitaciones.place(x=40,y=171)

        self.boton_reserva = LtkImageTextButton(self.frameBarraIzquierda,self.icono_reserva, funcion=lambda: self.menu_reserva(), texto="Reserva")
        self.boton_reserva.configure(width=120)
        self.boton_reserva.place(x=40,y=231)

        self.boton_servicios = LtkImageTextButton(self.frameBarraIzquierda,self.icono_servicios, funcion=lambda: self.menu_servicios(), texto="Servicios")
        self.boton_servicios.configure(width=120)
        self.boton_servicios.place(x=40,y=291)

        self.boton_cliente = LtkImageTextButton(self.frameBarraIzquierda,self.icono_cliente, funcion=lambda: self.menu_cliente(), texto="Cliente")
        self.boton_cliente.configure(width=120)
        self.boton_cliente.place(x=40,y=351)

        self.boton_empleados = LtkImageTextButton(self.frameBarraIzquierda,self.icono_empleados, funcion=lambda: self.menu_empleados(), texto="Empleados")
        self.boton_empleados.configure(width=120)
        self.boton_empleados.place(x=40,y=411)


    def cargar_menu_superior(self):


        self.reloj = LtkReloj(self.frameBarraSuperior)
        self.reloj.place(x=30, y=20)

        self.fecha = LtkFecha(self.frameBarraSuperior)
        self.fecha.place(x=250, y=20)


    def menu_principal(self):
        pass

    def menu_habitaciones(self):
        self.frame_informacion_relevante = FrameHabitacion(self.ventana, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)

    def menu_reserva(self):
        self.frame_informacion_relevante = FrameReservas(self.ventana, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)

    def menu_servicios(self):
        self.frame_informacion_relevante = FrameServiciosAdicionales(self.ventana, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)

    def menu_cliente(self):
        self.frame_informacion_relevante = FrameClientes(self.ventana, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)

    def menu_empleados(self):
        self.frame_informacion_relevante = FrameEmpleados(self.ventana, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)


    def menu_reportes(self):
        pass

