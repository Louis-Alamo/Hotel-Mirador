from front_end.ventanas.Login import Login
from tkinter import Tk

if __name__ == "__main__":
    ventana = Tk()
    n = Login(ventana, 820, 480)
    n.grid(row=0, column=0)
    ventana.mainloop()