from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Transaction(BaseModel):
    valor: float
    tipo: str
    descricao: str


@app.post("/clientes/{id}/transacoes")
async def criar_transacao(id: int, transaction: Transaction):
    # Aqui você pode processar a transação, salvar no banco de dados, etc.
    # Por enquanto, vamos apenas retornar os dados recebidos.
    return {"id_cliente": id, "transacao": transaction}
