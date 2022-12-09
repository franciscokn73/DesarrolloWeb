import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
datos_diccio = []

# Objeto persona
class vehiculo(BaseModel):
    serialMotor:str
    tipo:str
    categoria:str
    marca:str
    modelo:str
    color:str
    año:int
    pais:str
    valor:int
    valorString:str
    accesorios:str
    urlFoto:str

@app.get("/select/vehiculo")
def mostrar():
    readDatosDiccio()
    return datos_diccio

@app.post("/insert/vehiculo") 
async def guardar(datos:vehiculo):
    readDatosDiccio()
    encode_datos = jsonable_encoder(datos)
    datos_diccio.append(encode_datos)
    writeDatosDiccio()
    return {"Mensaje":"Registro almacenado"}

@app.put("/update/vehiculo") 
def actualizar(datos:vehiculo):
    print(datos)
    readDatosDiccio()
    estado = False
    id = 0
    for item in datos_diccio:
        if item["serialMotor"] == datos.serialMotor:
            datos_diccio[id]["tipo"] = datos.tipo
            datos_diccio[id]["categoria"] = datos.categoria
            datos_diccio[id]["marca"] = datos.marca
            datos_diccio[id]["modelo"] = datos.modelo
            datos_diccio[id]["color"] = datos.color
            datos_diccio[id]["año"] = datos.año
            datos_diccio[id]["pais"] = datos.pais
            datos_diccio[id]["valor"] = datos.valor
            datos_diccio[id]["accesorios"] = datos.accesorios
            datos_diccio[id]["urlFoto"] = datos.urlFoto
            writeDatosDiccio()
            estado = True
            break 
        id += 1

    if estado == True:
        return {"Mensaje": "Registro actualizado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

@app.delete("/delete/vehiculo")
def eliminar(datos:vehiculo):
    print(datos)
    readDatosDiccio()
    id = 0
    estado = False
    for item in datos_diccio:
        if item["serialMotor"] == datos.serialMotor:
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
    fichero = open("vehiculo.json", "r")
    global datos_diccio
    datos_diccio = json.loads(fichero.read())
    fichero.close()

def writeDatosDiccio():
    fichero = open("vehiculo.json", "w")
    #convierto diccionario a archivo Json con identacion
    forWrite = json.dumps(datos_diccio, indent=2)
    fichero.write(forWrite)
    fichero.close()