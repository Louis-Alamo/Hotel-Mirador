import tkinter as tk
from tkinter import ttk

class TreeviewTable:
    def __init__(self, master, column_names, rows):
        self.scrollbar_vertical = ttk.Scrollbar(master, orient="vertical")
        self.scrollbar_horizontal = ttk.Scrollbar(master, orient="horizontal")

        self.treeview = ttk.Treeview(master, yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set)
        self.treeview["columns"] = column_names

        # Ocultar la columna fantasma
        self.treeview.column("#0", width=0, stretch=False)

        for col in column_names:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, stretch=True)  # Ajustar el ancho de la columna automáticamente

        for row in rows:
            self.treeview.insert('', 'end', values=row)

        self.scrollbar_vertical.config(command=self.treeview.yview)
        self.scrollbar_horizontal.config(command=self.treeview.xview)


    def actualizar_datos(self, nuevos_datos):
        # Borrar todos los elementos existentes
        for elemento in self.treeview.get_children():
            self.treeview.delete(elemento)

        # Agregar los nuevos datos
        for fila in nuevos_datos:
            self.treeview.insert('', 'end', values=fila)

    def obtener_datos_seleccionados(self):
        elementos_seleccionados = self.treeview.selection()
        datos_seleccionados = [self.treeview.item(elemento)['values'] for elemento in elementos_seleccionados]
        return datos_seleccionados
    def pack(self, **kwargs):
        self.scrollbar_vertical.pack(side="right", fill="y")
        self.scrollbar_horizontal.pack(side="bottom", fill="x")
        self.treeview.pack(**kwargs)