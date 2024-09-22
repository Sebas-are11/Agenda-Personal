import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Contenedores (Frames)
        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(pady=10)

        self.frame_middle = tk.Frame(self.root)
        self.frame_middle.pack(pady=10)

        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.pack(pady=10)

        # Etiquetas y campos de entrada para agregar eventos
        tk.Label(self.frame_top, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_top, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_top, text="Hora").grid(row=0, column=2, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_top, width=10)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_top, text="Descripción").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_top, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # TreeView para mostrar los eventos
        self.event_tree = ttk.Treeview(self.frame_middle, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.event_tree.heading("Fecha", text="Fecha")
        self.event_tree.heading("Hora", text="Hora")
        self.event_tree.heading("Descripción", text="Descripción")
        self.event_tree.column("Fecha", width=100)
        self.event_tree.column("Hora", width=50)
        self.event_tree.column("Descripción", width=200)
        self.event_tree.pack()

        # Botones
        self.add_button = tk.Button(self.frame_bottom, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(self.frame_bottom, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=10)

        self.quit_button = tk.Button(self.frame_bottom, text="Salir", command=self.root.quit)
        self.quit_button.grid(row=0, column=2, padx=10)

    def add_event(self):
        # Obtener datos de los campos de entrada
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if date and time and desc:
            # Insertar los datos en el TreeView
            self.event_tree.insert("", "end", values=(date, time, desc))

            # Limpiar los campos de entrada
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")

    def delete_event(self):
        # Eliminar el evento seleccionado
        selected_item = self.event_tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar eliminación", "¿Seguro que deseas eliminar el evento seleccionado?")
            if confirm:
                self.event_tree.delete(selected_item)
        else:
            messagebox.showwarning("Ningún evento seleccionado", "Selecciona un evento para eliminarlo.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
