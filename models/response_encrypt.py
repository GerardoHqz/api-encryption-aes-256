from pydantic import BaseModel

class ResponseEncrypt(BaseModel):
    status: str
    statusCode: int
    statusMessage: str
    encrypted_data: str  # Datos encriptados
