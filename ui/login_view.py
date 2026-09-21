import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, controlador, servicio):
        super().__init__(parent, bg="#f0f2f5")
        self.controlador = controlador
        self.servicio = servicio

        # Contenedor central para el formulario de login
        frame_login = tk.Frame(self, bg="white", padx=30, pady=30, relief="raised", bd=1)
        frame_login.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame_login, text="Restaurante App - Login", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        tk.Label(frame_login, text="Usuario / Correo:", bg="white", anchor="w").pack(fill="x")
        self.entry_usuario = tk.Entry(frame_login, font=("Arial", 12), width=25)
        self.entry_usuario.pack(pady=5)

        tk.Label(frame_login, text="Contraseña:", bg="white", anchor="w").pack(fill="x")
        self.entry_clave = tk.Entry(frame_login, show="*", font=("Arial", 12), width=25)
        self.entry_clave.pack(pady=5)

        btn_ingresar = tk.Button(frame_login, text="Ingresar", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=self.verificar_login)
        btn_ingresar.pack(pady=15, fill="x")

    def verificar_login(self):
        correo = self.entry_usuario.get()
        clave = self.entry_clave.get()

        if self.servicio.validar_login(correo, clave):
            self.controlador.mostrar_main_view()
        else:
            messagebox.showerror("Error de acceso", "Credenciales incorrectas. Verifique sus datos.")