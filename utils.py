"""
Módulo de utilidades para la aplicación.
Contiene funciones auxiliares utilizadas en diferentes partes de la aplicación.
"""
import re
from datetime import datetime

def validar_correo(correo):
    """
    Valida que un correo electrónico tenga un formato válido.
    
    Args:
        correo (str): Correo electrónico a validar
        
    Returns:
        bool: True si el correo es válido, False en caso contrario
    """
    # TODO: crear la expresión regular para validar el correo
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    return bool(re.match(patron, correo))

def formatear_duracion(minutos):
    """
    Convierte una duración en minutos a formato hh:mm
    
    Args:
        minutos (int): Duración en minutos
        
    Returns:
        str: Duración formateada como hh:mm
    """
    # TODO: pendiente de implementar
    horas = minutos // 60
    mins = minutos % 60
    return f"{horas:02d}:{mins:02d}"
    pass 

def generar_slug(texto):
    """
    Genera un slug a partir de un texto.
    Un slug es una versión de texto amigable para URLs.
    
    Args:
        texto (str): Texto a convertir en slug
        
    Returns:
        str: Slug generado
    """
    # TODO: Convertir a minúsculas
    
    slug = texto.lower()
        
    # TODO: Reemplazar espacios con guiones
    slug = re.sub(r' '+;'-',slug)
    # TODO: Eliminar caracteres no alfanuméricos (excepto guiones)
    slug= re.sub(r'[^a-z0-9-]', '', slug)
    # TODO: Reemplazar múltiples guiones con uno solo
    slug = re.sub(r'-{2,}', '-', slug)

    # TODO: Eliminar guiones al inicio y final
    slug = slug.strip('-')

    return slug

def obtener_año_actual():
    """
    Obtiene el año actual.
    
    Returns:
        int: Año actual
    """
    # TODO: pendiente por implementar
    return datetime.now().year


def validar_año(año):
    """
    Valida que un año sea válido (no futuro y no muy antiguo).
    
    Args:
        año (int): Año a validar
        
    Returns:
        bool: True si el año es válido, False en caso contrario
    """
    año_actual = obtener_año_actual()
    return 1900 <= año <= año_actual

