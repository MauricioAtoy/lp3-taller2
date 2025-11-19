from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.database import create_db_and_tables
from app.routers import usuarios, peliculas, favoritos

# TODO: Importar la configuración desde app.config

from app.config import settings
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestor de ciclo de vida de la aplicación.
    Se ejecuta al iniciar y al cerrar la aplicación.
    """
    # Startup: Crear tablas en la base de datos
    create_db_and_tables()
    yield
    
    # Shutdown: Limpiar recursos si es necesario
    print("cerrando aplicación...")


# TODO: Crear la instancia de FastAPI con metadatos apropiados
# Incluir: title, description, version, contact, license_info
app = FastAPI(
    title="API de Películas",
    description="API RESTful para gestionar usuarios, películas y favoritos",
    version="1.0.0",
    lifespan=lifespan,
    # TODO: Agregar información de contacto y licencia
    contact={
        "name": "Tu Nombre",
        "email": "tu.email@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


# TODO: Configurar CORS para permitir solicitudes desde diferentes orígenes
# Esto es importante para desarrollo con frontend separado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: En producción, especificar orígenes permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Métodos permitidos
    allow_headers=["Authorization", "Content-Type"],
)


# TODO: Incluir los routers de usuarios, peliculas y favoritos
# Ejemplo:
# app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])


# TODO: Crear un endpoint raíz que retorne información básica de la API
@app.get("/", tags=["Root"])
async def root():
    """
    Endpoint raíz de la API.
    Retorna información básica y enlaces a la documentación.
    """
    return {
        # TODO: Agregar información 
    }


# Crear un endpoint de health check para monitoreo
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint para verificar el estado de la API.
    Útil para sistemas de monitoreo y orquestación.
    """
    return {
        "status": "healthy",
        # TODO: Agregar verificación de conexión a base de datos
        # TODO: Agregar información sobre el sistema (uptime, memoria, etc.)
    }


# TODO: Opcional - Agregar middleware para logging de requests


# TODO: Opcional - Agregar manejadores de errores personalizados


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        # TODO: Configurar el servidor uvicorn con los parámetros apropiados
    )

