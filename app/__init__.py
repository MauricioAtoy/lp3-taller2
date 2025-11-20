"""
Paquete principal de la aplicación API de Películas.
Este módulo inicializa el paquete y expone los componentes principales.
"""

# TODO: Importar los componentes principales para facilitar su uso
# Ejemplo:
from .database import get_session, engine, DatabaseSession, check_database_connection
from .models import Usuario, Pelicula, Favorito
from .config import settings

__version__ = "1.0.0"
__author__ = "Tu Nombre"  # TODO: Reemplazar con tu nombre

# TODO: Opcional - Definir __all__ para controlar qué se exporta
__all__ = [
    "Usuario",
    "Pelicula",
    "Favorito",
    "crear_usuario",
    "obtener_pelicula",
]

