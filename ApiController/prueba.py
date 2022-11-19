from pydantic import BaseModel

lista=[]

#Objeto persona
class Personas(BaseModel):
    nombre:str
    apellidos:str
    edad:int

#per:Personas

#per.nombre="Mauricio",
#per.apellidos="Hernandez",
#per.edad=38

lista.append({
    "nombre": "Mauricio",
    "apellidos": "Hernandez",
    "edad": 38
})

print(lista)