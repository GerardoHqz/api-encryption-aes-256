from pydantic import BaseModel

class ResponseDecrypt(BaseModel):
    status: str
    statusCode: int
    statusMessage: str
    decrypted_data: str  # Datos desencriptados
