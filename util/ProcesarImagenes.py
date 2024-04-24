from PIL import Image, ImageTk
from customtkinter import CTkImage
def rescale_image(image_path, new_width, new_height):
    img = Image.open(image_path)
    img_rescaled = img.resize((new_width, new_height))

    # Convertir la imagen PIL a una imagen Tkinter
    tk_image = ImageTk.PhotoImage(img_rescaled)

    return tk_image

def rescale_image_ctk(image_path, new_width, new_height):
    img = Image.open(image_path)
    img_rescaled = img.resize((new_width, new_height))

    # Convertir la imagen PIL a una imagen CTkImage
    ctk_image = CTkImage(img_rescaled)

    return ctk_image

