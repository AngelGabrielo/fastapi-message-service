# FastAPI Message Service 🚀

Este proyecto es una API RESTful desarrollada con **FastAPI** que implementa un sistema de gestión de mensajes. Destaca por utilizar una **Arquitectura en Capas** (Layered Architecture) para desacoplar la lógica de negocio, el acceso a datos y la capa de presentación.

## 🛠️ Tecnologías

* **Python 3.10+**
* **FastAPI** (Framework web)
* **SQLAlchemy** (ORM)
* **Pydantic** (Validación de datos)
* **MySQL** (Base de datos)
* **Uvicorn** (Servidor ASGI)

## 🏗️ Arquitectura y Patrones

El proyecto no utiliza la estructura plana por defecto, sino que implementa patrones de diseño robustos:

* **Repository Pattern:** Abstracción de la capa de datos (`SqlAlchemyMessageRepository`).
* **Service Layer:** Lógica de negocio pura (`SqlAlchemyMessageService`).
* **Dependency Injection:** Uso de `Depends` de FastAPI para inyectar repositorios y servicios.
* **DTOs vs Entities:** Separación entre modelos de Pydantic (API) y modelos de SQLAlchemy (BD).

## 🚀 Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/AngelGabrielo/fastapi-message-service.git
    cd fastapi-message-service
    ```

2.  **Crear entorno virtual e instalar dependencias:**
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Linux/Mac
    source .venv/bin/activate

    pip install -r requirements.txt
    ```

3.  **Configuración de Base de Datos:**
    Asegúrate de tener MySQL corriendo y actualiza la `DATABASE_URL` en `config/db.py` (o usa variables de entorno).

4.  **Ejecutar el servidor:**
    ```bash
    uvicorn course.angel.fastapi.webapi.services.main:app --reload
    ```

## 🔗 Endpoints Principales

* `GET /messages/`: Listar todos los mensajes.
* `POST /messages/`: Crear un nuevo mensaje (con validaciones).
* `GET /messages/{id}`: Obtener detalle.
* `PUT /messages/{id}`: Actualizar mensaje.
* `DELETE /messages/{id}`: Eliminar mensaje.