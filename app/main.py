from fastapi import FastAPI
from app.routes import profile

app = FastAPI(
    title="Api de portafolio - Brian Tifá",
    version="1.0.0",   
)

app.include_router(profile.router)


@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo!!!"}