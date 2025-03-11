import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Ruta del archivo donde se guardan los invitados
ruta_archivo = "C:/Quinto/archivo.txt"

def mostrar_invitados():
    """Muestra la lista de invitados en un cuadro de mensaje."""
    try:
        with open(ruta_archivo, "r") as archivo:
            invitados = archivo.readlines()
            # Crear una lista formateada de los invitados
            lista_invitados = "Lista de invitados:\n" + "\n".join(f"{i + 1}. {invitado.strip()}" for i, invitado in enumerate(invitados))
            messagebox.showinfo("Lista de Invitados", lista_invitados)
    except FileNotFoundError:
        messagebox.showwarning("Advertencia", "No hay invitados en la lista.")

def agregar_invitado():
    """Agrega un nuevo invitado a la lista, solicitando su nombre y detalles adicionales."""
    nombre_invitado = simpledialog.askstring("Agregar Invitado", "Ingrese el nombre del invitado:")
    if nombre_invitado:
        cuota = 100.00  # Cuota por invitado
        # Preguntar si el invitado llevará automóvil y si llevará regalo o dinero
        lleva_auto = simpledialog.askstring("Auto", f"{nombre_invitado}, ¿llevará automóvil? (sí/no):")
        lleva_regalo = simpledialog.askstring("Regalo", f"{nombre_invitado}, ¿llevará regalo o dinero en efectivo? (regalo/efectivo):")
        
        # Guardar la información del invitado en el archivo
        with open(ruta_archivo, "a") as archivo:
            archivo.write(f"{nombre_invitado} - Cuota: Q{cuota:.2f}, Lleva auto: {lleva_auto}, Lleva regalo: {lleva_regalo}\n")
        
        messagebox.showinfo("Éxito", f"{nombre_invitado} ha sido agregado a la lista de invitados.")

def eliminar_invitado():
    """Elimina un invitado de la lista, solicitando el número del invitado a eliminar."""
    try:
        with open(ruta_archivo, "r") as archivo:
            invitados = archivo.readlines()
        
        if not invitados:
            messagebox.showwarning("Advertencia", "No hay invitados en la lista.")
            return
        
        # Crear una lista formateada de los invitados para mostrar
        lista_invitados = "\n".join(f"{i + 1}. {invitado.strip()}" for i, invitado in enumerate(invitados))
        num_invitado = simpledialog.askinteger("Eliminar Invitado", f"Ingrese el número del invitado que desea eliminar:\n{lista_invitados}")
        
        if num_invitado is not None and 1 <= num_invitado <= len(invitados):
            nombre_eliminado = invitados.pop(num_invitado - 1).strip()  # Eliminar el invitado seleccionado
            with open(ruta_archivo, "w") as archivo:
                archivo.writelines(invitados)  # Escribir la lista actualizada en el archivo
            messagebox.showinfo("Éxito", f"Se ha eliminado al invitado: {nombre_eliminado}")
        else:
            messagebox.showwarning("Advertencia", "Número de invitado no válido.")
    except FileNotFoundError:
        messagebox.showwarning("Advertencia", "No hay invitados en la lista.")

def mostrar_resumen():
    """Muestra un resumen del total de invitados y la cuota total."""
    try:
        with open(ruta_archivo, "r") as archivo:
            invitados = archivo.readlines()
        
        if not invitados:
            messagebox.showwarning("Advertencia", "No hay invitados en la lista.")
            return
        
        total_invitados = len(invitados)  # Contar el número total de invitados
        total_cuota = total_invitados * 100.00  # Calcular la cuota total
        
        mensaje_resumen = f"Total de invitados: {total_invitados}\nTotal de cuota: Q{total_cuota:.2f}"
        messagebox.showinfo("Resumen de Invitados", mensaje_resumen)
    except FileNotFoundError:
        messagebox.showwarning("Advertencia", "No hay invitados en la lista.")

def mostrar_ubicacion():
    """Muestra la ubicación de la boda en un cuadro de mensaje."""
    messagebox.showinfo("Ubicación de la Boda", "Hacienda San Vicente 25/2/2035.")

def crear_ventana():
    """Crea la ventana principal de la aplicación y configura los botones."""
    ventana = tk.Tk()
    ventana.title("Gestión de Invitados para la Boda")
    ventana.geometry("500x400")
    ventana.configure(bg="#f0f0f0")

    # Frame para los botones
    frame_botones = ttk.Frame(ventana, padding="10")
    frame_botones.pack(pady=20)

    # Botones para las diferentes funciones
    btn_mostrar = ttk.Button(frame_botones, text="Mostrar lista de invitados", command=mostrar_invitados)
    btn_mostrar.grid(row=0, column=0, padx=10, pady=10)

    btn_agregar = ttk.Button(frame_botones, text="Agregar un nuevo invitado", command=agregar_invitado)
    btn_agregar.grid(row=0, column=1, padx=10, pady=10)

    btn_eliminar = ttk.Button(frame_botones, text="Eliminar un invitado", command=eliminar_invitado)
    btn_eliminar.grid(row=1, column=0, padx=10, pady=10)

    btn_resumen = ttk.Button(frame_botones, text="Mostrar resumen de invitados", command=mostrar_resumen)
    btn_resumen.grid(row=1, column=1, padx=10, pady=10)

    btn_ubicacion = ttk.Button(ventana, text="Ubicación de la boda", command=mostrar_ubicacion)
    btn_ubicacion.pack(pady=10)

    btn_salir = ttk.Button(ventana, text="Salir", command=ventana.quit)
    btn_salir.pack(pady=10)

    ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica

# Llamar a la función para crear la ventana
crear_ventana()