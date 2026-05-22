from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("ejemplo de frame en customtkinter")
ventana.geometry("900x500")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal=CTkFrame(master=ventana,
                        fg_color="#e67e7e",
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=100,pady=100)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)


frame_principal.grid_rowconfigure(0, weight=1)














frame_izquierdo=CTkFrame(master=frame_principal,
                         fg_color="#8fe67e",
                         corner_radius=0)
frame_izquierdo.grid(row=0, column=0 ,sticky="snew", padx=5, pady=5)
frame_izquierdo.grid_columnconfigure(0, weight=1)
frame_izquierdo.grid_columnconfigure(1, weight=1)
frame_izquierdo.grid_rowconfigure(0, weight=1)
frame_izquierdo.grid_rowconfigure(1, weight=1)

frame_izquierdoprincipal=CTkFrame(master=frame_izquierdo,
                         fg_color="#d66e19",
                         corner_radius=0)
frame_izquierdoprincipal.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)




frame_izquierdosecundario=CTkFrame(master=frame_izquierdo,
                         fg_color="#d61942",
                            corner_radius=0)
frame_izquierdosecundario.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)














frame_derecho=CTkFrame(master=frame_principal,
                         fg_color="#dd7ee6",
                         corner_radius=0)
frame_derecho.grid(row=0, column=1 ,sticky="wsne", padx=5, pady=5)
frame_derecho.grid_columnconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(0, weight=1)
frame_derecho.grid_rowconfigure(1, weight=1)

frame_derechoprincipal=CTkFrame(master=frame_derecho,
                         fg_color="#d66e19",
                         corner_radius=0)
frame_derechoprincipal.grid(row=0, column=0, sticky="snew", padx=5, pady=5)

frame_derechosecundario=CTkFrame(master=frame_derecho,
                         fg_color="#d61942",
                            corner_radius=0)
frame_derechosecundario.grid(row=1, column=0, sticky="snew", padx=5, pady=5)





ventana.mainloop()


