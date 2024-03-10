
#bibliotecas
import streamlit as st
import json
import requests


#Titulo
st.title('Modelo de propensão a faturas canceladas')

#Subtítulo
st.write('Preencha as informações da sua fatura.\n\n')

#DiaDaSemana
opcao_1 = st.selectbox('Escolha o dia da semana',('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'))

#FaixaHorária
opcao_2 = st.selectbox('Escolha a faixa horária',('Manhã','Tarde','Noite','Madrugada'))

#Mês
st.write('Escolha o mês')
opcao_3 = int(st.slider('Mês', 0, 12, 1))

#ClienteID
opcao_4 = st.text_input('Digite o ClienteID:')

#Qtd_Itens
opcao_5 = st.number_input('Digite a quantidade de itens:', min_value = 0)

#Vendas
opcao_6 =  st.number_input('Digite o valor de vendas:', min_value = 0.0)

#Média_Preço
opcao_7 = st.number_input('Digite a média de preço:', min_value = 0.0)

#Qtd_Itens_Distintos
opcao_8  = st.number_input('Digite a quantidade de itens distintos:', min_value=0)

#produto1
opcao_9  = st.number_input('Digite a quantidade de itens do produto "20971 - PINK BLUE FELT CRAFT TRINKET BOX":', min_value=0)

#produto2
opcao_10  = st.number_input('Digite a quantidade de itens do produto "21108 - FAIRY CAKE FLANNEL ASSORTED COLOUR":', min_value=0)

#produto3
opcao_11  = st.number_input('Digite a quantidade de itens do produto "22423 - REGENCY CAKESTAND 3 TIER":', min_value=0)

#produto4
opcao_12  = st.number_input('Digite a quantidade de itens do produto "23113 - PANTRY CHOPPING BOARD":', min_value=0)

#produto5
opcao_13  = st.number_input('Digite a quantidade de itens do produto "23166 - MEDIUM CERAMIC TOP STORAGE JAR":', min_value=0)

#produto6
opcao_14  = st.number_input('Digite a quantidade de itens do produto "23843 - PAPER CRAFT,LITTLE BIRDIE":', min_value=0)

#produto7
opcao_15  = st.number_input('Digite a quantidade de itens do produto "47566B - TEA TIME PARTY BUNTING":', min_value=0)

#produto8
opcao_16  = st.number_input('Digite a quantidade de itens do produto "48185 - DOORMAT FAIRY CAKE":', min_value=0)

#produto9
opcao_17 = st.number_input('Digite a quantidade de itens do produto "71477 - COLOUR GLASS. STAR T-LIGHT HOLDER":', min_value=0)

#produto10
opcao_18  = st.number_input('Digite a quantidade de itens do produto "79323P - PINK CHERRY LIGHTS":', min_value=0)

#produto11
opcao_19  = st.number_input('Digite a quantidade de itens do produto "79323W - WHITE CHERRY LIGHTS":', min_value=0)

#produto12
opcao_20  = st.number_input('Digite a quantidade de itens do produto "84078A - SET/4 WHITE RETRO STORAGE CUBES":', min_value=0)
 
#produto13
opcao_21  = st.number_input('Digite a quantidade de itens do produto "85123A - WHITE HANGING HEART T-LIGHT HOLDER":', min_value=0)


entradas = {"DiaSemana": opcao_1, "FaixaHora": opcao_2, "Mes": opcao_3, "ClienteID": opcao_4, "QuantidadeItens": opcao_5,
            "Vendas": opcao_6, "MediaPreco":opcao_7, "QtdItensDistintos": opcao_8, "QtdProduto1": opcao_9,
            "QtdProduto2": opcao_10,"QtdProduto3": opcao_11, "QtdProduto4": opcao_12,"QtdProduto5": opcao_13,
            "QtdProduto6": opcao_14,"QtdProduto7": opcao_15,"QtdProduto8": opcao_16, "QtdProduto9": opcao_17, 
            "QtdProduto10": opcao_18,"QtdProduto11": opcao_19,"QtdProduto12": opcao_20,"QtdProduto13": opcao_21}


if st.button('Gerar previsão'):
    res = requests.post(url='https://case-cancelamento-vendas.onrender.com/fazer-predicao', json = entradas)

    # Verificar se a solicitação foi bem-sucedida (código 200)
    if res.status_code == 200:
        resposta_json = res.json()
        st.subheader(f"Resposta da API foi = {resposta_json}")
    else:
        st.subheader(f"Falha na solicitação. Código de status = {res.status_code}")    
    
#Descrição detalhada

# Este código Python cria uma interface web usando o Streamlit para que os usuários possam preencher informações relacionadas a uma fatura. Essas informações são enviadas para uma API hospedada no serviço Render, que utiliza um modelo
# para fazer previsões sobre se a fatura será cancelada ou não.

# Aqui está uma explicação detalhada do que cada parte do código faz:

# 1. **Importação de Bibliotecas**:
#   - Importa as bibliotecas necessárias para o funcionamento do programa, incluindo Streamlit, JSON e Requests.

# 2. **Interface Web**:
#   - Cria uma interface web usando o Streamlit.
#   - Define o título da página como "Modelo de propensão a faturas canceladas".
#   - Adiciona um subtítulo explicativo.

# 3. **Coleta de Entradas dos Usuários**:
#   - Usa widgets do Streamlit para coletar informações do usuário, como dia da semana, faixa horária, mês, ClienteID, quantidade de itens, vendas, média de preço, quantidade de itens distintos e quantidade de cada produto específico.

# 4. **Preparação dos Dados**:
#   - Cria um dicionário chamado `entradas` contendo todas as informações coletadas do usuário.

# 5. **Envio de Solicitação para a API**:
#   - Quando o usuário clica no botão "Gerar previsão", uma solicitação POST é enviada para a API hospedada no Render.
#   - Os dados coletados são enviados como um objeto JSON na solicitação.

# 6. **Processamento da Resposta da API**:
#   - Se a solicitação for bem-sucedida (código de status 200), a resposta da API é recebida e processada.
#   - A resposta é exibida na interface web como uma subseção com o título "Resposta da API".

# 7. **Tratamento de Falhas na Solicitação**:
#    - Se a solicitação falhar (por exemplo, se a API estiver fora do ar), uma mensagem indicando o código de status da falha é exibida na interface web.

# Em resumo, este código cria uma interface web interativa para que os usuários possam fornecer informações relacionadas a uma fatura. Essas informações são então enviadas para uma API que usa um modelo para fazer previsões sobre se a fatura
# será cancelada ou não, e a resposta da API é exibida de volta ao usuário na interface web.
