import tkinter as tk
def window(window_text:str,window_title:str = "to-do-list",window_size:str =  "700x700",window_bg:str = "#e14d2d"):
    """ 
    Genera la ventana principal
    Args:
        window_text(str): Descripcion de la ventana.
        window_title(str): Titulo de la ventan.
        window_size(str): Tamaño de la ventan
        window_bg(str): Color de la ventana
    Retun: 
        None: La funcion no retorna nada pues no es necesario
    """
    # Crear la ventana principal
    ventana = tk.Tk()

    # Configuración de la ventana
    ventana.title(window_title)
    ventana.geometry(window_size)  # Ancho x Alto
    ventana.config(bg= window_bg)
    # Agregar widgets (elementos gráficos)
    label = tk.Label(ventana, text=window_text,font=("Arial",15),fg="#ece8e7",bg=window_bg)
    label.pack()

    # Widgets
    space = tk.Label(ventana,background="#e14d2d")
    label = tk.Label(ventana, text="Agregar tarea",background=window_bg,font=("Arial",15),fg="#ece8e7")
    label.pack(pady=5)
    entry = tk.Entry(ventana)
    entry.pack(pady=5)

    button = tk.Button(ventana, text="Añadir")
    button.pack()

    # Iniciar el bucle principal
    ventana.mainloop()