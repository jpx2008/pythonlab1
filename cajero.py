from customtkinter import *

set_default_color_theme("dark-blue")

# =========================
# VENTANA
# =========================

ventana = CTk()
ventana.title("CAJERO AUTOMATICO")
ventana.geometry("1000x700")

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# =========================
# VARIABLE SALDO
# =========================

saldo_actual = 200000

# =========================
# FRAME PRINCIPAL
# =========================

frame_principal = CTkFrame(
    master=ventana,
    fg_color="#7c7c7c"
)

frame_principal.grid(
    row=0,
    column=0,
    sticky="nsew"
)

# CONFIGURACION

frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_rowconfigure(1, weight=1)
frame_principal.grid_rowconfigure(2, weight=8)

frame_principal.grid_columnconfigure(0, weight=1)

# =========================
# TITULO
# =========================

labelnombre = CTkLabel(
    frame_principal,
    text="ESCOGA UNA OPCION DE SU CAJERO",
    font=("Arial", 35)
)

labelnombre.grid(
    row=0,
    column=0,
    pady=20
)

# =========================
# FRAME BOTONES
# =========================

frame_botones = CTkFrame(
    master=frame_principal,
    fg_color="transparent"
)

frame_botones.grid(
    row=1,
    column=0,
    pady=10
)

# =========================
# CONTENEDOR
# =========================

contenedor = CTkFrame(
    master=frame_principal,
    fg_color="transparent"
)

contenedor.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=20,
    pady=20
)

contenedor.grid_rowconfigure(0, weight=1)
contenedor.grid_columnconfigure(0, weight=1)

# =====================================================
# PAGINA CONSULTA DE SALDO
# =====================================================

pagina_formulario = CTkFrame(
    master=contenedor,
    fg_color="#2b2b2b",
    corner_radius=20
)

pagina_formulario.grid_columnconfigure(0, weight=1)
pagina_formulario.grid_columnconfigure(1, weight=1)

# TITULO

label1 = CTkLabel(
    pagina_formulario,
    text="CONSULTA DE SALDO",
    font=("Arial", 35)
)

label1.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)

# LABEL TEXTO

labelsaldo = CTkLabel(
    pagina_formulario,
    text="Tu saldo disponible es:",
    font=("Arial", 30)
)

labelsaldo.grid(
    row=1,
    column=0,
    pady=20
)

# LABEL SALDO

saldo = CTkLabel(
    pagina_formulario,
    text=f"${saldo_actual:,}",
    font=("Arial", 30)
)

saldo.grid(
    row=1,
    column=1,
    pady=20
)

# =====================================================
# FUNCIONES
# =====================================================

def depositar():

    global saldo_actual

    saldo_actual += 5000

    saldo.configure(text=f"${saldo_actual:,}")

def retirar():

    global saldo_actual

    saldo_actual -= 5000

    saldo.configure(text=f"${saldo_actual:,}")

# =====================================================
# BOTONES OPERACIONES
# =====================================================

boton_depositar = CTkButton(
    pagina_formulario,
    text="DEPOSITAR $5000",
    command=depositar,
    width=200,
    height=40
)

boton_depositar.grid(
    row=2,
    column=0,
    pady=30
)

boton_retirar = CTkButton(
    pagina_formulario,
    text="RETIRAR $5000",
    command=retirar,
    width=200,
    height=40
)

boton_retirar.grid(
    row=2,
    column=1,
    pady=30
)

# =====================================================
# PAGINA TRANSFERENCIA
# =====================================================

pagina_registro = CTkFrame(
    master=contenedor,
    fg_color="#3f3f42",
    corner_radius=20
)

label2 = CTkLabel(
    pagina_registro,
    text="TRANSFERENCIA",
    font=("Arial", 35)
)

label2.grid(
    row=0,
    column=0,
    pady=50,
    padx=50
)

# =====================================================
# PAGINA RETIRO
# =====================================================

pagina_retiro = CTkFrame(
    master=contenedor,
    fg_color="#1f1f1f",
    corner_radius=20
)

label3 = CTkLabel(
    pagina_retiro,
    text="RETIRO DE DINERO",
    font=("Arial", 35)
)

label3.grid(
    row=0,
    column=0,
    pady=50,
    padx=50
)

# =====================================================
# PAGINA DEPOSITO
# =====================================================

pagina_deposito = CTkFrame(
    master=contenedor,
    fg_color="#444444",
    corner_radius=20
)

label4 = CTkLabel(
    pagina_deposito,
    text="DEPOSITAR DINERO",
    font=("Arial", 35)
)

label4.grid(
    row=0,
    column=0,
    pady=50,
    padx=50
)

# =====================================================
# OCULTAR PAGINAS
# =====================================================

def ocultar_paginas():

    pagina_formulario.grid_forget()
    pagina_registro.grid_forget()
    pagina_retiro.grid_forget()
    pagina_deposito.grid_forget()

# =====================================================
# ABRIR PAGINAS
# =====================================================

def abrir_formulario():

    ocultar_paginas()

    pagina_formulario.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

def abrir_registro():

    ocultar_paginas()

    pagina_registro.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

def abrir_retiro():

    ocultar_paginas()

    pagina_retiro.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

def abrir_deposito():

    ocultar_paginas()

    pagina_deposito.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

# =====================================================
# BOTONES MENU
# =====================================================

boton1 = CTkButton(
    frame_botones,
    text="CONSULTAR SALDO",
    command=abrir_formulario
)

boton1.grid(
    row=0,
    column=0,
    padx=10
)

boton2 = CTkButton(
    frame_botones,
    text="TRANSFERENCIA",
    command=abrir_registro
)

boton2.grid(
    row=0,
    column=1,
    padx=10
)

boton3 = CTkButton(
    frame_botones,
    text="RETIRO",
    command=abrir_retiro
)

boton3.grid(
    row=0,
    column=2,
    padx=10
)

boton4 = CTkButton(
    frame_botones,
    text="DEPOSITO",
    command=abrir_deposito
)

boton4.grid(
    row=0,
    column=3,
    padx=10
)

# =====================================================
# PAGINA INICIAL
# =====================================================

abrir_formulario()

# =====================================================
# MAINLOOP
# =====================================================

ventana.mainloop()