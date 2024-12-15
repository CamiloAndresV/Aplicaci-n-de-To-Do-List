# 📝 **Aplicación de To-Do List** 

## 📜 **Descripción**

¡Bienvenido a tu nueva **aplicación de lista de tareas**! Esta herramienta te permitirá gestionar tus tareas o recordatorios de forma fácil y eficiente. Puedes agregar nuevas tareas, eliminarlas, marcarlas como completadas y visualizar solo las pendientes. Todo se guarda en un archivo local para que puedas acceder a tus tareas incluso después de cerrar la aplicación.

---

## 🚀 **Características**

- **Interfaz gráfica intuitiva**:
  - Desarrollada con **Tkinter**  para una experiencia de usuario amigable y visualmente atractiva.
  
- **Gestión de tareas**:
  - **Agregar tareas**: Añade nuevas tareas con descripción y fecha de vencimiento opcional.
  - **Eliminar tareas**: Elimina tareas que ya no sean necesarias.
  - **Marcar como completadas**: Marca las tareas completadas para llevar un control claro.
  - **Mostrar tareas pendientes**: Visualiza solo las tareas que aún no se han completado.

- **Persistencia de datos**:
  - Las tareas se guardan automáticamente en un archivo local (elige entre `.txt`, `.json`, `.csv`, o **SQLite**).
  
- **Notificaciones y Recordatorios**:
  - Si una tarea tiene una fecha de vencimiento, recibirás un recordatorio vía **WhatsApp** o **correo electrónico**.

---

## 🛠️ **Tecnologías Utilizadas**

- **Lenguaje de programación**: Python
- **Interfaz Gráfica**: Tkinter (o PyQt)
- **Persistencia de Datos**: 
  - Archivos locales (JSON, CSV, SQLite)
- **Notificaciones**: 
  - **WhatsApp**: Usando la API de Twilio o herramientas similares.
  - **Correo electrónico**: Configuración con SMTP para el envío de correos.

---

## ⚡ **Funcionalidades**

### **Interfaz Gráfica**
- **Menú de tareas**:
  - **Agregar tarea**: Añadir tareas con descripción y fecha de vencimiento.
  - **Eliminar tarea**: Eliminar tareas que ya no son necesarias.
  - **Marcar como completada**: Indica qué tareas han sido completadas.
  - **Ver tareas pendientes**: Filtra y muestra solo las tareas no completadas.

- **Notificaciones de tareas**:
  - **WhatsApp**: Recibe recordatorios automáticos vía WhatsApp.
  - **Correo electrónico**: Recibe un correo electrónico recordatorio para tus tareas con fecha de vencimiento.

### **Persistencia de Datos**
- **Archivos locales**: Las tareas se guardan automáticamente en un archivo, y puedes elegir el formato que prefieras (JSON, CSV, SQLite, etc.).

- **Actualización automática**: El archivo de tareas se actualiza cada vez que agregas, eliminas o marcas tareas como completadas.

---

## 🧑‍💻 **Instalación**

### **Requisitos previos**

1. **Instalar Python 3.x**: Si aún no lo tienes, descarga e instala [Python 3.x](https://www.python.org/downloads/).
2. **Instalar dependencias**: Ejecuta el siguiente comando para instalar las bibliotecas necesarias:

   ```bash
   pip install tk pyqt5 twilio smtplib json sqlite3
   ```

### **Clonar el Repositorio**

Puedes clonar este repositorio para empezar a usar la aplicación:

```bash
git clone https://github.com/tu-usuario/Aplicacion-de-To-Do-List.git
```

### **Ejecutar la Aplicación**

Dentro de la carpeta del proyecto, ejecuta:

```bash
python main.py
```

---

## 🤝 **Contribuciones**

¡Las contribuciones son bienvenidas! Si encuentras algún error o deseas mejorar el proyecto, siéntete libre de abrir un *pull request* o crear un *issue*.

---

## 📜 **Licencia**

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

✨ **¡Gracias por usar nuestra aplicación!** ✨

---


