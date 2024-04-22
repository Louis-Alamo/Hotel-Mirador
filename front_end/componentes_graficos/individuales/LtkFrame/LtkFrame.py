from tkinter import Frame

class LtkFrame(Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.config(
            bg="#FFFFFF",
        )

        self.grid_rowconfigure(0, minsize=10)
        self.grid_rowconfigure(1, minsize=10)
        self.grid_columnconfigure(0, minsize=10)
        self.grid_columnconfigure(1, minsize=10)