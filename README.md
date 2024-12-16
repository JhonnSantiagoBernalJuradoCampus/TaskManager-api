# Task Manager API

Esta es una API para gestionar tareas utilizando FastAPI y SQLAlchemy.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/JhonnSantiagoBernalJuradoCampus/TaskManager-api.git
    cd TaskManager-api
    ```

2. Instala las dependencias:
    ```sh
    pip install fastapi-cors fastapi uvicorn sqlalchemy pydantic
    ```

3. Ejecuta la aplicación:
    ```sh
    python -m uvicorn main:app --reload
    ```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### Listar Tareas

- **URL:** `/tasks/`
- **Método:** `GET`
- **Respuesta:** Lista de tareas
    ```json
    [
        {
            "id": 1,
            "title": "Crear repo",
            "description": "Se requiere crear un repositorio en github para gestionar las versiones del proyecto de task manager",
            "completed": false
        },
        ...
    ]
    ```

### Crear Tarea

- **URL:** `/tasks/`
- **Método:** `POST`
- **Cuerpo de la solicitud:**
    ```json
    {
        "title": "Nueva tarea",
        "description": "Descripción de la nueva tarea"
    }
    ```
- **Respuesta:** Tarea creada
    ```json
    {
        "id": 2,
        "title": "Nueva tarea",
        "description": "Descripción de la nueva tarea",
        "completed": false
    }
    ```

### Actualizar Tarea

- **URL:** `/tasks/{task_id}`
- **Método:** `PUT`
- **Parámetros de la URL:** [task_id](http://_vscodecontentref_/0) (ID de la tarea a actualizar)
- **Cuerpo de la solicitud:**
    ```json
    {
        "completed": true
    }
    ```
- **Respuesta:** Tarea actualizada
    ```json
    {
        "id": 1,
        "title": "Crear repo",
        "description": "Se requiere crear un repositorio en github para gestionar las versiones del proyecto de task manager",
        "completed": true
    }
    ```

### Eliminar Tareas Completadas

- **URL:** `/tasks/completed/`
- **Método:** `DELETE`
- **Respuesta:** Mensaje de confirmación
    ```json
    {
        "message": "Completed tasks have been deleted"
    }
    ```

### Exportar Tareas

- **URL:** `/tasks/export/`
- **Método:** `GET`
- **Respuesta:** Archivo JSON codificado en Base64
    ```json
    {
        "filename": "tasks_export.json",
        "filedata": "<BASE64_ENCODED_JSON>",
        "message": "Tasks exported successfully as Base64"
    }
    ```

## Estructura del Proyecto

- [crud.py](http://_vscodecontentref_/1): Funciones CRUD para gestionar las tareas.
- [database.py](http://_vscodecontentref_/2): Configuración de la base de datos.
- [models.py](http://_vscodecontentref_/3): Definición del modelo de datos.
- [schemas.py](http://_vscodecontentref_/4): Esquemas Pydantic para validación de datos.
- [main.py](http://_vscodecontentref_/5): Definición de los endpoints y configuración de la aplicación FastAPI.

## Notas

- Asegúrate de tener SQLite instalado o cambia la configuración de la base de datos en [database.py](http://_vscodecontentref_/6) si deseas usar otro motor de base de datos.
- Puedes modificar los permisos de CORS en [main.py](http://_vscodecontentref_/7) según tus necesidades.

¡Listo! Ahora puedes empezar a usar la API para gestionar tus tareas.