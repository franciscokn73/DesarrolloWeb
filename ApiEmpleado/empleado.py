import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
datos_diccio = []

# Objeto persona
class empleado(BaseModel):
    cedula:str
    cargo:str
    rol:str
    nombre:str
    apellido:str
    telefono:str
    correo:str

@app.get("/select")
def mostrar():
    readDatosDiccio()
    return datos_diccio

@app.post("/insert") 
async def guardar(datos:empleado):
    readDatosDiccio()
    encode_datos = jsonable_encoder(datos)
    datos_diccio.append(encode_datos)
    writeDatosDiccio()
    return {"Mensaje":"Registro almacenado"}

@app.put("/update") 
def actualizar(datos:empleado):
    print(datos)
    readDatosDiccio()
    estado = False
    id = 0
    for item in datos_diccio:
        if item["cedula"] == datos.cedula:
            datos_diccio[id]["rol"] = datos.rol
            datos_diccio[id]["nombre"] = datos.nombre
            datos_diccio[id]["apellido"] = datos.apellido
            datos_diccio[id]["telefono"] = datos.telefono
            datos_diccio[id]["correo"] = datos.correo
            writeDatosDiccio()
            estado = True
            break 
        id += 1

    if estado == True:
        return {"Mensaje": "Registro actualizado"}
    else:
        return {"Mensaje": "Registro no encontrado"}

@app.delete("/delete")
def eliminar(datos:empleado):
    print(datos)
    readDatosDiccio()
    id = 0
    estado = False
    for item in datos_diccio:
        if item["cedula"] == datos.cedula:
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
    fichero = open("empleado.json", "r")
    global datos_diccio
    datos_diccio = json.loads(fichero.read())
    fichero.close()

def writeDatosDiccio():
    fichero = open("empleado.json", "w")
    #convierto diccionario a archivo Json con identacion
    forWrite = json.dumps(datos_diccio, indent=2)
    fichero.write(forWrite)
    fichero.close()