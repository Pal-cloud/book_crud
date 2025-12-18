# 📚 Book CRUD API

Una API REST completa para la gestión de libros construida con **FastAPI**, **SQLAlchemy** y **MySQL**.

## 🚀 Características

- ✅ **CRUD Completo**: Crear, Leer, Actualizar y Eliminar libros
- ✅ **API REST**: Endpoints bien estructurados siguiendo estándares REST
- ✅ **FastAPI**: Framework moderno y rápido con documentación automática
- ✅ **SQLAlchemy ORM**: Gestión de base de datos con ORM
- ✅ **MySQL**: Base de datos robusta y escalable
- ✅ **Validación de Datos**: Esquemas Pydantic para validación automática
- ✅ **Documentación Automática**: Swagger UI y ReDoc incluidos
- ✅ **Arquitectura Limpia**: Separación clara de responsabilidades

## 📁 Estructura del Proyecto

```
book_crud/
│
├── main.py                     # Punto de entrada de la aplicación
├── requirements.txt            # Dependencias del proyecto
├── .env                       # Variables de entorno (opcional)
├── db.sqlite3                 # Base de datos (se crea automáticamente)
│
├── config/                    # Configuración de la aplicación
│   ├── __init__.py
│   └── config_variables.py    # Variables de configuración y entorno
│
├── database/                  # Configuración de base de datos
│   ├── __init__.py
│   └── database.py           # Conexión y configuración SQLAlchemy
│
├── models/                   # Modelos de base de datos
│   ├── __init__.py
│   └── libro_model.py        # Modelo SQLAlchemy para libros
│
├── schemas/                  # Esquemas de validación
│   ├── __init__.py
│   └── libros_schema.py      # Esquemas Pydantic para libros
│
├── controllers/              # Lógica de negocio
│   ├── __init__.py
│   └── libro_controller.py   # Controlador CRUD para libros
│
└── routes/                   # Definición de rutas
    ├── __init__.py
    └── libro_routes.py       # Endpoints de la API
```

## 🛠️ Instalación y Configuración

### 1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd book_crud
```

### 2. **Crear entorno virtual**
```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/Mac
source .venv/bin/activate
```

### 3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 4. **Configurar variables de entorno** (Opcional)
Edita el archivo `.env`:
```env
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_NAME=book_crud_db
```

### 5. **Ejecutar la aplicación**
```bash
# Usando uvicorn directamente
uvicorn main:app --reload

# O usando Python
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📡 Endpoints de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Mensaje de bienvenida |
| `GET` | `/libros/` | Obtener todos los libros |
| `GET` | `/libros/{id}` | Obtener un libro por ID |
| `POST` | `/libros/` | Crear un nuevo libro |
| `PUT` | `/libros/{id}` | Actualizar un libro existente |
| `DELETE` | `/libros/{id}` | Eliminar un libro |

### Ejemplo de uso:

**Crear un libro:**
```bash
curl -X POST "http://localhost:8000/libros/" \\
-H "Content-Type: application/json" \\
-d '{
  "title": "Don Quijote de la Mancha",
  "description": "Una obra maestra de Miguel de Cervantes"
}'
```

**Obtener todos los libros:**
```bash
curl -X GET "http://localhost:8000/libros/"
```

## 🗄️ Modelo de Datos

### Libro
```python
{
  "id": 1,
  "title": "Don Quijote de la Mancha",
  "description": "Una obra maestra de Miguel de Cervantes"
}
```

## 📖 Documentación Interactiva

Una vez que la aplicación esté ejecutándose, puedes acceder a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🏗️ Arquitectura

El proyecto sigue una **arquitectura en capas** clara:

1. **Capa de Presentación** (`main.py`, `routes/`): Maneja las peticiones HTTP
2. **Capa de Lógica de Negocio** (`controllers/`): Implementa la lógica CRUD
3. **Capa de Acceso a Datos** (`models/`, `database/`): Interactúa con la base de datos
4. **Capa de Validación** (`schemas/`): Valida y serializa datos
5. **Capa de Configuración** (`config/`): Maneja configuración y variables de entorno

### Ventajas de esta arquitectura:
- ✅ **Separación de responsabilidades**
- ✅ **Fácil mantenimiento y testing**
- ✅ **Escalabilidad**
- ✅ **Código reutilizable**

## 🔧 Tecnologías Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno y rápido
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para Python
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validación de datos
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[MySQL](https://www.mysql.com/)** - Sistema de gestión de base de datos
- **[PyMySQL](https://pymysql.readthedocs.io/)** - Conector MySQL para Python
- **[python-dotenv](https://python-dotenv.readthedocs.io/)** - Carga variables de entorno

## 🚀 Próximos Pasos

- [ ] Implementar autenticación y autorización
- [ ] Añadir paginación avanzada
- [ ] Implementar filtros y búsqueda
- [ ] Añadir tests unitarios
- [ ] Dockerizar la aplicación
- [ ] Implementar cache con Redis
- [ ] Añadir logging estructurado

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

⭐ ¡No olvides darle una estrella al proyecto si te fue útil!