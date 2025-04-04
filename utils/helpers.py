from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import base64
from models.request_encrypt import RequestEncryptText
from models.request_decrypt import RequestDecryptText
from models.response_encrypt import ResponseEncrypt
from models.response_decrypt import ResponseDecrypt
from utils.params import KEY, IV

def encrypt_data(request: RequestEncryptText) -> ResponseEncrypt:
    # Crear el objeto Cipher con AES y CBC utilizando un IV fijo
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()

    # El dato a encriptar
    data_to_encrypt = request.data.encode('utf-8')

    # Añadir padding PKCS7 para que los datos sean múltiplos de 16 bytes
    padder = padding.PKCS7(algorithms.AES.block_size).padder()  # AES block size is 128 bits (16 bytes)
    padded_data = padder.update(data_to_encrypt) + padder.finalize()

    # Encriptar los datos con el IV fijo
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Codificar los datos encriptados en base64 para su envío o almacenamiento
    encrypted_data_b64 = base64.b64encode(encrypted_data).decode('utf-8')

    return ResponseEncrypt(
        status="success",
        statusCode=1,
        statusMessage="Datos encriptados correctamente",
        encrypted_data=encrypted_data_b64,
    )


def decrypt_data(request: RequestDecryptText) -> ResponseDecrypt:
    # Usamos el IV fijo para la desencriptación, el mismo IV usado para encriptar
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    decryptor = cipher.decryptor()

    # Desencriptar el dato
    encrypted_data = base64.b64decode(request.encryptText)  # Decodificar los datos en base64
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Eliminar el padding de los datos desencriptados
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Convertir los datos desencriptados a una cadena
    decrypted_data_str = unpadded_data.decode('utf-8')

    return ResponseDecrypt(
        status="success",
        statusCode=1,
        statusMessage="Datos desencriptados correctamente",
        decrypted_data=decrypted_data_str
    )
