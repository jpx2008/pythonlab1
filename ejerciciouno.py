from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("Titulo de la ventana")
ventana.geometry("800x600")

# acá se configuran las columnas, con el weight se le da un peso a cada columna, 
# para que se redimensionen de forma proporcional
ventana.grid_columnconfigure(0, weight=1)


# acá se configuran las filas, con el weight se le da un peso a cada fila,
# para que se redimensionen de forma proporcional
ventana.grid_rowconfigure(0, weight=1)

# acá se crea un frame, que es un contenedor para otros widgets
# ------------------------------------------------------------------------------
frame_principal=CTkFrame(master=ventana,
                    
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10,pady=10)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1,weight=1)

frame_principal.grid_rowconfigure([0,1], weight=1)

frame_inferior=CTkFrame(master=frame_principal,
                        corner_radius=0,
                        fg_color="#F01D1D")
frame_inferior.grid(row=1,column=0, sticky="nsew",padx=10,pady=10)
frame_inferior.grid_columnconfigure(0,weight=1)
frame_inferior.grid_columnconfigure(1,weight=1)

frame_inferior.grid_rowconfigure(0,weight=1)




pestañas=CTkTabview(
    master=frame_principal,
    corner_radius=0,
    fg_color="#1519db",
    segmented_button_fg_color="#1519db",
    segmented_button_selected_color="#1519db",
    segmented_button_selected_hover_color="#15db57",
    text_color="#ffffff"
)

pestañas.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10
)

formulario= pestañas.add("formulario")
registro= pestañas.add("Registro")

formulario.configure(fg_color="#1519db")
formulario.configure(fg_color="#15db57")

formulario.grid_columnconfigure(0,weight=1)
formulario.grid_rowconfigure(0,weight=1)
pestañas._segmented_button.grid_forget()


def click_boton_formulario():
    pestañas.set("formulario")
    
    
def click_boton_registro():
    pestañas.set("Registro")

boton_formulario=CTkButton(
    master=frame_inferior,
    text="formulario",
    fg_color="#1519DB",
    command=click_boton_formulario
)

boton_formulario.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

boton_registro=CTkButton(
    master=frame_inferior,
    text="registro",
    fg_color="#1519db",
    command=click_boton_registro
)
boton_registro.grid(
    row=1,
    column=1,
    padx=10,
    pady=10,
)




ventana.mainloop()