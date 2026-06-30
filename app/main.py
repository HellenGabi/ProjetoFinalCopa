from fastapi import FastAPI
from app.routes.router import router

app = FastAPI(
    title="Álbum da Copa 2026"
)

app.include_router(router)

@app.get("/")
def home():
    return {"mensagem": "API do Álbum da Copa funcionando!"}