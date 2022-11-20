import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
datos_diccio = []

# Objeto persona
class envio(BaseModel):
    guia:str
    keyCliente:str
    keyTransportador:str

@app.get("/select/envio")
def mostrar():
    readDatosDiccio()
    return datos_diccio

@app.post("/insert/envio") 
async def guardar(datos:envio):
    readDatosDiccio()
    encode_datos = jsonable_encoder(datos)
    datos_diccio.append(encode_datos)
    writeDatosDiccio()
    return {"Mensaje":"Registro almacenado"}

@app.put("/update/envio") 
def actualizar(datos:envio):
    print(datos)
    readDatosDiccio()
    estado = False
    id = 0
    for item in datos_diccio:
        if item["guia"] == datos.guia:
            datos_diccio[id]["keyCliente"] = datos.keyCliente
            datos_diccio[id]["keyTransportador"] = datos.keyTransportador
            writeDatosDiccio()
            estado = True
            break 
        id += 1

    if estado == True:
        return {"Mensaje": "Registro actualizado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

@app.delete("/delete/envio")
def eliminar(datos:envio):
    print(datos)
    readDatosDiccio()
    id = 0
    estado = False
    for item in datos_diccio:
        if item["guia"] == datos.guia:
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
    fichero = open("envio.json", "r")
    global datos_diccio
    datos_diccio = json.loads(fichero.read())
    fichero.close()

def writeDatosDiccio():
    fichero = open("envio.json", "w")
    #convierto diccionario a archivo Json con identacion
    forWrite = json.dumps(datos_diccio, indent=2)
    fichero.write(forWrite)
    fichero.close()