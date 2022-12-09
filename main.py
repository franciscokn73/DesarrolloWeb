import uvicorn

async def app(scope, receive, send):
    ...

if __name__ == "__main__":
    uvicorn.run("usuario:app", port=5000, log_level="info", reload="true", app_dir="C:/Users/User/Documents/Mintic/Ciclo4/Desarrollo web/Semana 2/ApisGestionVehiculos/DesarrolloWeb/ApiUsuario")
    uvicorn.run("vehiculo:app", port=6000, log_level="info", reload="true", app_dir="C:/Users/User/Documents/Mintic/Ciclo4/Desarrollo web/Semana 2/ApisGestionVehiculos/DesarrolloWeb/ApiVehiculo")
    uvicorn.run("empleado:app", port=7000, log_level="info", reload="true", app_dir="C:/Users/User/Documents/Mintic/Ciclo4/Desarrollo web/Semana 2/ApisGestionVehiculos/DesarrolloWeb/ApiEmpleado")
    uvicorn.run("envio:app", port=8000, log_level="info", reload="true", app_dir="C:/Users/User/Documents/Mintic/Ciclo4/Desarrollo web/Semana 2/ApisGestionVehiculos/DesarrolloWeb/ApiEnvio")

