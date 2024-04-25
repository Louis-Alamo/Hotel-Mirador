from typing import Union

from customtkinter import CTkFrame, CTkLabel
from tkinter import Frame
from front_end.componentes_graficos.individuales.LtkButton.LtkImageTextButton import LtkImageTextButton
from front_end.componentes_graficos.compuestos.LtkFecha import LtkFecha
from front_end.componentes_graficos.compuestos.LtkReloj import LtkReloj
from front_end.ventanas.FrameEmpleados import FrameEmpleados
from front_end.ventanas.FrameHabitaciones import FrameHabitacion
from front_end.ventanas.FrameServiciosAdicionales import FrameServiciosAdicionales

from util.ProcesarImagenes import rescale_image_ctk

class FrameMenuPrincipal(Frame):

    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)

        master.geometry("1200x650")
        master.title("Sistema de Gestión de Hotel")
        master.resizable(False, False)
        master.config(bg="#FFFFFF")

        self.master = master



        self.frameBarraIzquierda = CTkFrame(master, fg_color="#DCF0F1", width=210, height=650)
        self.frameBarraIzquierda.place(x=0, y=0)

        self.frameBarraSuperior = CTkFrame(master, fg_color="transparent",width=990, height=80)
        self.frameBarraSuperior.place(x=210, y=0)

        self.imagen_titulo_hotel = rescale_image_ctk("../../imagenes/titulo-hotel.png", 500, 200)
        self.etiqueta_titulo_hotel = CTkLabel(self.frameBarraIzquierda, image=self.imagen_titulo_hotel)
        self.etiqueta_titulo_hotel.place(x=20, y=20)

        self.crear_botones_menu_lateral_izquierdo()
        self.cargar_menu_superior()


    def crear_botones_menu_lateral_izquierdo(self):
        #Cargar las imagenes correspondientes

        self.icono_principal = rescale_image_ctk("../../imagenes/iconos/icono-principal.png", 30,30)
        self.icono_habitaciones = rescale_image_ctk("../../imagenes/iconos/icono-habitacion.png", 30,30)
        self.icono_reserva = rescale_image_ctk("../../imagenes/iconos/icono-reserva.png",30,30)
        self.icono_servicios = rescale_image_ctk("../../imagenes/iconos/icono-servicios.png",30,30)
        self.icono_cliente = rescale_image_ctk("../../imagenes/iconos/icono-cliente.png",30,30)
        self.icono_empleados = rescale_image_ctk("../../imagenes/iconos/icono-empleados.png", 30,30)


        self.boton_principal = LtkImageTextButton(self.frameBarraIzquierda,self.icono_principal, funcion=lambda: self.menu_principal(), texto="Principal")
        self.boton_principal.place(x=40,y=111)

        self.boton_habitaciones = LtkImageTextButton(self.frameBarraIzquierda,self.icono_habitaciones, funcion=lambda: self.menu_habitaciones(), texto="Habitaciones")
        self.boton_habitaciones.place(x=40,y=171)

        self.boton_reserva = LtkImageTextButton(self.frameBarraIzquierda,self.icono_reserva, funcion=lambda: self.menu_reserva(), texto="Reserva")
        self.boton_reserva.place(x=40,y=231)

        self.boton_servicios = LtkImageTextButton(self.frameBarraIzquierda,self.icono_servicios, funcion=lambda: self.menu_servicios(), texto="Servicios")
        self.boton_servicios.place(x=40,y=291)

        self.boton_cliente = LtkImageTextButton(self.frameBarraIzquierda,self.icono_cliente, funcion=lambda: self.menu_cliente(), texto="Cliente")
        self.boton_cliente.place(x=40,y=351)

        self.boton_empleados = LtkImageTextButton(self.frameBarraIzquierda,self.icono_empleados, funcion=lambda: self.menu_empleados(), texto="Empleados")
        self.boton_empleados.place(x=40,y=411)


    def cargar_menu_superior(self):


        self.reloj = LtkReloj(self.frameBarraSuperior)
        self.reloj.place(x=30, y=20)

        self.fecha = LtkFecha(self.frameBarraSuperior)
        self.fecha.place(x=250, y=20)


    def menu_principal(self):
        pass

    def menu_habitaciones(self):
        self.frame_informacion_relevante = FrameHabitacion(self.master, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)

    def menu_reserva(self):
        pass

    def menu_servicios(self):
        self.frame_informacion_relevante = FrameServiciosAdicionales(self.master, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)

    def menu_cliente(self):
        pass

    def menu_empleados(self):
        self.frame_informacion_relevante = FrameEmpleados(self.master, bg="white", width=990, height=570)
        self.frame_informacion_relevante.pack_propagate(False)
        self.frame_informacion_relevante.place(x=240, y=80)


    def menu_reportes(self):
        pass


import tkinter as tk
ventana = tk.Tk()
frame = FrameMenuPrincipal(ventana)
frame.pack()
ventana.mainloop()

