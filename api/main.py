from fastapi import FastAPI

app = FastAPI()

@app.get("/saludar")
async def saludar():
    return{"Mensaje":"Hola mundo!"}
