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
        "name": "Api Javier",
        "email": "tu.email@example.com",
    },
    license_info={
        "name": "MIT",
    },
)


# TODO: Configurar CORS para permitir solicitudes desde diferentes orígenes
# Esto es importante para desarrollo con frontend separado
# Configuración de CORS: tomamos orígenes desde `settings` si están definidos,
# soportamos una lista o un solo origen en string. Si se usa "*" y se permiten
# credenciales, eso no es compatible con el estándar CORS de navegadores, así
# que desactivamos allow_credentials en ese caso.
cors_origins = getattr(settings, "cors_origins", ["http://localhost:3000"])
if isinstance(cors_origins, str):
    cors_origins = [cors_origins]

# allow_credentials por defecto (puede ser override en settings)
allow_credentials = getattr(settings, "allow_credentials", True)
# Si el origen es un wildcard "*" no es seguro/usual permitir credentials
if "*" in cors_origins and allow_credentials:
    # Evitar enviar True junto con '*' (los navegadores lo bloquearán)
    allow_credentials = False

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=allow_credentials,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


# TODO: Incluir los routers de usuarios, peliculas y favoritos
from app.routers import usuarios, peliculas, favoritos

# Ejemplo:
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(peliculas.router, prefix="/api/peliculas", tags=["Películas"])
app.include_router(favoritos.router, prefix="/api/favoritos", tags=["Favoritos"])

# TODO: Crear un endpoint raíz que retorne información básica de la API
@app.get("/", tags=["Root"])
async def root():
    """
    Endpoint raíz de la API.
    Retorna información básica y enlaces a la documentación.
    """
    routes = {}
    for route in app.routes:
        if hasattr(route,"path") and hasattr(route, "methods"):
            routes[route.name]={
                "path":route.path,
                "methods":list(route.methods)
            }
    return {

        # TODO: Agregar información 
        "api_name": app.title,
        "version": app.version,
        "routes": routes,
        "description": "API para gestionar usuarios, películas y favoritos.",
        "endpoints": {
            "usuarios": "/api/usuarios",
            "peliculas": "/api/peliculas",
            "favoritos": "/api/favoritos"
        },
        "docs": "/docs",
        "redoc": "/redoc",
        "note": "Para más información, revisa la documentación en los enlaces proporcionados."
    }


# Crear un endpoint de health check para monitoreo
@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint para verificar el estado de la API.
    Útil para sistemas de monitoreo y orquestación.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

        # TODO: Agregar información sobre el sistema (uptime, memoria, etc.)
        uptime_seconds = int(time.time() - APP_START_TIME)

    system_info = {
        "uptime_seconds": uptime_seconds,
        "cpu_usage_percent": psutil.cpu_percent(),
        "memory_usage_percent": psutil.virtual_memory().percent,
    }
    return {
        "status": "healthy",
        # TODO: Agregar verificación de conexión a base de datos
        "status": "healthy" if db_status == "connected" else "degraded",
        "database": db_status,
        "system": system_info,
    }


# TODO: Opcional - Agregar middleware para logging de requests


# TODO: Opcional - Agregar manejadores de errores personalizados


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        # TODO: Configurar el servidor uvicorn con los parámetros apropiados
        "main:app",         
        host="0.0.0.0", 
        port=8000,
        reload=True,
        workers=1,
        log_level="info",
    )

