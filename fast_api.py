
#bibliotecas
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from modelo import carregar_modelo, fazer_predicao


class User_input(BaseModel):
    DiaSemana: str
    FaixaHora: str
    Mes: int
    ClienteID: str
    QuantidadeItens: int
    Vendas: float
    MediaPreco: float
    QtdItensDistintos:int
    QtdProduto1: int
    QtdProduto2: int
    QtdProduto3: int
    QtdProduto4: int
    QtdProduto5: int
    QtdProduto6: int
    QtdProduto7: int
    QtdProduto8: int
    QtdProduto9: int
    QtdProduto10: int
    QtdProduto11: int
    QtdProduto12: int
    QtdProduto13: int


app = FastAPI()

caminho_do_modelo = 'modelo.pkl'
modelo = carregar_modelo(caminho_do_modelo)


@app.post("/fazer_predicao")
def operate(input:User_input):
    resultado = fazer_predicao(modelo,[input.DiaSemana, input.FaixaHora, input.Mes, input.ClienteID, input.QuantidadeItens,
                                       input.Vendas, input. MediaPreco, input.QtdItensDistintos, input.QtdProduto1,
                                       input.QtdProduto2, input.QtdProduto3, input.QtdProduto4, input.QtdProduto5, input.QtdProduto6,
                                       input.QtdProduto7, input.QtdProduto8, input.QtdProduto9, input.QtdProduto10, input.QtdProduto11,
                                       input.QtdProduto12, input.QtdProduto13])
    return {"resultado": resultado}




