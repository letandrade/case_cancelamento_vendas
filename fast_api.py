
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


# Descrição detalhada do módulo fast_api.py

# 1. **Importação de Bibliotecas**:
#   - O código começa importando algumas bibliotecas necessárias para o desenvolvimento da API. FastAPI é usado para criar a API web, e Pydantic é usado para definir os modelos de entrada e saída da API. 
#     A biblioteca pickle é usada para carregar um modelo serializado que será usado para fazer previsões.

# 2. **Definição do Modelo de Entrada**:
#   - É definida uma classe `User_input` usando o Pydantic que representa os dados de entrada esperados pela API. Esta classe define os campos de dados necessários para fazer uma previsão.

# 3. **Inicialização da Aplicação FastAPI**:
#   - Uma instância do FastAPI é criada e atribuída à variável `app`.

# 4. **Rota Raiz da API**:
#   - Uma rota raiz (`"/"`) é definida usando o decorador `@app.get("/")`. Quando acessada, essa rota retorna uma mensagem de boas-vindas.

# 5. **Carregamento do Modelo Serializado**:
#   - O caminho para o arquivo que contém o modelo serializado é especificado na variável `caminho_do_modelo`. Em seguida, o modelo é carregado usando a função `carregar_modelo`.

# 6. **Rota para Fazer Predições**:
#   - É definida uma rota chamada `"/fazer-predicao"` usando o decorador `@app.post("/fazer-predicao")`. Esta rota aceita solicitações POST, onde os dados necessários para fazer a previsão são passados no corpo da solicitação.
   
# 7. **Função para Fazer Predições**:
#  - A função `operate` é definida para processar as solicitações na rota `"/fazer-predicao"`. Ela recebe os dados de entrada conforme definido pela classe `User_input`, faz a previsão usando o modelo carregado e retorna o resultado.

# Em resumo, este código define uma API web usando FastAPI que aceita solicitações POST contendo dados necessários para fazer uma previsão. Quando uma solicitação é recebida na rota `"/fazer-predicao"`, os dados são processados
#e uma previsão é feita usando um modelo carregado previamente. O resultado da previsão é então retornado como resposta da API.

