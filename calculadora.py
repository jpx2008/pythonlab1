from customtkinter import *

set_default_color_theme("dark-blue")

ventana = CTk()
ventana.title("calculadora")
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
                        fg_color="#e67e7e",
                        corner_radius=0)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=100,pady=100)
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_principal.grid_columnconfigure(2, weight=1)
frame_principal.grid_columnconfigure(3, weight=1)

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=1)
frame_principal.grid_rowconfigure(3, weight=1)
frame_principal.grid_rowconfigure(4, weight=1)
frame_principal.grid_rowconfigure(5, weight=1)
frame_principal.grid_rowconfigure(6, weight=1)


def funcion_boton_1():
    print(f"%")



boton_1_porcentaje = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="%",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_1,
)
boton_1_porcentaje.grid(row=1, column=0, padx=10, pady=10)

boton_2_CE = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="CE",
    anchor="center",
    font=("Montserrat", 16),
)
boton_2_CE.grid(row=1, column=1, padx=10, pady=10)


boton_3_C = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="C",
    anchor="center",
    font=("Montserrat", 16),
)
boton_3_C.grid(row=1, column=2, padx=10, pady=10)


boton_4_borrar = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="<-",
    anchor="center",
    font=("Montserrat", 16),
)
boton_4_borrar.grid(row=1, column=3, padx=10, pady=10)



boton_5_division1 = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="1/x",
    anchor="center",
    font=("Montserrat", 16),
)
boton_5_division1.grid(row=2, column=0, padx=10, pady=10)


boton_potencia = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="x^y",
    anchor="center",
    font=("Montserrat", 16),
)
boton_potencia.grid(row=2, column=1, padx=10, pady=10)

boton_raiz = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="2√x",
    anchor="center",
    font=("Montserrat", 16),
)
boton_raiz.grid(row=2, column=2, padx=10, pady=10)



boton_dividir = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="÷",
    anchor="center",
    font=("Montserrat", 16),
)
boton_dividir.grid(row=2, column=3, padx=10, pady=10)


boton_num7 = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="7",
    anchor="center",
    font=("Montserrat", 16),
)
boton_num7.grid(row=3, column=0, padx=10, pady=10)

boton_num8 = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="8",
    anchor="center",
    font=("Montserrat", 16),
)
boton_num8.grid(row=3, column=1, padx=10, pady=10)


boton_num9= CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="9",
    anchor="center",
    font=("Montserrat", 16),
)
boton_num9.grid(row=3, column=2, padx=10, pady=10)







    
boton_multiplicar = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="x",
    anchor="center",
    font=("Montserrat", 16),
)

boton_multiplicar.grid(row=3, column=3, padx=10, pady=10)

def funcion_boton_4():
    print("4")
    
boton_num4 = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="4",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_4
    
)
boton_num4.grid(row=4, column=0, padx=10, pady=10)




def funcion_boton_5():
    print("5")
boton_num5= CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="5",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_5

)
boton_num5.grid(row=4, column=1, padx=10, pady=10)





def funcion_boton_6():
    print("6")


boton_num6 = CTkButton(
    master=frame_principal,
    width=80,
    height=30,
    corner_radius=0,
    text="6",
    anchor="center",
    font=("Montserrat", 16),
    command=funcion_boton_6,
)
boton_num6.grid(row=4, column=2, padx=10, pady=10)










ventana.mainloop()