from sqlalchemy.orm import Session
from schemas import libros_schema
from models.libro_model import Libro

class LibroController:
    """
    Si no usaramos @static methos tendriamos que escribir:

    def __init__(self, db: Session): # El trabajador ya tiene su caja de herramientas (self.db) y no necesita traer nada externo cada vez.
            self.db = db

    y el controlador se vería así:

     def create_item(self, item: crud_schema.ItemCreate): # No hace falta pasar db:session cada vez
            db_item = Item(**item.dict())
            self.db.add(db_item)
            self.db.commit()
            self.db.refresh(db_item)
            return db_item
    """

    @staticmethod
    async def get_libros(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Libro).offset(skip).limit(limit).all()

    @staticmethod # Cada función es como un trabajador independiente que llega con su propio conjunto de herramientas (db) y hace su tarea.
    async def get_libro(db: Session, libro_id: int):
        return db.query(Libro).filter(Libro.id == libro_id).first()

    @staticmethod
    async def create_libro(db: Session, libro: libros_schema.LibroCreate):
        db_libro = Libro(**libro.dict())
        db.add(db_libro)
        db.commit()
        db.refresh(db_libro)
        return db_libro

    @staticmethod
    async def update_libro(db: Session, libro_id: int, libro: libros_schema.LibroCreate):
        db_libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if db_libro:
            db_libro.title = libro.title
            db_libro.description = libro.description
            db.commit()
            db.refresh(db_libro)
        return db_libro
    
    @staticmethod
    async def delete_libro(db: Session, libro_id: int):
        db_libro = db.query(Libro).filter(Libro.id == libro_id).first()
        if db_libro:
            db.delete(db_libro)
            db.commit()
        return db_libro