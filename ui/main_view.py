import tkinter as tk
from tkinter import messagebox, ttk

class MainView(tk.Frame):
    def __init__(self, parent, controlador, servicio):
        super().__init__(parent, bg="#f5f6fa")
        self.controlador = controlador
        self.servicio = servicio

        # Contenedor superior (Título y Cerrar sesión)
        top_frame = tk.Frame(self, bg="#2c3e50", height=50)
        top_frame.pack(side="top", fill="x")

        tk.Label(top_frame, text="Sistema de Gestión - Restaurante App", fg="white", bg="#2c3e50", font=("Arial", 14, "bold")).pack(side="left", padx=15, pady=10)
        tk.Button(top_frame, text="Cerrar Sesión", bg="#e74c3c", fg="white", command=self.controlador.cerrar_sesion).pack(side="right", padx=15, pady=10)

        # Contenedor principal dividido en Pestañas (Notebook) para separar vistas de Usuarios y Productos
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Gestión de Productos
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Gestión de Productos")
        self.crear_seccion_productos()

        # Pestaña 2: Consulta de Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Consulta de Usuarios")
        self.crear_seccion_usuarios()

    def crear_seccion_productos(self):
        # Marco izquierdo para el Formulario
        frame_form = tk.LabelFrame(self.tab_productos, text=" Formulario de Producto ", font=("Arial", 11, "bold"), padx=15, pady=15)
        frame_form.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky="w", pady=5)
        self.txt_codigo = tk.Entry(frame_form, width=20)
        self.txt_codigo.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nombre = tk.Entry(frame_form, width=20)
        self.txt_nombre.grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Categoría:").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_categoria = tk.Entry(frame_form, width=20)
        self.txt_categoria.grid(row=2, column=1, pady=5)

        tk.Label(frame_form, text="Precio:").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_precio = tk.Entry(frame_form, width=20)
        self.txt_precio.grid(row=3, column=1, pady=5)

        tk.Label(frame_form, text="Stock:").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_stock = tk.Entry(frame_form, width=20)
        self.txt_stock.grid(row=4, column=1, pady=5)

        # Botones de Acción (Registrar, Cargar/Consultar, Actualizar, Eliminar)
        frame_botones = tk.Frame(frame_form)
        frame_botones.grid(row=5, column=0, columnspan=2, pady=15)

        tk.Button(frame_botones, text="Registrar", bg="#2ecc71", fg="white", width=10, command=self.registrar).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_botones, text="Consultar", bg="#3498db", fg="white", width=10, command=self.consultar).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_botones, text="Actualizar", bg="#f39c12", fg="white", width=10, command=self.actualizar).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame_botones, text="Eliminar", bg="#e74c3c", fg="white", width=10, command=self.eliminar).grid(row=1, column=1, padx=5, pady=5)

        # Marco derecho para la tabla / visualización de productos
        frame_tabla = tk.LabelFrame(self.tab_productos, text=" Listado de Productos Registrados ", font=("Arial", 11, "bold"), padx=10, pady=10)
        frame_tabla.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        columns = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings", height=12)
        
        for col in columns:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, width=90)

        self.tabla.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        scrollbar.pack(side="right", fill="y")
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for p in self.servicio.productos:
            self.tabla.insert("", "end", values=(p.codigo, p.nombre, p.categoria, f"${p.precio:.2f}", p.stock))

    def registrar(self):
        try:
            self.servicio.registrar_producto(
                self.txt_codigo.get(),
                self.txt_nombre.get(),
                self.txt_categoria.get(),
                self.txt_precio.get(),
                self.txt_stock.get()
            )
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.limpiar_formulario()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def consultar(self):
        codigo = self.txt_codigo.get()
        p = self.servicio.buscar_producto(codigo)
        if p:
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, p.nombre)
            self.txt_categoria.delete(0, tk.END)
            self.txt_categoria.insert(0, p.categoria)
            self.txt_precio.delete(0, tk.END)
            self.txt_precio.insert(0, str(p.precio))
            self.txt_stock.delete(0, tk.END)
            self.txt_stock.insert(0, str(p.stock))
        else:
            messagebox.showwarning("No encontrado", "No existe un producto con ese código.")

    def actualizar(self):
        try:
            self.servicio.actualizar_producto(
                self.txt_codigo.get(),
                self.txt_nombre.get(),
                self.txt_categoria.get(),
                self.txt_precio.get(),
                self.txt_stock.get()
            )
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        try:
            self.servicio.eliminar_producto(self.txt_codigo.get())
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.limpiar_formulario()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_formulario(self):
        self.txt_codigo.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_categoria.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_stock.delete(0, tk.END)

    def crear_seccion_usuarios(self):
        frame_u = tk.Frame(self.tab_usuarios, padx=20, pady=20)
        frame_u.pack(fill="both", expand=True)

        tk.Label(frame_u, text="Usuarios Registrados en el Sistema", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        columns = ("id", "nombre", "correo")
        tabla_u = ttk.Treeview(frame_u, columns=columns, show="headings", height=10)
        for col in columns:
            tabla_u.heading(col, text=col.capitalize())
            tabla_u.column(col, width=150)
        tabla_u.pack(fill="both", expand=True, pady=5)

        for u in self.servicio.usuarios:
            tabla_u.insert("", "end", values=(u.identificacion, u.nombre, u.correo))