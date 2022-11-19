from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista=[]

#Objeto persona
class Personas(BaseModel):
    nombre:str
    apellidos:str
    edad:int

@app.get("/select") 
def mostrar():
    return lista

@app.post("/insert")
def guardar(datos:Personas):
    lista.append(datos)
    return{"Mensaje":"Registro almacenado"}

@app.put("/update")
def guardar(datos:Personas):
    for item in lista:
        for key in lista[item]:
            if lista[item][key] == datos.nombre:
                lista[item]=datos

    return{"Mensaje":"Registro actualizado"}
