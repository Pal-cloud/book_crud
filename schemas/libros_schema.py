from pydantic import BaseModel

# Hereda todo de LibroBase.
# Se usa cuando el usuario envía datos para crear un libro.
# "pass" significa que no añadimos nada nuevo, solo usamos lo que está en LibroBase.

class LibroBase(BaseModel):
    title: str
    description: str = None

class LibroCreate(LibroBase):
    pass

class Libro(LibroBase): # Hereda de LibroBase (title y description) y añade el id que ya existe en la base de datos.
    id: int

    class Config:
        orm_mode = True # permite que Pydantic lea directamente objetos de SQLAlchemy como si fueran diccionarios, para enviarlos en respuestas JSON.rt BaseModel

# Hereda todo de ItemBase.
# Se usa cuando el usuario envía datos para crear un item.
# “pass” significa que no añadimos nada nuevo, solo usamos lo que está en ItemBase.

class ItemBase(BaseModel):
    title: str
    description: str = None

class LibroCreate(LibroBase):
    pass

class Libro(LibroBase): # Hereda de ItemBase (title y description) y añade el id que ya existe en la base de datos.
    id: int

    class Config:
        orm_mode = True # permite que Pydantic lea directamente objetos de SQLAlchemy como si fueran diccionarios, para enviarlos en respuestas JSON.