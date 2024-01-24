
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

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de predição!"}

caminho_do_modelo = 'modelo.pkl'
modelo = carregar_modelo(caminho_do_modelo)

@app.post("/fazer-predicao")
def operate(input_data:User_input):
    resultado = fazer_predicao(modelo, [input_data.DiaSemana, input_data.FaixaHora, input_data.Mes, input_data.ClienteID, input_data.QuantidadeItens,
                                    input_data.Vendas, input_data.MediaPreco, input_data.QtdItensDistintos, input_data.QtdProduto1,
                                    input_data.QtdProduto2, input_data.QtdProduto3, input_data.QtdProduto4, input_data.QtdProduto5, input_data.QtdProduto6,
                                    input_data.QtdProduto7, input_data.QtdProduto8, input_data.QtdProduto9, input_data.QtdProduto10, input_data.QtdProduto11,
                                    input_data.QtdProduto12, input_data.QtdProduto13])
    
    return resultado




