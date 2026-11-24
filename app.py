from fastapi import FastAPI

# Crear la aplicación
app = FastAPI(
    title="MikroTik WhatsApp Alerts",
    description="API para recibir alertas de dispositivos de red",
    version="1.0.0"
)


# Endpoint de comprobación
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API funcionando correctamente"
    }

