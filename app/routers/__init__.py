"""
Paquete de routers de la API.
Contiene los endpoints organizados por recurso.
"""

# TODO: Importar los routers para facilitar su uso en main.py
from .usuarios import router as usuarios_router
from .peliculas import router as peliculas_router
from .favoritos import router as favoritos_router

# TODO: Opcional - Definir __all__ para controlar las exportaciones
__all__ = [
    "Usuario",
    "Pelicula",
    "Favorito",
    "crear_usuario",
    "obtener_pelicula",
]

