import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
datos_diccio = []

# Objeto persona
class transportador(BaseModel):
    nit:str
    nombre:str
    direccion:str
    correo:str
    telefono:str

@app.get("/select/transportador")
def mostrar():
    readDatosDiccio()
    return datos_diccio

@app.post("/insert/transportador") 
async def guardar(datos:transportador):
    readDatosDiccio()
    encode_datos = jsonable_encoder(datos)
    datos_diccio.append(encode_datos)
    writeDatosDiccio()
    return {"Mensaje":"Registro almacenado"}

@app.put("/update/transportador") 
def actualizar(datos:transportador):
    print(datos)
    readDatosDiccio()
    estado = False
    id = 0
    for item in datos_diccio:
        if item["nit"] == datos.nit:
            datos_diccio[id]["nombre"] = datos.nombre
            datos_diccio[id]["direccion"] = datos.direccion
            datos_diccio[id]["correo"] = datos.correo
            datos_diccio[id]["telefono"] = datos.telefono
            writeDatosDiccio()
            estado = True
            break 
        id += 1

    if estado == True:
        return {"Mensaje": "Registro actualizado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

@app.delete("/delete/transportador")
def eliminar(datos:transportador):
    print(datos)
    readDatosDiccio()
    id = 0
    estado = False
    for item in datos_diccio:
        if item["nit"] == datos.nit:
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
    fichero = open("transportador.json", "r")
    global datos_diccio
    datos_diccio = json.loads(fichero.read())
    fichero.close()

def writeDatosDiccio():
    fichero = open("transportador.json", "w")
    #convierto diccionario a archivo Json con identacion
    forWrite = json.dumps(datos_diccio, indent=2)
    fichero.write(forWrite)
    fichero.close()
# cambios a fichero VS