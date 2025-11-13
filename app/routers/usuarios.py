"""
Router de Usuarios.
Endpoints para gestionar usuarios en la plataforma.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models import Usuario, Favorito, Pelicula
from app.schemas import (
    UsuarioCreate,
    UsuarioRead,
    UsuarioUpdate,
    UsuarioWithFavoritos,
    PeliculaRead
)

# TODO: Crear el router con prefijo y tags
router = APIRouter(
    prefix="/api/usuarios",
    tags=["Usuarios"]
)


# TODO: Endpoint para listar todos los usuarios
@router.get("/", response_model=List[UsuarioRead])
def listar_usuarios(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
):
    """
    Lista todos los usuarios registrados.
    
    - **skip**: Número de registros a omitir (para paginación)
    - **limit**: Número máximo de registros a retornar
    """
    # TODO: Consultar todos los usuarios con paginación
    total = db.query(Usuario).count()
    pages = (total + size - 1) // size
    return PaginatedResponse(
        items=usuarios,
        total=total,
        page=page,
        size=size,
        pages=pages
    )
    return usuarios


# TODO: Endpoint para crear un nuevo usuario
@router.post("/", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
def crear_usuario(
    usuario: UsuarioCreate,
    session: Session = Depends(get_session)
):
    """
    Crea un nuevo usuario en la plataforma.
    
    - **nombre**: Nombre del usuario
    - **correo**: Correo electrónico único
    """
    # TODO: Verificar que el correo no exista
    statement = 
    existing_user = 
    
    # TODO: Crear el nuevo usuario
    db_usuario = Usuario.model_validate(usuario)
    
    return db_usuario


# TODO: Endpoint para obtener un usuario por ID
@router.get("/{usuario_id}", response_model=UsuarioRead)
def obtener_usuario(
    usuario_id: int,
    session: Session = Depends(get_session)
):
    """
    Obtiene un usuario específico por su ID.
    
    - **usuario_id**: ID del usuario
    """
    # TODO: Buscar el usuario por ID
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario


# TODO: Endpoint para actualizar un usuario
@router.put("/{usuario_id}", response_model=UsuarioRead)
def actualizar_usuario(
    usuario_id: int,
    usuario_update: UsuarioUpdate,
    session: Session = Depends(get_session)
):
    """
    Actualiza la información de un usuario existente.
    
    - **usuario_id**: ID del usuario a actualizar
    - **nombre**: Nuevo nombre (opcional)
    - **correo**: Nuevo correo (opcional)
    """
    # TODO: Buscar el usuario
    db_usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    
    # TODO: Si se actualiza el correo, verificar que no exista
        if usuario_update.correo:
        correo_existente = session.query(Usuario).filter(
            Usuario.correo == usuario_update.correo,
            Usuario.id != usuario_id
        ).first()
        if correo_existente:
            raise HTTPException(status_code=400, detail="Correo ya registrado por otro usuario")

    # TODO: Actualizar solo los campos proporcionados
    usuario_data =  usuario_update.dict(exclude_unset=True)
    
    return db_usuario


# TODO: Endpoint para eliminar un usuario
@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(
    usuario_id: int,
    session: Session = Depends(get_session)
):
    """
    Elimina un usuario de la plataforma.
    
    - **usuario_id**: ID del usuario a eliminar
    
    También se eliminarán todos los favoritos asociados al usuario.
    """
    # Buscar el usuario
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {usuario_id} no encontrado"
        )
    
    # Eliminar el usuario (los favoritos se eliminan por CASCADE)
    session.delete(usuario)
    session.commit()
    return None


# TODO: Endpoint para obtener los favoritos de un usuario
@router.get("/{usuario_id}/favoritos", response_model=List[PeliculaRead])
def listar_favoritos_usuario(
    usuario_id: int,
    session: Session = Depends(get_session)
):
    """
    Lista todas las películas favoritas de un usuario.
    
    - **usuario_id**: ID del usuario
    """
    # TODO: Verificar que el usuario existe
    usuario = 
    
    # TODO: Obtener las películas favoritas del usuario
    statement = 
    
    return peliculas


# TODO: Endpoint para marcar una película como favorita
@router.post(
    "/{usuario_id}/favoritos/{pelicula_id}",
    status_code=status.HTTP_201_CREATED
)
def marcar_favorito(
    usuario_id: int,
    pelicula_id: int,
    session: Session = Depends(get_session)
):
    """
    Marca una película como favorita para un usuario.
    
    - **usuario_id**: ID del usuario
    - **pelicula_id**: ID de la película
    """
    # Verificar que el usuario existe
    usuario = session.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con id {usuario_id} no encontrado"
        )
    
    # Verificar que la película existe
    pelicula = session.get(Pelicula, pelicula_id)
    if not pelicula:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Película con id {pelicula_id} no encontrada"
        )
   
    # Verificar si ya existe el favorito
    statement = select(Favorito).where(
        Favorito.id_usuario == usuario_id,
        Favorito.id_pelicula == pelicula_id
    )
    existing_favorito = session.exec(statement).first()
    if existing_favorito:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La película ya está marcada como favorita"
        )
    
    # TODO: Crear el favorito
    favorito = 
    
    return {"message": "Película marcada como favorita exitosamente"}


# TODO: Endpoint para eliminar una película de favoritos
@router.delete(
    "/{usuario_id}/favoritos/{pelicula_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_favorito(
    usuario_id: int,
    pelicula_id: int,
    session: Session = Depends(get_session)
):
    """
    Elimina una película de los favoritos de un usuario.
    
    - **usuario_id**: ID del usuario
    - **pelicula_id**: ID de la película
    """
    # TODO: Buscar el favorito
    statement = 

    favorito = 
    
    if not favorito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El favorito no existe"
        )
    
    # TODO: Eliminar el favorito
    
    return None


# TODO: Opcional - Endpoint para estadísticas del usuario
@router.get("/{usuario_id}/estadisticas")
def obtener_estadisticas_usuario(
    usuario_id: int,
    session: Session = Depends(get_session)
):
    """
    Obtiene estadísticas del usuario (películas favoritas, géneros preferidos, etc.)
    
    - **usuario_id**: ID del usuario
    """
    # TODO: Verificar que el usuario existe
    # TODO: Calcular número total de favoritos
    # TODO: Obtener géneros más favoritos
    # TODO: Calcular tiempo total de películas favoritas
    pass
