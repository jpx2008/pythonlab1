from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("500x900")
gris="#5F5F5F"
blanco="#ffffff"
negro="#000000"
transparente="transparent"
boton={
    "width":80,
    "height":30,
    "corner_radius":0,
    "anchor":"center",
    "font": ("Montserrat", 16, "bold")
    
}

boton_volumen={
    "width":120,
    "height":80,
    "corner_radius":0,
    "anchor":"center",
    "font": ("Montserrat", 26, "bold")
}

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal=CTkFrame(master=ventana,
                        fg_color=gris,
                        corner_radius=20)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=20,pady=20)
frame_principal.grid_columnconfigure(0, weight=1)


frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)

frame_musica=CTkFrame(master=frame_principal,
                      fg_color=blanco,
                      corner_radius=20)
frame_musica.grid(row=0,column=0,sticky="nsew",padx=20,pady=20)

frame_controles=CTkFrame(master=frame_principal,
                         fg_color="#d798da",
                         corner_radius=1200)
frame_controles.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
frame_controles.grid_columnconfigure(0,weight=1)
frame_controles.grid_columnconfigure(1,weight=1)
frame_controles.grid_columnconfigure(2,weight=1)
frame_controles.grid_rowconfigure(0,weight=1)
frame_controles.grid_rowconfigure(1,weight=1)  
frame_controles.grid_rowconfigure(2,weight=1)



boton_pausarepoducir = CTkButton(
    master=frame_controles,
    text="pausa/reproducir",
    fg_color=transparente,
    text_color=blanco,
    **boton
    
)

boton_pausarepoducir.grid(
    row=1,
    column=1,
)
boton_suma=CTkButton(
    master=frame_controles,
    text="+",
    fg_color=transparente,
    text_color=blanco,
    **boton_volumen
)
boton_suma.grid(row=0,column=1)

boton_resta=CTkButton(
    master=frame_controles,
    text="-",
    fg_color=transparente,
    text_color=blanco,
    **boton_volumen
    
)
boton_resta.grid(
    row=2,
    column=1
)

boton_anterior=CTkButton(
    master=frame_controles,
    text="anterior",
    fg_color=transparente,
    text_color=blanco,
    **boton
)
boton_anterior.grid(
    row=1,
    column=0
)

boton_siguiente=CTkButton(
    master=frame_controles,
    text="siguiente",
    fg_color=transparente,
    text_color=blanco,
    **boton
)
boton_siguiente.grid(
    row=1,
    column=2
)
ventana.mainloop()