import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    etiqueta_saludar.config(text=f"hola, (nombre)!")

ventana =tk.Tk()
ventana.title("hol")

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)

entrada_nombre_inst = tk.Entry(ventana, text="nombre")
entrada_nombre_inst.grid(row=0 , column=0, pady=0, stick="w")

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0 , column=0, pady=0, stick="ew") 

boton_saludar = tk.Button(ventana, text="saludar", command=saludar)
boton_saludar.grid(row=1 , column=0, columnspan=2, padx=10, pady=0,  stick="ew") 

etiqueta_saludar = tk.Label(ventana, text="")
etiqueta_saludar.grid(row=2 , column=0, columnspan=2, padx=5, pady=0,  stick="ew") 

ventana.mainloop()