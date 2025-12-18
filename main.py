# IMPORTANTE: Aquí referenciamos el archivo "database"no la variable  "db"
from fastapi import FastAPI
from database import database

# Crear la instancia de FastAPI
app = FastAPI(title="Book CRUD API", description="API para gestión de libros", version="1.0.0")

@app.get("/")  # Ruta raíz
async def root():
    return {"message": "Welcome to the Book CRUD API!"}  # Mensaje de bienvenida

def run():
    pass

if __name__ == "__main__":
    # Crear las tablas en la base de datos
    database.Base.metadata.create_all(database.engine)
    run()