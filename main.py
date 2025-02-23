from fastapi import FastAPI
from pydantic import BaseModel
import re
import random 

app = FastAPI()

# Expreciones regulares 
numero_regex = r"\d"  
caracter_especial_regex = r"[!@#$%^&*(),.?\":{}|<>]" 

class Passwordverify(BaseModel):
    password: str

class Createpassword(BaseModel):
    longitud: int

@app.post("/verify/password")
async def veryfi_password(password_data: Passwordverify):
    password = password_data.password
    if (
        len(password) >= 8
        and any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and re.search(numero_regex, password)
        and re.search(caracter_especial_regex, password)
    ):
        return {"message": "La contraseña es segura"}

    return {"message": "La contraseña no es segura"}

@app.post("/create/password")
async def create_password(creta_password_data: Createpassword):
    password_long = creta_password_data.longitud
    lista = list()
    letras_minusculas = list("abcdefghijklmnopqrstuvwxyz")
    letras_mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numeros = list("0123456789")
    caracteres_especiales = list("!@#$%^&*()-_=+[]{}|;:',.<>?/")
    opciones = letras_minusculas + letras_mayusculas + numeros + caracteres_especiales

    if password_long < 8:
        return {"message" : "Esta longitud no es segura minimo 8"}
    
    while len(lista) < password_long:
        lista.append(random.choice(opciones))
        
    return "".join(lista)
    
    

    





