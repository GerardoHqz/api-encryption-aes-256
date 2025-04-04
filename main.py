from fastapi import FastAPI, HTTPException
from models.request_encrypt import RequestEncryptText
from models.request_decrypt import RequestDecryptText
from models.response_encrypt import ResponseEncrypt
from models.response_decrypt import ResponseDecrypt
from utils.helpers import encrypt_data, decrypt_data

app = FastAPI(
    title="ENCRIPTACION AES IGS - COMEDICA",
    description="Servicio para desencriptar archivos proporcioando por IGS"
                "con metodo de encriptacion para responder por medio de un archivo a IGS",
    version="1.0.0"
)

@app.post("/aes-encrypt", response_model=ResponseEncrypt)
async def aes_encrypt(request: RequestEncryptText):
    try:
        encrypted_data = encrypt_data(request)
        return encrypted_data
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error en la petición: {err}")

@app.post("/aes-decrypt", response_model=ResponseDecrypt)
async def aes_decrypt(request: RequestDecryptText):
    try:
        decrypted_data = decrypt_data(request)
        return decrypted_data
    except Exception as err:
        raise HTTPException(status_code=400, detail=f"Error en la petición: {err}")
