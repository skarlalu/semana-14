Sistema de Restaurante - Componentes y Contenedores (Semana 14)
Estudiante: Karla Faniela Luque Navarrete

El objetivo principal es ofrecer una experiencia más clara y amigable para el usuario, incorporando formularios, tablas, pestañas y botones de acción, manteniendo estrictamente la arquitectura modular, la persistencia en archivos JSON y la separación de responsabilidades.

2. Estructura del Proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── init.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── init.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── init.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md

3. Componentes y Contenedores Utilizados
Contenedores (Frame y LabelFrame): Utilizados para agrupar y organizar visualmente las zonas de navegación, los formularios de captura de datos y las áreas de visualización.

Pestañas (ttk.Notebook): Organizan las distintas secciones funcionales del sistema (Gestión de Productos y Consulta de Usuarios) dentro de la interfaz principal.

Tablas (ttk.Treeview): Componentes tabulares interactivos para mostrar en tiempo real la información de productos y usuarios.

Entradas y Etiquetas (tk.Entry y tk.Label): Componentes organizados mediante el gestor de geometría grid para la captura de datos de productos.

Botones de Acción (tk.Button): Configurados mediante el parámetro command= para activar las operaciones CRUD de manera desacoplada.

4. Mejoras Realizadas en la Interfaz
Se implementó una pantalla de inicio de sesión (LoginView) que valida las credenciales a través del servicio antes de dar acceso al sistema.

Se estructuró la interfaz principal (MainView) dividiendo claramente el panel superior, la sección de formularios y la tabla de registros.

Se actualizó la información mostrada de manera automática tras cada operación realizada por el usuario.

5. Operaciones Implementadas sobre Productos
Registrar: Permite dar de alta un nuevo producto validando códigos únicos.

Cargar / Consultar: Permite buscar un producto por su código para rellenar el formulario.

Actualizar: Modifica los datos de un producto existente y actualiza la persistencia.

Eliminar: Remueve el producto seleccionado del sistema y refresca la interfaz.

Nota: Todas las validaciones y operaciones de negocio se ejecutan dentro de RestauranteServicio, evitando manipular directamente los archivos JSON desde las vistas.

6. Persistencia Utilizada
La persistencia de los datos se mantiene mediante los archivos productos.json y usuarios.json ubicados en la carpeta datos/, gestionados de forma segura a través de ArchivoServicio.

