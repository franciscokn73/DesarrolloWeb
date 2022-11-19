import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
datos_diccio = []

# Objeto persona
class usuario(BaseModel):
    id:str
    usuario:str
    clave:str

@app.get("/select")
def mostrar():
    readDatosDiccio()
    return datos_diccio

@app.post("/insert") 
async def guardar(datos:usuario):
    readDatosDiccio()
    encode_datos = jsonable_encoder(datos)
    datos_diccio.append(encode_datos)
    writeDatosDiccio()
    return {"Mensaje":"Registro almacenado"}

@app.put("/update") 
def actualizar(datos:usuario):
    print(datos)
    readDatosDiccio()
    estado = False
    id = 0
    for item in datos_diccio:
        if item["id"] == datos.id:
            datos_diccio[id]["usuario"] = datos.usuario
            datos_diccio[id]["clave"] = datos.clave
            writeDatosDiccio()
            estado = True
            break 
        id += 1

    if estado == True:
        return {"Mensaje": "Registro actualizado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

@app.delete("/delete")
def eliminar(datos:usuario):
    print(datos)
    readDatosDiccio()
    id = 0
    estado = False
    for item in datos_diccio:
        if item["id"] == datos.id:
            datos_diccio.pop(id)
            estado = True
            writeDatosDiccio()
            break
        id += 1
    if estado==True:
        return {"Mensaje": "Registro eliminado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

# abro archivo json y convierto en dicionario
def readDatosDiccio():
    fichero = open("usuario.json", "r")
    global datos_diccio
    datos_diccio = json.loads(fichero.read())
    fichero.close()

def writeDatosDiccio():
    fichero = open("usuario.json", "w")
    #convierto diccionario a archivo Json con identacion
    forWrite = json.dumps(datos_diccio, indent=2)
    fichero.write(forWrite)
    fichero.close()
# cambios a fichero VS