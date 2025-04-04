from pydantic import BaseModel
from typing import List, Union

class RequestEncryptText(BaseModel):
    # user: str
    # office: str
    # pid: str
    data: str  # Datos a encriptar
