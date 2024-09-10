from fastapi import FastAPI
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


@app.post("/user/", response_model=UserResponse, summary="Crear un usuarioaaaaa", description="Este endpoint crea un nuevo usuario en el sistema.", tags=["Users"])
async def create_user(user: User):
    """
    Crea un nuevo usuario con la información proporcionada en el cuerpo de la solicitud.

    - **username**: Nombre del usuario
    - **email**: Dirección de correo del usuario
    - **full_name**: Nombre completo del usuario (opcional)
    """
    return {
        "id": 1,
        "usernameeeeeeeee": user.username,
        "emaillllllllllll": user.email,
    }