from pydantic import BaseModel

class RequestDecryptText(BaseModel):
    # user: str
    # office: str
    encryptText: str  # El texto encriptado a desencriptar
    # fileName: str
