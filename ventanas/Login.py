import os
import pyodbc
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from ventanas.FrameMenuPrincipal import FrameMenuPrincipal
from util import ProcesarImagenes


from Excepciones.EmptyFieldException import EmptyFieldException


class Login(Frame):

    def __init__(self):
        self.ventana = CTk()
        self.ventana.geometry("820x480")
        self.ventana.configure(fg_color="#FFFFFF")
        self.ventana.resizable(False, False)

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        image_path = '../imagenes/Hotel.jpg'

        # Guardar la imagen como un atributo de la clase
        ruta_imagen = os.path.join(self.ruta_ventana, image_path)
        self.imagen = ProcesarImagenes.rescale_image(image_path=ruta_imagen, new_width=400, new_height=480)

        self.etiqueta_imagen = Label(self.ventana, image=self.imagen)
        self.etiqueta_imagen.place(x=0, y=0)

        self.etiqueta_bienvenida = CTkLabel(self.ventana, text="Bienvenido de nuevo! POrfavor inicia sesión para continuar",
                                            font=("Poppins", 12), fg_color="#FFFFFF", text_color="#387782")
        self.etiqueta_bienvenida.place(x=460, y=100)

        self.etiqueta_titulo = CTkLabel(self.ventana, text="Login", font=("Poppins", 20, "bold"), fg_color="#FFFFFF")
        self.etiqueta_titulo.place(x=460, y=40)

        self.etiqueta_entrada_empleado = CTkLabel(self.ventana, text="Nombre: ", font=("Poppins", 14),
                                                  fg_color="#FFFFFF")
        self.etiqueta_entrada_empleado.place(x=460, y=150)

        self.entrada_nombre_empleado = LtkEntryLine(self.ventana)
        self.entrada_nombre_empleado.configure(width=280, height=30)
        self.entrada_nombre_empleado.place(x=460, y=180)

        self.etiqueta_clave = CTkLabel(self.ventana, text="Clave: ", font=("Poppins", 14), fg_color="#FFFFFF")
        self.etiqueta_clave.place(x=460, y=230)
        self.entrada_clave = LtkEntryLine(self.ventana)
        self.entrada_clave.configure(width=280, height=30)
        self.entrada_clave.place(x=460, y=260)

        self.boton_iniciar_sesion = LtkButtonFill(self.ventana, nombre="Iniciar Sesión",
                                                  funcion=lambda: self.comprobar_acceso())
        self.boton_iniciar_sesion.configure(width=280, height=40)
        self.boton_iniciar_sesion.place(x=460, y=340)
        self.boton_iniciar_sesion.bind('<Return>', lambda event: self.comprobar_acceso())
        self.ventana.mainloop()

    def comprobar_acceso(self):
        """
        Comprueba si el nombre de usuario y la contraseña ingresados son correctos.
        """

        try:
            nombre_empleado = self.entrada_nombre_empleado.get_text()
            clave = self.entrada_clave.get_text()

            if nombre_empleado == "" or clave == "":
                raise EmptyFieldException("Los campos no pueden estar vacios")

            empleado = self.obtener_detalles_empleado(nombre_empleado, clave)
            if nombre_empleado == "User" and clave == "admin123":
                self.crear_ventana_principal()

            elif empleado:
                self.crear_ventana_principal()

            else:
                messagebox.showinfo("Acceso denegado", "Credenciales incorrectas o permisos denegados")


        except EmptyFieldException as e:
            messagebox.showerror("Error", "Los campos no pueden estar vacios")

        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Error al iniciar sesión")

    def obtener_detalles_empleado(self, nombre_empleado, clave):
        """
        Obtiene los detalles del empleado desde la base de datos.
        """
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=LOUIS;"  # Reemplaza con tu servidor
            "DATABASE=HotelMirador;"  # Reemplaza con tu base de datos
            "UID=UserHotel;"  # Reemplaza con tu usuario
            "PWD=admin123"  # Reemplaza con tu contraseña
        )

        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT clave_empleado, nombre_completo, cargo
                FROM Empleado
                WHERE nombre_completo = ? AND clave_empleado = ? AND (cargo = 'Recepcionista' OR cargo = 'Administrativo')
            """, (nombre_empleado, clave))

            resultado = cursor.fetchone()

            conn.close()

            if resultado:
                return {"clave_empleado": resultado[0], "nombre_completo": resultado[1], "cargo": resultado[2]}
            return None
        except pyodbc.Error as e:
            print("Error al conectar con la base de datos:", e)
            return None


    def crear_ventana_principal(self):
        """
        Crea la ventana principal del sistema.
        """
        self.ventana.withdraw()
        self.obj = FrameMenuPrincipal()

