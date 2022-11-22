import json
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
datos_diccio = []

# Objeto PEDIDO
class pedido(BaseModel):
    codigo:str
    cedulacliente:str
    fecha:str
    detalle:str
    total:str
    estado:str

@app.get("/select-pedido")
def mostrar_pedido():
    readDatosDiccio()
    return datos_diccio

@app.post("/insert-pedido") 
async def guardar_pedido(datos:pedido):
    readDatosDiccio()
    encode_datos = jsonable_encoder(datos)
    datos_diccio.append(encode_datos)
    writeDatosDiccio()
    return {"Mensaje":"Registro almacenado"}

@app.put("/update-pedido") 
def actualizar_pedido(datos:pedido):
    print(datos)
    readDatosDiccio()
    estado = False
    id = 0
    for item in datos_diccio:
        if item["codigo"] == datos.codigo:
            datos_diccio[id]["cedulacliente"] = datos.cedulacliente
            datos_diccio[id]["fecha"] = datos.fecha
            datos_diccio[id]["detalle"] = datos.detalle
            datos_diccio[id]["total"] = datos.total
            datos_diccio[id]["estado"] = datos.estado
            writeDatosDiccio()
            estado = True
            break 
        id += 1

    if estado == True:
        return {"Mensaje": "Registro de pedido actualizado"}
    else:
        return {"Mensaje": "Registro de pedido no encontrado"}

@app.delete("/delete-pedido")
def eliminar_pedido(datos:pedido):
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
        return {"Mensaje": "Registro de pedido eliminado"}
    else:
        return {"Mensaje": "Registro de pedido no encontrado"}

# abro archivo json y convierto en dicionario
def readDatosDiccio():
    fichero = open("pedido.json", "r")
    global datos_diccio
    datos_diccio = json.loads(fichero.read())
    fichero.close()

def writeDatosDiccio():
    fichero = open("pedido.json", "w")
    #convierto diccionario a archivo Json con identacion
    forWrite = json.dumps(datos_diccio, indent=2)
    fichero.write(forWrite)
    fichero.close()
