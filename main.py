from fastapi import FastAPI
from pydantic import BaseModel
from agente.orquestrador import processar_comando

app = FastAPI(title="Agente Ale")

class Comando(BaseModel):
    texto: str

@app.post("/comando")
def comando(cmd: Comando):
    resposta = processar_comando(cmd.texto)
    return resposta
