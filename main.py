from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Url: https://fastapi-production-6358.up.railway.app/
# Cuando se crea un proyecto en Railway, se crea un entorno virtual por defecto
# Pero al clonar el proyecto, no se incluye el entorno virtual
# Por lo que es necesario crearlo manualmente si lo clonas de GitHub por ejemplo
# Ingresas al terminal y el siguiente es el comando para crear el entorno virtual: python -m venv venv (venv es el nombre del entorno virtual y esta incluido en .gitignore)
# Luego, para activar el entorno virtual: venv\Scripts\activate
# Para instalar las dependencias: pip install fastapi uvicorn pydantic
# Para ejecutar el proyecto y habilitar un servidor local: uvicorn main:app --reload

# Crear una instancia de la clase FastAPI
app = FastAPI()

# Crear una clase para el modelo de datos
class Msg(BaseModel):
    msg: str
    
class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str] = None
    precio: Optional[float] = None
    isbn: Optional[str] = None

# Crear una ruta raíz (Cuando alguien ingrese a la url principal, se ejecutará la función root)
@app.get("/")
async def root():
    return {"message": "Hola Mundo. Bienvenido a FastAPI!"}

# Crear una ruta con parámetros (Cuando alguien ingrese a la url /path, se ejecutará la función demo_get)
@app.get("/path")
async def demo_get():
    return {"mensaje": "Esta es la ruta /path, usa un post request para transformar el texto a mayúsculas"}    

# Crear una ruta con parámetros (Cuando alguien ingrese a la url /path, se ejecutará la función demo_post)
@app.post("/path")
async def demo_post(inp: Msg):
    return {"mensaje": inp.msg.upper()}

# Crear una ruta con parámetros (Cuando alguien ingrese a la url /path, se ejecutará la función demo_get_path_id)
@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"mensaje": f"Esta es la ruta /path/{path_id}, usa un post request para retornar el resultado"}    

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"dato": f"Este es el libro con id {id}"}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"mensaje": f"Se ha insertado el libro {libro.titulo} de {libro.autor}"}