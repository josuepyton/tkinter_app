import tkinter as tk
from tkinter import messagebox
venta_principal = tk.Tk()
venta_principal.title("Sistema de Ventas")
venta_principal.geometry("900x600")
venta_principal.config(bg="lightblue")
etiqueta_titulo = tk.Label(venta_principal, text="mk baby", font=("Arial", 24), bg="lightblue")
etiqueta_titulo.pack(pady=20)
etiqueta_titulo.pack()
venta_principal.mainloop()