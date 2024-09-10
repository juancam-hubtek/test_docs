from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Modelo para los datos de entrada (request body)
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


# Modelo para los datos de salida (response)
class UserResponse(BaseModel):
    id: int
    username: str
    email: str


# Simulación de base de datos en memoria
fake_db = {
    1: {"id": 1, "username": "user1", "email": "user1@example.com"},
    2: {"id": 2, "username": "user2", "email": "user2@example.com"}
}


# 1. POST - Crear un usuario
@app.post("/user/", response_model=UserResponse, summary="Crear un usuario", description="Este endpoint crea un nuevo usuario en el sistema.", tags=["Users"])
async def create_user(user: User):
    """
    Crea un nuevo usuario con la información proporcionada en el cuerpo de la solicitud.

    - **username**: Nombre del usuario
    - **email**: Dirección de correo del usuario
    - **full_name**: Nombre completo del usuario (opcional)
    """
    new_id = max(fake_db.keys()) + 1
    new_user = {"id": new_id, "username": user.username, "email": user.email}
    fake_db[new_id] = new_user
    return new_user


# 2. GET - Obtener un usuario por ID
@app.get("/user/{user_id}", response_model=UserResponse, summary="Obtener un usuario", description="Obtiene los datos de un usuario específico por su ID.", tags=["Users"])
async def get_user(user_id: int):
    """
    Obtiene un usuario por su ID.

    - **user_id**: ID del usuario que deseas obtener.
    """
    user = fake_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


# 3. PUT - Actualizar un usuario por ID
@app.put("/user/{user_id}", response_model=UserResponse, summary="Actualizar un usuario", description="Actualiza los datos de un usuario existente.", tags=["Users"])
async def update_user(user_id: int, user: User):
    """
    Actualiza los datos de un usuario existente.

    - **user_id**: ID del usuario que deseas actualizar.
    - **username**: Nuevo nombre del usuario.
    - **email**: Nueva dirección de correo.
    - **full_name**: Nuevo nombre completo (opcional).
    """
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    updated_user = {"id": user_id, "username": user.username, "email": user.email}
    fake_db[user_id] = updated_user
    return updated_user


# 4. DELETE - Eliminar un usuario por ID
@app.delete("/user/{user_id}", summary="Eliminar un usuario", description="Elimina un usuario del sistema.", tags=["Users"])
async def delete_user(user_id: int):
    """
    Elimina un usuario por su ID.

    - **user_id**: ID del usuario que deseas eliminar.
    """
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    del fake_db[user_id]
    return {"detail": "Usuario eliminado correctamente"}